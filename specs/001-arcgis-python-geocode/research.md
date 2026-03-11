# Research: ArcGIS Location Platform Geocoding (Python)

## Decision: Use `arcgis` (ArcGIS API for Python) + `geocodeAddresses` endpoint

**Decision**: Implement the example using the official `arcgis` Python package, calling the `geocode_addresses` method on `arcgis.geocoding.Geocoder` (which targets the `https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/geocodeAddresses` endpoint).  

**Rationale**:
- `arcgis` is the officially supported Python SDK for ArcGIS and includes built-in handling for authentication, rate limiting headers, and JSON parsing.
- `geocode_addresses` maps directly to the required REST endpoint and accepts a CSV-style payload, making it simple to integrate with a local input CSV file.
- It provides a clean, documented API that minimizes the amount of boilerplate in the onboarding example.

**Alternatives considered**:
- **Raw HTTP requests (requests/urllib)**: would work, but would require reimplementing auth signing, parsing, and rate-limit detection. Higher chance of drift from ArcGIS API changes.
- **ArcGIS REST JS or other language SDKs**: Not applicable for a Python-focused onboarding example.

---

## Decision: Use environment variable for credentials, default to `ARCGIS_API_KEY`

**Decision**: Require an environment variable `ARCGIS_API_KEY` (or `ARCGIS_TOKEN`) for authentication. Provide a helper that reads `.env` files if present.

**Rationale**:
- Keeps examples simple and secure: no hard-coded keys in code.
- Matches common patterns used by ArcGIS Python tutorials and other SDKs.
- Allows CI/users to run locally without editing code.

**Alternatives considered**:
- Using a config file (YAML/JSON) for credentials: adds complexity for a demo.
- Prompting for credentials interactively: not suitable for CI and automated tests.

---

## Decision: Provide CSV input + CSV output

**Decision**: Accept input as a plain CSV file (one address per row or structured columns) and output a CSV with appended lat/lon/score columns.

**Rationale**:
- CSV is the simplest cross-platform data interchange format for non-technical users and scripts.
- It fits the user request and avoids introducing databases or dependencies beyond `pandas` (optional) or the Python `csv` module.

**Alternatives considered**:
- JSON input/output: more verbose and less accessible to non-developers.
- Database-backed input: overkill for a simple onboarding example.

---

## Decision: Provide clear failure handling (auth, rate limit, no match)

**Decision**: The example will:
- Detect auth failures and show a helpful message (`Invalid API key`, `Authentication failed`).
- Detect rate limiting (HTTP 429) and recommend a backoff strategy.
- Mark non-matched addresses clearly in output without stopping the entire batch.

**Rationale**:
- Helps users understand why an address failed and how to recover.
- Aligns with the constitution principle that errors must be informative and actionable.

**Alternatives considered**:
- Failing fast on first error: would make the example less robust and less suitable for real-world address lists.
- Swallowing errors silently: would violate the constitution’s emphasis on clarity.
