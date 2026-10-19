# Host compatibility

The content is plain Markdown with Agent Skills frontmatter. These placement conventions were checked against primary host documentation on 2026-10-19. Installation paths may evolve. The public release has local packaging checks; it has not been behaviorally tested in every product below.

| Host | Example project root for the installer | Notes / primary documentation |
|---|---|---|
| Claude Code | `.claude/skills` | [Skills](https://code.claude.com/docs/en/skills) |
| Codex | `.agents/skills` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| Cursor | `.cursor/skills` or `.agents/skills` | [Skills](https://cursor.com/help/customization/skills) |
| GitHub Copilot | `.github/skills` on supported surfaces | [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) |
| Visual Studio Code | Depends on the active AI harness | The editor itself does not provide a universal agent runner |
| OpenCode | `.opencode/skills` or `.agents/skills` | [Skills](https://opencode.ai/docs/skills/) |
| Hermes | Active Hermes home: `skills/business-analysis` | [Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| ChatGPT | Use supported skill import, or portable documents | [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins) |
| Rovo | Agent instructions and authorized knowledge sources | [Rovo agents](https://support.atlassian.com/rovo/docs/agents/) |

## Install folder-based skills

```bash
python scripts/install.py --root /path/to/project/.agents/skills --dry-run
python scripts/install.py --root /path/to/project/.agents/skills
```

Use the destination supported by your selected host. Windows paths are accepted; quote paths containing spaces. Existing destination skills are preserved: any name conflict stops the complete installation before copying. The installer does not modify editor settings, credentials, or remote services.

## Use portable roles

Supply `portable/START-HERE.md` and one or more documents from `portable/roles/`. Each role document embeds its own templates/references. The orchestrator's portable document names the other roles; those guides still need to be supplied if the host cannot retrieve them. A ZIP is not assumed to be readable by every interface.

For Rovo, configure a role's instructions and supported knowledge source using your site's setup. For ChatGPT, use the file/instructions mechanism available in your workspace. Neither operation has been performed by this repository. An uploaded role document does not itself create a separately running agent.

## Tool and model limits

- Any model that can use the supplied instructions can attempt the workflows. Context capacity and reasoning quality affect results.
- Research requires actual source access. Without it, produce a plan and mark hypotheses.
- Rendering/export requires a suitable browser or execution environment. Without it, return diagram source and report visual verification pending.
- Separate agents require a host delegation feature and authorization. Otherwise apply roles sequentially.
- Python 3.10+ is required only for the optional repository scripts; they use the standard library.

## Verify on your host

Ask the assistant to identify a supplied skill, apply one focused evaluation case from `evals/`, and report the artifact, evidence, and checks performed. Explicit skill loading and automatic selection are separate behaviors to test. Share host versions and observed results when reporting compatibility.
