"""A Python utility for downloading Sentinel-1 Orbit files from the Registry of Open Data on AWS."""

from importlib.metadata import version

from .exceptions import InvalidSceneError, OrbitNotFoundError
from .s1_orbits import API_URL, fetch_for_scene


__version__ = version(__name__)

__all__ = [
    '__version__',
    'fetch_for_scene',
    'API_URL',
    'InvalidSceneError',
    'OrbitNotFoundError',
]
