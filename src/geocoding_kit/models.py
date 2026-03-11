from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AddressInput:
    """An input address to be geocoded."""

    id: int
    address: str
    postal: str
    city: str
    country: str

@dataclass(frozen=True)
class GeocodeResponse:
    """The item of a geocoding response."""

    address: str
    location: Optional[dict]
    score: Optional[float]
    attributes: Optional[dict]

@dataclass(frozen=True)
class GeocodeResult:
    """The result of geocoding an address."""

    id: int
    input_address: str
    matched_address: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    score: Optional[float]
    match_type: Optional[str]
    match_status: str
