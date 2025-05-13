# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
Types of changes

    `Added` for new features.
    `Changed` for changes in existing functionality.
    `Deprecated` for soon-to-be removed features.
    `Removed` for now removed features.
    `Fixed` for any bug fixes.
    `Security` in case of vulnerabilities.
-->

## [Unreleased]

## [v0.1.2] &ndash; 2025-05-13

### Changed

- Change hook stage `push` to `pre-push` for pre-commit v3.2.0.

## [v0.1.1] &ndash; 2024-11-04

### Fixed

- `check_no_special_commits` will default to check all commits reachable from the current `HEAD` if pre-commit doesn't
  provide a `from_ref` and `to_ref` (which is the case for the very first push in a new repo).

## [v0.1.0] &ndash; 2024-09-10

### Added

- `check-no-special-commits`: prevent pushing commits that contain certain "special" prefixes

[Unreleased]: https://github.com/FMeinicke/pre-commit-hooks/commits/main/
[v0.1.2]: https://github.com/FMeinicke/pre-commit-hooks/releases/tag/v0.1.2
[v0.1.1]: https://github.com/FMeinicke/pre-commit-hooks/releases/tag/v0.1.1
[v0.1.0]: https://github.com/FMeinicke/pre-commit-hooks/releases/tag/v0.1.0
