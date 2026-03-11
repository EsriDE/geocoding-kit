# Implementation Plan: Python ArcGIS Geocoding Example

**Branch**: `001-arcgis-python-geocode` | **Date**: 2026-03-11 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-arcgis-python-geocode/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Provide a minimal, copy/paste runnable Python example that reads a CSV list of addresses, calls the ArcGIS Location Platform Geocoding REST endpoint (`https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/geocodeAddresses`) via the official `arcgis` Python module, and outputs geocoded coordinates with match scores. The goal is to onboard users quickly with a working script and clear guidance on authentication, error handling, and partial/missing results.

## Technical Context

**Language/Version**: Python 3.11+  
**Primary Dependencies**: `arcgis` (ArcGIS API for Python), `pandas` (for CSV handling, optional), `typer` (CLI helper, optional), `python-dotenv` (optional)  
**Storage**: Input: CSV file; output: CSV or stdout (no persistent storage required)  
**Testing**: `pytest` (unit tests + integration tests using local fixtures / mock responses)  
**Target Platform**: Linux/macOS (general desktop/workstation environment with network access)  
**Project Type**: Library + CLI example script (documentation + runnable sample)  
**Performance Goals**: Handle small-to-medium batches (hundreds–low thousands of addresses) with respect for ArcGIS rate limits; keep memory use minimal (streaming CSV processing when possible)  
**Constraints**: Must use ArcGIS Location Platform REST endpoint `geocodeAddresses`; must support API key or token auth via env var; must surface rate limiting (HTTP 429) and auth failures clearly; should remain easy to run without complex setup  
**Scale/Scope**: Aimed at “proof-of-concept” onboarding; not intended for high-throughput production ETL.  

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ **Code quality**: Plan assumes enforcement of formatting/linting (per constitution).  
- ✅ **Testing**: Plan commits to `pytest` and testable example scripts.  
- ✅ **User experience**: Plan focuses on copy/paste runnable examples and clear output.  
- ✅ **Performance**: Plan includes guidance for rate limiting and batching.  

## Project Structure

### Documentation (this feature)

```text
specs/001-arcgis-python-geocode/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
examples/
└── geocode_addresses.py

src/  # optional if we create a small library
└── geocoding_kit/
    ├── __init__.py
    ├── config.py
    └── geocode.py

tests/
├── unit/
└── integration/
```

**Structure Decision**: We'll ship a lightweight example script under `examples/` plus a small library (`src/geocoding_kit/`) for reusable logic. Tests live under `tests/`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (none) | (none) | (none) |
## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
