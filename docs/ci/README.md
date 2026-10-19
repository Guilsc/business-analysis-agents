# Enable GitHub Actions checks

The repository includes a ready-to-enable [workflow template](validate.yml). It runs the packaging validator and installer unit tests on Windows and Linux with read-only repository permissions.

To activate it, use an account/token permitted to manage workflows and copy the file to `.github/workflows/validate.yml`. Commit and push that change. In GitHub's web editor, creating the same file under `.github/workflows/` is another option for an authorized repository owner.

The initial publishing login did not include the `workflow` OAuth scope, so this release ships the template without activating it. Local validation and installer tests passed; no remote run or status badge is implied.

After activation, the workflow appears in the Actions tab. You can then replace the README's local-check badge with the actual workflow-status badge.
