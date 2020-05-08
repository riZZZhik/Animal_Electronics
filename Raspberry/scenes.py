import time


class Scenes:  # TODO: Scenes code
    """Class to represent the scenes"""

    def __init__(self):
        # Scene ID variable
        self.scene_id = 0

        # Init variable for checking if scene is running
        self.scene_running = False

        # Init bool variable to set is ARuco position needed
        self.scene_aruco = True

        # Init time variables
        self._start_time = time.time()
        self._scene_time = 0
        self._scene_end_time = 0

        # Init scenes dictionaries
        self._scenes_dict = {
            1: self.give_five,
            2: self.sing,
            3: self.sit
        }

        self._scenes_config = {
            1: {"time": 0, "ARuco": True},
            2: {"time": 0, "ARuco": True},
            3: {"time": 0, "ARuco": False}
        }  # In seconds

    def scene(self, scene_id=0):
        if self.scene_running:
            # Call scene
            self._scenes_dict[self.scene_id]()

            # Check scene time finished
            if time.time() - self._scene_end_time > 0:
                self.scene_running = False
                self.scene_aruco = True
                self.scene_id = 0

        elif scene_id:  # Turn on scene
            self.scene_id = scene_id
            self.scene_running = True
            self.scene_aruco = self._scenes_config[scene_id]["ARuco"]

            self._scene_time = self._scenes_config[scene_id]["time"]
            self._scene_end_time = time.time() + self._scene_time

    def give_five(self):
        pass

    def sing(self):
        pass

    def sit(self):
        pass
