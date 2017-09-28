try:
    import RPi.GPIO as GPIO
except (RuntimeError, ImportError):
    pass

from Core.Vision.TargetDetector import TargetDetector
import yaml
import os


class System:
    # A class to perform a robotic task according to a profile

    STATE_STOPPED = "stopped"
    STATE_MOVING = "moving"

    STATE_INIT = "init"
    STATE_SEARCH = "search"

    CUR_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_FILE = CUR_DIR + "/static/config.yaml"

    class Pose:
        # A class to hold position and orientation of robot

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
        self.target_found = None

        fpt = open(self.CONFIG_FILE, 'r')
        self.config = yaml.load(fpt)
        fpt.close()
        self.target_detector = TargetDetector()

    def run(self):
        self.pose.reset_pose()
        self.target_found = self.target_detector.scan_for_potential_targets()

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_move_state(self):
        return self.move_state

    def set_move_state(self, state):
        self.move_state = state
