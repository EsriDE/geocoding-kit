---
description: "Task list for Python ArcGIS Location Platform geocoding example"
---

# Tasks: Python ArcGIS Geocoding Example

**Input**: Design documents from `/specs/001-arcgis-python-geocode/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, tooling, and example scaffolding.

- [ ] T001 Create Python project structure with `examples/`, `src/geocoding_kit/`, and `tests/` directories
- [ ] T002 Add `requirements.txt` listing `arcgis`, `python-dotenv`, and (optional) `pandas` (unittest is built into the standard library)
- [ ] T003 Add a minimal `README.md` section (or update existing) pointing to the example script and quickstart documentation
- [ ] T004 [P] Configure linting/formatting (e.g., `ruff`, `black`, or similar) and add a `pyproject.toml` or other config file
- [ ] T005 [P] Add a basic `.env.example` file documenting `ARCGIS_API_KEY` usage

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core library code and shared utilities that user stories depend on.

- [ ] T006 Create `src/geocoding_kit/config.py` to read `ARCGIS_API_KEY` (env var + optional `.env` support)
- [ ] T007 Create `src/geocoding_kit/models.py` defining `AddressInput` and `GeocodeResult` dataclasses
- [ ] T008 Create `src/geocoding_kit/geocode.py` using `arcgis.geocoding.Geocoder` that calls `geocodeAddresses` via the `arcgis.geocoding.geocode` function
- [ ] T009 [P] Create `examples/geocode_addresses.py` CLI script that reads a CSV, calls the geocoder instance, and writes output CSV
- [ ] T010 Add `tests/unit/test_config.py` verifying env var parsing and missing-key errors
- [ ] T011 Add `tests/unit/test_models.py` verifying data model serialization and field coverage
- [ ] T012 Add `tests/unit/test_geocode.py` with mocked geocode service responses to validate parsing and error handling

---

## Phase 3: User Story 1 - Run a Python geocoding example (Priority: P1) 🎯 MVP

**Goal**: Deliver a working, copy/paste-able Python script that geocodes a CSV list of addresses and produces a results CSV.

**Independent Test**: Run `python examples/geocode_addresses.py --input examples/addresses.csv --output examples/results.csv` with a valid `ARCGIS_API_KEY` and confirm output includes lat/lon for each address.

### Tests for User Story 1

- [ ] T013 [P] [US1] Add an integration test `tests/integration/test_geocode_example.py` that runs the CLI script against a small fixture CSV and asserts output columns exist

### Implementation for User Story 1

- [ ] T014 [US1] Create `examples/addresses.csv` fixture with 3 sample addresses
- [ ] T015 [US1] Implement CLI flags in `examples/geocode_addresses.py` (`--input`, `--output`, `--key`, `--batch-size`, `--verbose`)
- [ ] T016 [US1] Implement CSV input parsing and validation in `examples/geocode_addresses.py`
- [ ] T017 [US1] Implement CSV output writing including `matched_address`, `latitude`, `longitude`, `score`, `match_status`, and `error`
- [ ] T018 [US1] Add clear error messaging for missing API key, invalid auth, and file I/O issues

**Checkpoint**: The script runs end-to-end and produces expected output for valid addresses.

---

## Phase 4: User Story 2 - Handle missing/partial geocoding results gracefully (Priority: P2)

**Goal**: Ensure the example demonstrates reliable handling of no-match and ambiguous results without crashing.

**Independent Test**: Run the example with at least one invalid address and confirm output marks it as `NoMatch` and includes an `error` message while still processing the remaining addresses.

### Tests for User Story 2

- [ ] T019 [P] [US2] Add a unit test that verifies `GeocodeResult` is produced with `match_status=NoMatch` and an `error` field when the ArcGIS response indicates no match
- [ ] T020 [P] [US2] Add a unit test that verifies the best match is selected and the score is present when ArcGIS returns multiple candidates

### Implementation for User Story 2

- [ ] T021 [US2] Implement logic in `src/geocoding_kit/geocode.py` to map ArcGIS response statuses to `match_status`/`error` values
- [ ] T022 [US2] Update `examples/geocode_addresses.py` to continue processing on per-row errors and to record failures in output
- [ ] T023 [US2] Add documentation comments in the example explaining how to interpret `match_status`, `score`, and `error`

**Checkpoint**: The example returns a result row for every input row and clearly indicates missing/ambiguous matches.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Cleanup, docs, and usability improvements across all stories.

- [ ] T024 [P] Update `specs/001-arcgis-python-geocode/quickstart.md` with the final CLI example flags and any updated file names
- [ ] T025 [P] Add README instructions for running the example and setting `ARCGIS_API_KEY`
- [ ] T026 [P] Add `examples/README.md` describing how to run the example and interpret output
- [ ] T027 [P] Add additional unit tests for edge cases: empty input file, invalid CSV format, and rate-limiting retry behavior
- [ ] T028 [P] Ensure linting/format checks pass and update CI config (if present) to include these checks

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can proceed in parallel once foundation is ready
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2)
- **User Story 2 (P2)**: Can start after Foundational (Phase 2)

### Parallel Opportunities

- Separate tasks in the Setup and Foundational phases are marked [P] where they can be worked on concurrently.
- Once the foundation is in place, User Story work (US1 vs US2) can be owned by different contributors in parallel.
- Unit tests for different behaviors are marked [P] and can be implemented concurrently.

---

## Implementation Strategy

- **MVP first**: Deliver the simplest working end-to-end script (US1) with minimal dependencies and clear documentation.
- **Incrementally improve**: Add resilience (US2), better error handling, and user guidance once the baseline script is working.
- **Keep examples runnable**: Ensure any example in docs remains runnable; update quickstart and READMEs as code changes.
