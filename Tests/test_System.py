import unittest
from Core.System import System


class SystemTest(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def tearDown(self):
        pass

    def test_SetState(self):
        self.system.set_move_state(System.STATE_STOPPED)
        self.assertTrue(self.system.get_move_state(), System.STATE_STOPPED)

    def test_ResetPoseToZero(self):
        self.system.pose.reset_pose()
        self.assertTrue(self.system.pose.get_pose(), (0.0, 0.0, 0.0))


if __name__ == '__main__':
    unittest.main()
