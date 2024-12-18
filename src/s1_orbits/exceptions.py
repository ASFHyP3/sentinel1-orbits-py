class InvalidSceneError(Exception):
    def __init__(self, scene: str):
        self.scene = scene
        self.message = f'{scene} is not a valid Sentinel-1 scene name.'

    def __str__(self):
        return str(self.message)


class OrbitNotFoundError(Exception):
    def __init__(self, scene: str):
        self.scene = scene
        self.message = f'No orbit file could be found for the provided Sentinel-1 scene: {scene}'

    def __str__(self):
        return str(self.message)
