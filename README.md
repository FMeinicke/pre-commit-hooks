# pre-commit-hooks

Collection of useful pre-commit hooks.

See also: <https://github.com/pre-commit/pre-commit>

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/FMeinicke/pre-commit-hooks
  rev: v0.1.0
  hooks:
    - id: ...
```

## Available hooks

### `check-no-special-commits`

Prevent pushing commits that contain certain "special" prefixes.

- Specify the prefixes to check for with `args: ["dont-push! ", "fix-me! "]`  
  By default (or if `args: []`), `["squash! ", "fixup! ", "amend! "]` (special prefixes that are used in combination with `git rebase --autosquash`).
