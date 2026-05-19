# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project scaffolding: `src/` layout, `pyproject.toml` (PEP 621/639), `uv.lock`.
- Typer-based CLI entry point (`hl-archive`) with `version` command and a `fetch` stub.
- Tooling: `ruff` (lint + format), `pytest` + `pytest-cov`, `ty` (type checker), `pre-commit`.
- GitHub Actions CI: lint, type check, and pytest matrix on Python 3.11 / 3.12 / 3.13.
- Dependabot for `uv` and `github-actions` ecosystems (weekly).
- Issue templates (bug report, feature request) and contact links.
- `.editorconfig` and pre-commit config for consistent contributor experience.
- MIT license, aspirational README with roadmap and caveats.

[Unreleased]: https://github.com/tomazzi14/hl-archive/compare/HEAD...HEAD
