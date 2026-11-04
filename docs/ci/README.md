# GitHub Actions checks

The active [validation workflow](../../.github/workflows/validate.yml) runs packaging validation and installer tests with read-only repository permissions on Ubuntu and Windows using Python 3.12. It triggers on pushes and pull requests. No remote run is claimed by this document.

[validate.yml](validate.yml) remains a portable copy for downstream users. Keep it aligned with the active workflow when changing checks. See [the validation record](../validation.md) for historical local evidence and limitations.
