# sentinel1-orbits-py

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

```python
>>> import s1_orbits
>>> orbit_file = s1_orbits.fetch_for_scene(
...     scene='S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A',
...     dir='/data',
... )
>>> orbit_file
PosixPath('/data/S1A_OPER_AUX_POEORB_OPOD_20230816T080815_V20230726T225942_20230728T005942.EOF')
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
