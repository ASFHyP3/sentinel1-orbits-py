from importlib.metadata import version

from .s1_orbits import *

__version__ = version(__name__)

__all__ = [
    '__version__',
]