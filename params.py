from argparse import ArgumentParser

from exceptions import ParamsError
import config

def parse_location() -> str:
    parser = _create_parser()
    namespace, _ = parser.parse_known_args()
    if namespace.location is None and config.DEFAULT_LOCATION is None:
        raise ParamsError
    return namespace.location if namespace.location else config.DEFAULT_LOCATION # type: ignore

def _create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('location', nargs='?')
    return parser
