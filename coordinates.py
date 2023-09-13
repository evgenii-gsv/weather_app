from typing import NamedTuple
from geopy.geocoders import Nominatim
from geopy.location import Location
from pprint import pprint

import config
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float
    location: str


def get_coordinates(query: str) -> Coordinates:
    """Returns coordinates of the location in query"""
    coordinates = _parse_coordinates(_get_location(query))
    return _round_coordinates(coordinates)

def _get_geolocator() -> Nominatim:
    return Nominatim(user_agent=config.NOMINATIM_USER_AGENT)

def _get_location(query: str) -> Location:
    geolocator = _get_geolocator()
    location = geolocator.geocode(query, language='ru') # type: ignore
    if not location:
        raise CantGetCoordinates('The location name is not valid')
    if config.DEBUG:
        pprint(location.raw) # type: ignore
        print()
    return location # type: ignore

def _parse_coordinates(location: Location) -> Coordinates:
    return Coordinates(
        latitude=location.latitude,
        longitude=location.longitude,
        location=location.address
    )

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ), location=coordinates.location)