# Release validation

Version 0.1.0 was prepared on 2026-10-19 with these local checks:

| Check | Observed result |
|---|---|
| Skill metadata and naming | All nine skills passed the skill-creator validator |
| Advisory generated-skill scan | All nine skill entrypoints passed the converter's scan scope |
| Repository validator | Local Markdown file links, registry paths, portable document sync, and release-hygiene checks passed |
| Installer tests | Four tests passed: dry-run writes nothing, conflict preserves existing content and copies nothing, nested resources survive, source-tree destinations are refused |
| Installer CLI | Dry-run listed all nine skills without writing |
| Diagram checks | Both HTML sources passed diagram-design's packaged self-check |
| Browser rendering | Both PNGs rendered at 2560 x 1440 and were visually inspected |
| Narrow viewport | The role map scrolls inside its wrapper at 390px without horizontal page overflow |
| Public content review | No book PDF, extraction, private conversion pack, personal machine paths, or credentials were included |

The ready-to-enable workflow at `docs/ci/validate.yml` runs repository validation and installer unit tests on Windows and Linux when copied to `.github/workflows/validate.yml`. It is supplied as a template because the publishing login lacks workflow-upload scope. No remote CI run is claimed. See [activation instructions](ci/README.md).

Behavioral cases in `evals/` have not been run across all hosts or models. No accuracy, productivity, or token-savings benchmark is claimed. Diagram checking covers these supplied artifacts, not every future model generated from the skills.
