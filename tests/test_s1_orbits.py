import tempfile
import responses
import pytest
from pathlib import Path

import s1_orbits


@responses.activate
def test_fetch_for_scene():
    granule = "foo"
    filename = "filename.txt"
    request_url = f"{s1_orbits.API_URL}/{granule}"
    response_url = f"https://bar.com/{filename}"
    directory = tempfile.gettempdir()

    responses.add(
        responses.GET, request_url, status=302, headers={"Location": response_url}
    )
    responses.add(
        responses.GET,
        response_url,
        status=200,
        body="This is some text.",
        content_type="text/plain",
    )
    filepath = s1_orbits.fetch_for_scene("foo", directory)
    assert filepath == Path(directory) / filename

    responses.add(responses.GET, request_url, status=400)
    with pytest.raises(s1_orbits.InvalidSceneError):
        s1_orbits.fetch_for_scene("foo", directory)

    responses.add(responses.GET, request_url, status=404)
    with pytest.raises(s1_orbits.OrbitNotFoundError):
        s1_orbits.fetch_for_scene("foo", directory)
