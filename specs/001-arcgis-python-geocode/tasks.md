---
description: "Task list for Python ArcGIS Location Platform geocoding example (completed)"
---

# Tasks: Python ArcGIS Geocoding Example

This task list tracks the implementation of the example script and supporting library. All tasks are now complete.

## Phase 1: Setup (Completed)

- [x] Create Python project structure with `examples/`, `src/geocoding_kit/`, and `tests/` directories
- [x] Add `requirements.txt` listing `arcgis` and `python-dotenv`
- [x] Add a minimal `README.md` section (or update existing) pointing to the example script and quickstart documentation
- [x] Add a basic `.env.example` file documenting `ARCGIS_API_KEY` usage

## Phase 2: Foundational (Completed)

- [x] Create `src/geocoding_kit/config.py` to read `ARCGIS_API_KEY` (env var + optional `.env` support)
- [x] Create `src/geocoding_kit/models.py` defining `AddressInput` and `GeocodeResult` dataclasses
- [x] Create `src/geocoding_kit/geocode.py` that calls `geocodeAddresses` and selects the best candidate
- [x] Create `examples/geocode_addresses.py` CLI script that reads a CSV, calls the geocoder, and writes output CSV
- [x] Add `tests/unit/test_config.py` verifying env var parsing and missing-key errors
- [x] Add `tests/unit/test_models.py` verifying the data model structure
- [x] Add `tests/unit/test_geocode.py` verifying parsing logic and best-candidate selection
- [x] Add `tests/unit/test_geocode_sample_address.py` validating parsing logic against a real sample address
- [x] Add `tests/integration/test_geocode_example.py` that runs the CLI script with mocked geocoding and verifies output schema

## Notes

- The example can be run with `python examples/geocode_addresses.py --input examples/addresses.csv --output results.csv` once dependencies are installed.
- The script is intentionally minimal and focuses on showing correct API usage and result parsing.
