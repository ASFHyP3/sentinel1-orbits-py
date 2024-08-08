# s1-orbits

A Python utility for downloading Sentinel-1 Orbit files from the Registry of Open Data on AWS.

```python
>>> import s1_orbits

>>> orbit_file = s1_orbits.fetch_for_scene('S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A')
>>> orbit_file
PosixPath('S1A_OPER_AUX_POEORB_OPOD_20230816T080815_V20230726T225942_20230728T005942.EOF')
```

## Installation

In order to easily manage dependencies, we recommend using dedicated project
environments via [Anaconda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
or [Python virtual environments](https://docs.python.org/3/tutorial/venv.html). 

`s1_orbits` can be installed into a conda environment with:

```
conda install -c conda-forge s1_orbits
```

or into a virtual environment with:

```
python -m pip install s1_orbits
```

## Usage

**s1-orbits** provides one function - `fetch_for_scene` - to download the "best available" orbit file for a given scene. This means it will download the *AUX_POEORB* file if it exists; otherwise, it will download the *AUX_RESORB* file. For a more full-featured API, see [sentineleof](https://github.com/scottstanie/sentineleof) or [CDSE's APIs](https://documentation.dataspace.copernicus.eu/APIs.html).

```python
fetch_for_scene(scene: str, dir: Union[pathlib.Path, str] = '.') -> pathlib.Path
    """
    For the given scene, downloads the AUX_POEORB file if available, otherwise downloads the AUX_RESORB file.

    Args:
        scene: The scene name for which to download the orbit file.
        dir: The directory that the orbit file should download into.

    Raises:
        InvalidSceneError: Thrown if the scene name is not a proper Sentinel-1 scene name.
        OrbitNotFoundError: Thrown if an orbit cannot be found for the provided scene.

    Returns:
        download_path: The path to the downloaded file.
    """
```


## Development

1. Install [git](https://git-scm.com/) and [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
1. Clone the repository.
   ```
   git clone git@github.com:ASFHyP3/sentinel1-orbits-py.git
   cd sentinel1-orbits-py
   ```
1. Create and activate the conda environment.
   ```
   conda env create -f environment.yml
   conda activate s1-orbits
   ```
1. Run the tests.
   ```
   pytest tests
   ```
