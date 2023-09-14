from datetime import datetime
from typing import NamedTuple, Literal, TypeAlias
from enum import Enum
import ssl
import requests
from requests.exceptions import InvalidURL, JSONDecodeError
from pprint import pprint

import config
from exceptions import ApiServiceError, InvalidAPIKey
from coordinates import Coordinates


Celsius: TypeAlias = int


class WeatherType(Enum):
    THUNDERSTORM = 'Гроза'
    DRIZZLE = 'Изморозь'
    RAIN = 'Дождь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'
    FOG = 'Туман'
    CLOUDS = 'Облачно' 


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    location: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeather API and returns it"""
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, 
        latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(
        openweather_response,
        location=coordinates.location
        )
    return weather

def _get_openweather_response(latitude: float, longitude: float) -> requests.Response:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL.format(
        latitude=latitude,
        longitude=longitude
    )
    try:
        return requests.get(url)
    except InvalidURL:
        raise ApiServiceError
    
def _parse_openweather_response(openweather_response: requests.Response, location: str) -> Weather:
    try:
        openweather_dict = openweather_response.json()
        if config.DEBUG:
            pprint(openweather_dict)
            print()
    except JSONDecodeError:
        raise ApiServiceError
    if openweather_dict['cod'] == 401:
        raise InvalidAPIKey
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
        sunset=_parse_sun_time(openweather_dict, 'sunset'),
        location=location
    )

def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict['main']['temp'])

def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict['weather'][0]['id'])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        '1': WeatherType.THUNDERSTORM,
        '3': WeatherType.DRIZZLE,
        '5': WeatherType.RAIN,
        '6': WeatherType.SNOW,
        '7': WeatherType.FOG,
        '800': WeatherType.CLEAR,
        '80': WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError

def  _parse_sun_time(
        openweather_dict: dict,
        time: Literal['sunrise'] | Literal['sunset']
) -> datetime:
    return datetime.fromtimestamp(openweather_dict['sys'][time])

def _parse_location(
        openweather_dict: dict,
) -> str:
    return openweather_dict['name']
