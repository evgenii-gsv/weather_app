class ParamsError(Exception):
    """Error with parameters"""


class CantGetCoordinates(Exception):
    """Program can't get the coordinates"""


class ApiServiceError(Exception):
    """API service is not available"""


class InvalidAPIKey(Exception):
    """The provided API key is not valid"""