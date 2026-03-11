# Feature Specification: Python ArcGIS Geocoding Example

**Feature Branch**: `001-arcgis-python-geocode`  
**Created**: 2026-03-11  
**Status**: Draft  
**Input**: User description: "Show how to use our geocoding service of ArcGIS Location Platform with a simple Python example"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Run a Python geocoding example (Priority: P1)

As a developer, I want a minimal, copy/paste-ready Python example that geocodes a list of addresses using the ArcGIS Location Platform so I can quickly validate the service and integrate it into my workflow.

**Why this priority**: Demonstrating a working end-to-end sample is the fastest way to prove the value of the geocoding service and onboard new users.

**Independent Test**: Run the provided `examples/geocode_addresses.py` script (or equivalent) with a valid API key and verify that it produces a list of coordinates for the input addresses.

**Acceptance Scenarios**:

1. **Given** a file or in-code list of valid street addresses and a valid ArcGIS Location Platform API key, **when** the example script is executed, **then** the output includes each input address mapped to a latitude/longitude coordinate pair.
2. **Given** an invalid API key or expired token, **when** the script runs, **then** it fails with a clear error message explaining the authentication issue (e.g., "Invalid API key" or "Authentication failed").

---

### User Story 2 - Handle missing/partial geocoding results gracefully (Priority: P2)

As a developer, I want the example code to clearly show how to handle addresses that cannot be geocoded (e.g., no match or ambiguous result) so I can build resilient integrations.

**Why this priority**: Real-world address lists often contain typos, PO boxes, or incomplete data; demonstrating graceful handling reduces support questions and improves user trust.

**Independent Test**: Run the example with at least one intentionally invalid/ambiguous address and verify the output indicates which addresses could not be resolved and why.

**Acceptance Scenarios**:

1. **Given** an address that cannot be matched, **when** the script runs, **then** it logs or returns a clear indication that the address was not found and continues processing the remaining addresses.
2. **Given** an address that yields multiple possible matches, **when** the script runs, **then** it returns the best match and includes a confidence/score value.

---

### Edge Cases

- What happens when the network connection drops mid-request? The example should show a retry strategy or a clear error message.
- How does the script behave when the ArcGIS service returns a rate-limit response (HTTP 429)? The guidance should suggest backoff and retry.
- How does the feature behave when the input list is empty? It should exit cleanly without making API calls.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST include a Python example (script or library API) that accepts a list of addresses and returns geocoding results using ArcGIS Location Platform.
- **FR-002**: System MUST accept configuration for authentication (API key or token) via environment variable and/or configuration file.
- **FR-003**: System MUST return structured results including at least: input address, matched address (if different), latitude, longitude, and match confidence/score.
- **FR-004**: System MUST detect and surface common failures (authentication errors, rate limits, invalid input) with user-friendly messages.
- **FR-005**: Documentation (README or docs/quickstart) MUST include a complete, runnable example that can be copy/pasted and executed as-is.

### Key Entities *(include if feature involves data)*

- **AddressInput**: A user-provided address string requiring geocoding.
- **GeocodeResult**: The geocoding response that includes the matched address, latitude, longitude, and confidence score.
- **ArcGISConfig**: Authentication and endpoint configuration needed to call ArcGIS Location Platform.

## Assumptions

- Users have access to an ArcGIS Location Platform account and a valid API key or token.
- The repository will include a small example script under `examples/` (or similar) that can be executed directly.
- The example will not be production-grade; it is intended for onboarding and learning.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A developer can run the provided Python example and see geocoding results for at least 3 sample addresses within 5 minutes of cloning the repo.
- **SC-002**: The example clearly indicates when an address could not be geocoded and does not terminate processing for remaining addresses.
- **SC-003**: The documentation example is copy/paste runnable with no modifications beyond setting API credentials.
- **SC-004**: Users can diagnose authentication failures from the output message without needing to inspect the code.

## Clarifications

### Session 2026-03-11
- Q: Does the output CSV include an `error` column when geocoding fails?
  → A: No. The script uses `match_status` to indicate success or failure (e.g., `M`, `T`, `U`). The output CSV does not include a separate `error` column.
