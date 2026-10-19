"""Validate packaging, references, portable sync, and public-release hygiene."""
from pathlib import Path
import json
import re
import sys

from build_portable import render

REPO = Path(__file__).resolve().parents[1]


def validate(root: Path = REPO) -> list[str]:
    errors: list[str] = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        name = re.search(r"(?m)^name: ([a-z0-9]+(?:-[a-z0-9]+)*)$", match[1])
        desc = re.search(r'(?m)^description: "(.+)"$', match[1])
        if not name or name[1] != path.parent.name or len(name[1]) > 64:
            errors.append(f"{path.relative_to(root)}: invalid skill name")
        if not desc or len(desc[1]) > 1024:
            errors.append(f"{path.relative_to(root)}: invalid description")
        portable = root / "portable" / "roles" / (path.parent.name + ".md")
        if not portable.exists() or portable.read_text(encoding="utf-8") != render(path.parent):
            errors.append(f"{portable.relative_to(root)}: stale; run scripts/build_portable.py")
    if not skills:
        errors.append("No skills found")
    registry = root / "skills/ba-orchestrator/references/roles.json"
    if registry.exists():
        data = json.loads(registry.read_text(encoding="utf-8"))
        ids = [r["id"] for r in data["roles"]]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate registry role IDs")
        for role in data["roles"]:
            target = (registry.parents[1] / role["skill_path"]).resolve()
            if not target.is_relative_to((root / "skills").resolve()) or not target.is_file():
                errors.append(f"Registry target missing/outside skills: {role['id']}")
    else:
        errors.append("Missing role registry")
    for path in root.rglob("*"):
        if any(p in {".git", "__pycache__", ".venv"} for p in path.relative_to(root).parts):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in {".pdf", ".zip"} or path.name in {"full_text.txt", "metadata.json", "INSTALLATION.json"}:
            errors.append(f"Private/source or binary archive artifact: {path.relative_to(root)}")
        if path.suffix not in {".md", ".json", ".html", ".csv", ".yml", ".py", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"[A-Z]:[\\/]Users[\\/]|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}", text):
            errors.append(f"Possible personal path or credential: {path.relative_to(root)}")
        if path.suffix == ".md":
            prose = re.sub(r"```.*?```", "", text, flags=re.S)
            for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
                target = link.split("#", 1)[0]
                if not target or re.match(r"[a-z]+://", target):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f"{path.relative_to(root)}: broken/local-outside link {target}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(failures))
        sys.exit(1)
    print("Validated skills, registry, portable sync, local links, and public-release hygiene")
