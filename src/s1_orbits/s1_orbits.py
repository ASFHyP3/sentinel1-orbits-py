"""A Python utility for downloading Sentinel-1 Orbit files from the Registry of Open Data on AWS."""

from pathlib import Path

import requests

from .exceptions import InvalidSceneError, OrbitNotFoundError


API_URL = 'https://s1-orbits.asf.alaska.edu/scene'


def fetch_for_scene(
    scene: str,
    dir: Path | str = '.',
) -> Path:
    """For the given scene, downloads the AUX_POEORB file if available, otherwise downloads the AUX_RESORB file.

    Args:
        scene: The scene name for which to download the orbit file.
        dir: The directory that the orbit file should download into.

    Raises:
        InvalidSceneError: Thrown if the scene name is not a proper Sentinel-1 scene name.
        OrbitNotFoundError: Thrown if an orbit cannot be found for the provided scene.

    Returns:
        download_path: The path to the downloaded file.
    """
    request_url = f'{API_URL}/{scene}'

    res = requests.get(request_url)
    if res.status_code == 400:
        raise InvalidSceneError(scene)
    if res.status_code == 404:
        raise OrbitNotFoundError(scene)
    res.raise_for_status()

    filename = res.url.split('/')[-1]
    download_path = Path(dir) / filename
    download_path.write_text(res.text)

    return download_path
