# Data Model: ArcGIS Geocoding Example

This feature is primarily focused on transforming a list of input addresses into geocoded results using ArcGIS Location Platform.

## Entities

### AddressInput
Represents a single address to be resolved.

- **id**: string (optional) – A stable identifier for each row (e.g., row number or user-provided ID).
- **raw_address**: string – The freeform address text to geocode.
- **street** (optional): string – Street address portion.
- **city** (optional): string – City name.
- **region** (optional): string – State/region.
- **postal** (optional): string – Postal code.
- **country** (optional): string – Country/region.

### GeocodeResult
Represents the output from ArcGIS after attempting to geocode an `AddressInput`.

- **id**: string (matches AddressInput.id if provided)
- **input_address**: string (original address string)
- **matched_address**: string (normalized address returned by ArcGIS)
- **latitude**: float
- **longitude**: float
- **score**: float (match confidence score)
- **match_type**: string (e.g., "PointAddress", "StreetAddress")
- **match_status**: string (e.g., "Matched", "NoMatch")
- **error**: string (optional; populated when geocoding fails or no match)

## Relationships

- Each `AddressInput` yields exactly one `GeocodeResult` in the output, even when no match is found (the result includes `match_status` and optional `error`).
