<!--
SYNC IMPACT REPORT
- Version: (none) → 1.0.0
- Modified principles: (initial composition)
- Added sections: Quality & Performance Standards; Development Workflow
- Removed sections: (none)
- Templates reviewed: .specify/templates/plan-template.md ✅, .specify/templates/spec-template.md ✅, .specify/templates/tasks-template.md ✅
- Follow-up TODOs: none
-->

# geocoding-kit Constitution

## Core Principles

### I. Code Quality is Non-Negotiable
Every line shipped must be easy to read, easy to review, and easy to refactor. We enforce consistent formatting and linting in CI, require clear naming, and prefer small, focused functions/modules over large, opaque ones. Code should be safe by default: avoid global state, prefer immutability where practical, and document edge cases inline.

### II. Testing is the Ground Truth (NON-NEGOTIABLE)
Every behavior must be backed by automated tests before it is considered done. Unit tests validate logic in isolation; integration tests validate real-world boundaries; regression tests lock in bug fixes. All tests must be reproducible in CI with a single command and failing tests must block merges.

### III. User Experience Consistency
Consumers must be able to use the project with minimal friction. Public APIs, CLI interfaces, and examples must be consistent, predictable, and follow the same naming and error-handling patterns. Documentation snippets (quickstarts, README examples) must work copy/pasted without modification.

### IV. Performance is a First-Class Requirement
Performance goals are explicit: avoid needless allocations, keep latency predictable, and make performance trade-offs visible in code. Any feature that could impact speed or memory must include benchmark or profiling evidence. For non-trivial paths, we require measurable targets (e.g., p95 latency, memory budget) and automated checks where feasible.

### V. Easy-to-Use Code Snippets
Every sample in docs, README, and API docs must be end-to-end runnable and minimal. Prefer “copy→paste→run” snippets over conceptual pseudocode. When a snippet demonstrates a pattern, include the minimal necessary setup and imports so users can run it immediately.

## Quality & Performance Standards

- **Formatting & linting**: The repository must have a single source of truth for formatting and lint rules (e.g., `prettier`, `rustfmt`, `black`, `eslint`, or equivalent). All contributions must pass the lint/format check in CI.
- **Test coverage**: Critical paths must have automated coverage thresholds. Test suites must be fast enough for frequent runs; avoid excessive end-to-end tests where unit/integration tests suffice.
- **Benchmarking**: Performance-impacting areas should include a benchmark or a reproducible profiling case. If a change regresses performance, the author must document the trade-off and mitigation.
- **Error handling**: Errors must be informative and actionable. Avoid generic errors; include context and recovery hints when possible.

## Development Workflow

- **Branching**: Use short-lived feature branches. Each PR should implement one user story or one logical refactor.
- **Code review**: Every change must be reviewed by at least one other contributor. Reviews should validate adherence to these principles, confirm tests pass, and ensure documentation stays correct.
- **Documentation**: Every behavior visible to users must be documented (README, quickstart, inline code comments). Examples in docs must remain accurate; broken examples are treated as bugs.
- **CI gating**: The CI pipeline must run formatting, linting, unit tests, and (where applicable) integration tests. No merge until CI passes.

## Governance

This constitution is the single source of truth for development priorities and quality standards. Amendments require:

1. A documented proposal in a pull request describing the change, reasoning, and migration impact.
2. Review and approval by at least one other maintainer or stakeholder.
3. An update to this document (version bump) and any impacted templates or guidance docs.

**Versioning policy**
- Bump **MAJOR** for changes that alter or remove an existing principle in a way that breaks existing workflows.
- Bump **MINOR** for new principles, new mandatory standards, or material expansions of existing principles.
- Bump **PATCH** for wording clarifications, typo fixes, and purely editorial refinements.

**Compliance**
- Every PR must reference the applicable principle(s) and demonstrate how the proposed change complies.
- When automation exists (lint, tests, benchmarks), it must be enabled and run in CI.

**Version**: 1.0.0 | **Ratified**: 2026-03-11 | **Last Amended**: 2026-03-11
