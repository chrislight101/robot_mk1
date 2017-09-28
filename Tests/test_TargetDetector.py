import unittest
from Core.TargetDetector import TargetDetector
import numpy as np


class TargetDetectorTest(unittest.TestCase):

    def setUp(self):
        self.target_detector = TargetDetector()

    def tearDown(self):
        pass

    def test_SetBounds(self):
        low_bounds = np.array([0, 0, 0])
        high_bounds = np.array([255, 255, 255])

        self.target_detector.set_bounds(low_bounds, high_bounds)
        self.assertEqual(self.target_detector.get_hsv_low_bounds().all(), low_bounds.all())
        self.assertEqual(self.target_detector.get_hsv_high_bounds().all(), high_bounds.all())

    def test_GetAvgGreen(self):
        self.target_detector.get_avg_green()
        pass

if __name__ == '__main__':
    unittest.main()
