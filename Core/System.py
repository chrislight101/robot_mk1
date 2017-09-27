

class System:

    STATE_STOPPED = "stopped"
    STATE_MOVING = "moving"

    class Pose:
        def __init__(self):
            self._x = 0.0
            self._y = 0.0
            self._phi = 0.0

        def get_pose(self):
            return self._x, self._y, self._phi

        def set_pose(self, x, y, phi):
            self._x = x
            self._y = y
            self._phi = phi

    def __init__(self):
        self.pose = self.Pose()
        self.state = self.STATE_STOPPED
        pass

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def start(self):
        pass
