import logging
from pathlib import Path
from typing import Union

import requests


API_URL = "https://s1-orbits.asf.alaska.edu/scene"


def fetch_for_scene(
    scene: str,
    dir: Union[Path, str] = ".",
) -> str:
    """Download a file

    Args:
        url: URL of the file to download
        directory: Directory location to place files into
        chunk_size: Size to chunk the download into

    Returns:
        download_path: The path to the downloaded file
    """
    request_url = f"{API_URL}/{scene}"

    logging.info(f"Downloading {request_url}")

    session = requests.Session()

    with session.get(request_url, stream=True) as res:
        if res.status_code == 400:
            raise ValueError("Invalid scene name.")
        res.raise_for_status()
        filename = res.url.split("/")[-1]
        download_path = Path(dir) / filename
        with open(download_path, "wb") as f:
            for chunk in res.iter_content():
                if chunk:
                    f.write(chunk)
    session.close()

    return download_path
