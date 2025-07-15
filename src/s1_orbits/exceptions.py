"""Custom exception types."""


class InvalidSceneError(Exception):
    """Error for invalid scene."""

    def __init__(self, scene: str) -> None:  # noqa: D107
        self.scene = scene
        self.message = f'{scene} is not a valid Sentinel-1 scene name.'

    def __str__(self) -> str:  # noqa: D105
        return str(self.message)


class OrbitNotFoundError(Exception):
    """Error for orbit not found."""

    def __init__(self, scene: str) -> None:  # noqa: D107
        self.scene = scene
        self.message = f'No orbit file could be found for the provided Sentinel-1 scene: {scene}'

    def __str__(self) -> str:  # noqa: D105
        return str(self.message)
