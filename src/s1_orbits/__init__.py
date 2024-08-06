from importlib.metadata import version

from .s1_orbits import fetch_for_scene, API_URL

__version__ = version(__name__)

__all__ = ["__version__", "fetch_for_scene", "API_URL"]
