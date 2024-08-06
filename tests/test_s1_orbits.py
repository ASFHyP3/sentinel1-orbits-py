import responses
import pytest
from pathlib import Path

import s1_orbits


@responses.activate
def test_fetch_for_scene(tmp_path):
    granule = "foo"
    filename = "filename.txt"
    file_contents = "This is some text."
    request_url = f"{s1_orbits.API_URL}/{granule}"
    response_url = f"https://bar.com/{filename}"

    responses.add(
        responses.GET, request_url, status=302, headers={"Location": response_url}
    )
    responses.add(
        responses.GET,
        response_url,
        status=200,
        body=file_contents,
        content_type="text/plain",
    )
    filepath = s1_orbits.fetch_for_scene("foo", tmp_path)
    assert filepath == Path(tmp_path) / filename
    assert filepath.read_text() == file_contents

    responses.add(responses.GET, request_url, status=400)
    with pytest.raises(s1_orbits.InvalidSceneError):
        s1_orbits.fetch_for_scene("foo", tmp_path)

    responses.add(responses.GET, request_url, status=404)
    with pytest.raises(s1_orbits.OrbitNotFoundError):
        s1_orbits.fetch_for_scene("foo", tmp_path)
