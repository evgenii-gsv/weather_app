import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False
USE_ROUNDED_COORDS = False
NOMINATIM_USER_AGENT = os.getenv('NOMINATIM_USER_AGENT')
OPENWEATHER_API = os.getenv('OPENWEATHER_API')
DEFAULT_LOCATION = os.getenv('DEFAULT_LOCATION')
OPENWEATHER_URL = (
    'https://api.openweathermap.org/data/2.5/weather?'
    'lat={latitude}&lon={longitude}&'
    'appid=' + OPENWEATHER_API + '&lang=ru&' # type: ignore
    'units=metric'
)