# Contributing

Make a real analysis task easier to complete and review. Prefer a focused improvement over adding another broad agent role.

## Before opening a pull request
1. Explain the concrete situation, current failure, and expected behavior.
2. Keep the skill's trigger narrow and its instructions useful to a capable model.
3. Include a synthetic or redistributable example when it clarifies the change.
4. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.
5. If you edited skills or templates, run `python scripts/build_portable.py` and include refreshed portable documents.
6. Report behavioral tests honestly: model/host, input, observed artifact, and limitations. Do not invent pass rates or benchmark results.

Do not include copyrighted manuals, member-only book summaries, customer records, credentials, personal information, or confidential company material. Permission to access a source does not by itself establish redistribution rights.

## Good first contributions
- A testable exception missing from a worked example.
- A routing case where two roles are easily confused.
- Verified instructions for one specific host version.
- A smaller, clearer artifact template.

By contributing, you agree that your original contributions are available under this repository's MIT license and that you have the right to contribute them.
