
try:
    import RPi.GPIO as GPIO
except (RuntimeError, ImportError):
    pass

class System:

    STATE_STOPPED = "stopped"
    STATE_MOVING = "moving"

    STATE_INIT = "init"
    STATE_SEARCH = "search"

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

        def reset_pose(self):
            self._x = 0.0
            self._y = 0.0
            self._phi = 0.0

    def __init__(self):
        self.pose = self.Pose()
        self.move_state = self.STATE_STOPPED
        self.state = self.STATE_INIT
        self.action_timer = 0.0
        self.target_acquired = False
        pass

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_move_state(self):
        return self.move_state

    def set_move_state(self, state):
        self.move_state = state

    def run(self):
        # set pose to zero
        if self.get_state() == self.STATE_INIT:
            self.pose.reset_pose()
            self.target_acquired = False
            self.set_state(self.STATE_SEARCH)

        if self.get_state() == self.STATE_SEARCH:
            self.get_scene()
        # is target in view
        # find target
        # set new pose
        # move to target


        pass
