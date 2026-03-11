# Data Model: ArcGIS Geocoding Example

This feature is primarily focused on transforming a list of input addresses into geocoded results using ArcGIS Location Platform.

## Entities

### AddressInput
Represents a single address to be resolved.

- **id**: int (optional) – A stable identifier for each row (e.g., row number or user-provided ID).
- **address**: string – The freeform address text to geocode.
- **postal** (optional): string – Street address portion.
- **city** (optional): string – City name.
- **country** (optional): string – Two letter ISO country code.

### GeocodeResult
Represents the output from the geocoding service after attempting to geocode an `AddressInput`.

- **id**: int (matches AddressInput.id if provided)
- **input_address**: string (original address string)
- **matched_address**: string (normalized address returned by ArcGIS)
- **latitude**: float
- **longitude**: float
- **score**: float (match confidence score)
- **match_type**: string (e.g., "PointAddress", "StreetAddress")
- **match_status**: string (e.g., "Matched", "Tied", "Unmatched")

## Relationships

- Each `AddressInput` yields exactly one `GeocodeResult` in the output, even when no match is found (the result includes `match_status`).
