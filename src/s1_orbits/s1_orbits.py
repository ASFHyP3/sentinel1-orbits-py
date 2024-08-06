import logging
from pathlib import Path
from typing import Union

import requests

from .exceptions import InvalidSceneError, OrbitNotFoundError


API_URL = "https://s1-orbits.asf.alaska.edu/scene"


def fetch_for_scene(
    scene: str,
    dir: Union[Path, str] = ".",
) -> Path:
    """For the given scene, this downloads the AUX_POEORB file, if available, otherwise it downloads the AUX_RESORB.

    Args:
        scene: The scene name for which to download the orbit file.
        dir: The directory that the orbit file should download into.

    Returns:
        download_path: The path to the downloaded file.
    """
    request_url = f"{API_URL}/{scene}"

    logging.info(f"Downloading {request_url}")

    res = requests.get(request_url)
    if res.status_code == 400:
        raise InvalidSceneError(scene)
    if res.status_code == 404:
        raise OrbitNotFoundError(scene)
    res.raise_for_status()

    filename = res.url.split("/")[-1]
    download_path = Path(dir) / filename
    download_path.write_text(res.text)

    return download_path
