# Data Model: Add Geocode Notebook

## Overview
The notebook feature involves two primary data entities: input addresses to be geocoded and the resulting geocoded locations with coordinates.

## Entities

### Address
Represents location information to be geocoded.
See `geocoding_kit.models.AddressInput`

**Validation Rules**:
- At least one of street, city, or zip must be provided
- String fields should be trimmed of whitespace

**Relationships**:
- One-to-one with Geocode Result

### Geocode Result
Represents the output of geocoding an address, including matched location and confidence.
See `geocoding_kit.models.GeocodeResult`.

**Validation Rules**:
- Latitude must be between -90 and 90
- Longitude must be between -180 and 180
- Confidence score must be between 0.0 and 100.0

**Relationships**:
- One-to-one with Address (result of geocoding that address)

## Data Flow
1. Addresses loaded from CSV file
2. Each address geocoded using the geocoder
3. Results collected and displayed in notebook
4. Results may include coordinates for mapping visualization