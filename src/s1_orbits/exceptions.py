class InvalidSceneError(Exception):
    def __init__(self, scene: str = ""):
        if scene:
            self.scene = scene
            self.message = f"{self.scene} is an invalid scene name."
        else:
            self.message = "The provided scene name is invalid."

    def __str__(self):
        return str(self.message)


class OrbitNotFoundError(Exception):
    def __init__(self, scene: str = ""):
        if scene:
            self.scene = scene
            self.message = (
                f"No orbit file could be found for the provided scene: {self.scene}"
            )
        else:
            self.message = "No orbit file could be found for the provided scene."

    def __str__(self):
        return str(self.message)
