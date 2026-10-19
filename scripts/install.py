"""Copy the complete skill set to an explicit host root, preserving existing skills."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil

REPO = Path(__file__).resolve().parents[1]


def install(destination: Path, *, dry_run: bool = False, source: Path | None = None) -> list[str]:
    source = (source or REPO / "skills").resolve()
    destination = destination.expanduser().resolve()
    skills = sorted(p for p in source.iterdir() if (p / "SKILL.md").is_file())
    if not skills:
        raise ValueError("No skill directories found")
    if destination == source or any(p == destination or p in destination.parents for p in skills):
        raise ValueError("Destination must not be the source skill tree")
    conflicts = [p.name for p in skills if os.path.lexists(destination / p.name)]
    if conflicts:
        raise FileExistsError("Existing skills preserved; choose another root: " + ", ".join(conflicts))
    if not dry_run:
        destination.mkdir(parents=True, exist_ok=True)
        for skill in skills:
            # copytree also refuses a destination created after the preflight.
            shutil.copytree(skill, destination / skill.name)
    return [p.name for p in skills]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="Host's destination skills directory")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        names = install(args.root, dry_run=args.dry_run)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")
    print(("Would install" if args.dry_run else "Installed") + f" {len(names)} skills in {args.root}")
    print("\n".join(names))


if __name__ == "__main__":
    main()
