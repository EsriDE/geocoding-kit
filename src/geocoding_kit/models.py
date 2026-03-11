from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AddressInput:
    """A single address to be geocoded."""

    id: str
    address: str
    postal: str
    city: str
    country: str


@dataclass(frozen=True)
class GeocodeResult:
    """The result of geocoding an address."""

    id: str
    input_address: str
    matched_address: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    score: Optional[float]
    match_type: Optional[str]
    match_status: str
    error: Optional[str] = None
