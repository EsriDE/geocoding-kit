from __future__ import annotations

from dataclasses import asdict
from typing import Dict, Iterable, List, Optional

from .config import ArcGISConfig
from .models import AddressInput, GeocodeResponse, GeocodeResult

try:
    from arcgis.gis import GIS
    from arcgis.geocoding import Geocoder, batch_geocode
except ImportError:  # pragma: no cover
    GIS = None  # type: ignore[assignment]
    Geocoder = None  # type: ignore[assignment]
    batch_geocode = None  # type: ignore[assignment]


class PlatformGeocoder:
    """Wraps ArcGIS Location Platform geocoding calls."""

    def __init__(self, config: ArcGISConfig) -> None:
        self._config = config

    def geocode(
        self,
        addresses: Iterable[AddressInput],
        batch_size: int = 100,
    ) -> List[GeocodeResult]:
        """Geocodes a list of addresses.

        Args:
            addresses: List of AddressInput entries.
            batch_size: Number of addresses to send per request.

        Returns:
            A list of GeocodeResult in the same order as the input.
        """

        # Build deterministic ordering and mapping by input ID.
        input_list = list(addresses)
        results_by_id: Dict[int, GeocodeResult] = {}

        # Initialize the Geocoder with API key for authentication.
        portal = GIS(api_key=self._config.api_key)
        geocoder = Geocoder(self._config.geocode_url, gis=portal)

        # Batch requests to avoid overly large payloads.
        for batch_start in range(0, len(input_list), batch_size):
            batch = input_list[batch_start : batch_start + batch_size]

            try:
                # Convert addresses to dict
                def to_address_dict(addr: AddressInput) -> Dict:
                    addr_dict = asdict(addr)
                    addr_dict["OBJECTID"] = addr_dict["id"]  # Add OBJECTID for tracking
                    return addr_dict
                
                addresses_dict = [to_address_dict(addr) for addr in batch]
                
                # Batch geocode expects a list of dicts with address components
                geocode_response = batch_geocode(
                    addresses=addresses_dict,
                    geocoder=geocoder
                )
            except Exception as ex:  # pragma: no cover
                # Treat as a fatal error for the whole batch.
                for addr in batch:
                    results_by_id[addr.id] = GeocodeResult(
                        id=addr.id,
                        input_address=addr.address,
                        matched_address=None,
                        latitude=None,
                        longitude=None,
                        score=None,
                        match_type=None,
                        match_status="U",
                    )
                continue

            batch_results = self._parse_response(geocode_response, batch)
            results_by_id.update({result.id: result for result in batch_results})

        # Ensure results list matches the input order.
        return [results_by_id.get(addr.id) for addr in input_list]

    def _parse_response(self, response: List[Dict], batch: List[AddressInput]) -> List[GeocodeResult]:
        """Parse the geocode addresses response into GeocodeResult list."""

        # Build a mapping from OBJECTID to AddressInput.
        # We used sequential OBJECTIDs per batch.
        inputs_by_oid: Dict[int, AddressInput] = {addr.id: addr for addr in batch}

        results: List[GeocodeResult] = []
        entries = [GeocodeResponse(**loc) for loc in response] or []

        # Track which inputs were matched.
        matched_oids = set()

        # For each geocoding result, map back to the input and create a GeocodeResult.
        # For details on output fields, see:
        # https://developers.arcgis.com/rest/geocode/service-output/#output-fields
        for entry in entries:
            attributes = entry.attributes
            oid = attributes.get("ResultID")
            if oid is None or oid not in inputs_by_oid:
                continue

            input_item = inputs_by_oid[oid]
            matched_oids.add(oid)

            score = entry.score
            match_status = attributes.get("Status")

            # Coordinates may be inside `location` dict.
            location = entry.location
            latitude = location.get("y")
            longitude = location.get("x")

            result = GeocodeResult(
                id=input_item.id,
                input_address=input_item.address,
                matched_address=attributes.get("Match_addr") or None,
                latitude=float(latitude) if latitude is not None else None,
                longitude=float(longitude) if longitude is not None else None,
                score=float(score) if score is not None else None,
                match_type=attributes.get("Addr_type"),
                match_status=match_status
            )
            results.append(result)

        # For any inputs not returned, create a NoMatch result.
        for oid, input_item in inputs_by_oid.items():
            if oid in matched_oids:
                continue
            results.append(
                GeocodeResult(
                    id=input_item.id,
                    input_address=input_item.address,
                    matched_address=None,
                    latitude=None,
                    longitude=None,
                    score=None,
                    match_type=None,
                    match_status="U",
                )
            )

        return results
