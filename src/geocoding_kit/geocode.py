from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from arcgis.gis import GIS
from arcgis.geocoding import Geocoder, batch_geocode

from .config import ArcGISConfig
from .models import AddressInput, GeocodeResult


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
        inputs_by_id: Dict[str, AddressInput] = {addr.id: addr for addr in input_list}
        results_by_id: Dict[str, GeocodeResult] = {}

        # Initialize the Geocoder with API key for authentication.
        portal = GIS(api_key=self._config.api_key)
        geocoder = Geocoder(self._config.geocode_url, gis=portal)

        # Batch requests to avoid overly large payloads.
        for batch_start in range(0, len(input_list), batch_size):
            batch = input_list[batch_start : batch_start + batch_size]

            try:
                response = batch_geocode(
                    addresses,
                    geocoder=geocoder
                )
            except Exception as ex:  # pragma: no cover
                # Treat as a fatal error for the whole batch.
                for item in batch:
                    results_by_id[item.id] = GeocodeResult(
                        id=item.id,
                        input_address=item.address,
                        matched_address=None,
                        latitude=None,
                        longitude=None,
                        score=None,
                        match_type=None,
                        match_status="Error",
                        error=str(ex),
                    )
                continue

            batch_results = self._parse_response(response, batch)
            results_by_id.update({r.id: r for r in batch_results})

        # Ensure results list matches the input order.
        return [results_by_id.get(addr.id) for addr in input_list]

    def _parse_response(self, response: dict, batch: List[AddressInput]) -> List[GeocodeResult]:
        """Parse ArcGIS geocodeAddresses response into GeocodeResult list."""

        # Build a mapping from OBJECTID to AddressInput.
        # We used sequential OBJECTIDs per batch.
        inputs_by_oid: Dict[int, AddressInput] = {
            idx: item for idx, item in enumerate(batch)
        }

        results: List[GeocodeResult] = []
        locations = response.get("locations") or []

        # Track which inputs were matched.
        matched_oids = set()

        for loc in locations:
            attributes = loc.get("attributes", {})
            oid = attributes.get("OBJECTID")
            if oid is None or oid not in inputs_by_oid:
                continue

            input_item = inputs_by_oid[oid]
            matched_oids.add(oid)

            score = attributes.get("Score")
            match_status = "Matched" if score and score > 0 else "NoMatch"

            # Coordinates may be inside `location` dict.
            location = loc.get("location") or {}
            latitude = location.get("y")
            longitude = location.get("x")

            result = GeocodeResult(
                id=input_item.id,
                input_address=input_item.address,
                matched_address=attributes.get("Match_addr") or None,
                latitude=float(latitude) if latitude is not None else None,
                longitude=float(longitude) if longitude is not None else None,
                score=float(score) if score is not None else None,
                match_type=attributes.get("FeatureType"),
                match_status=match_status,
                error=None if match_status == "Matched" else "No match found",
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
                    match_status="NoMatch",
                    error="No match found",
                )
            )

        # Preserve original input order in output.
        results.sort(key=lambda r: int(r.id) if str(r.id).isdigit() else 0)
        return results
