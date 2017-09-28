from Core.Camera import Camera
import cv2
import numpy as np


class TargetDetector:

    DEFAULT_LOWER_HSV_BOUNDS =  [0, 0, 0]
    DEFAULT_UPPER_HSV_BOUNDS = [179, 255, 255]

    GREEN_LOWER_HSV_BOUNDS =  [45, 0, 0]
    GREEN_UPPER_HSV_BOUNDS = [65, 255, 255]

    def __init__(self):
        self.camera = Camera()
        self.hsv_low_bounds = np.array(self.DEFAULT_LOWER_HSV_BOUNDS)
        self.hsv_high_bounds = np.array(self.DEFAULT_UPPER_HSV_BOUNDS)
        pass

    def set_bounds(self, lower_bounds, upper_bounds):
        self.hsv_low_bounds = np.array(lower_bounds)
        self.hsv_high_bounds = np.array(upper_bounds)

    def get_hsv_low_bounds(self):
        return self.hsv_low_bounds

    def get_hsv_high_bounds(self):
        return self.hsv_high_bounds

    def capture_and_color_filter(self):
        raw_bgr_frame = self.camera.get_frame()
        hsv_frame = cv2.cvtColor(raw_bgr_frame, cv2.COLOR_BGR2HSV)
        filtered = cv2.inRange(hsv_frame, self.hsv_low_bounds, self.hsv_high_bounds)
        return filtered

    def get_avg_green(self):
        self.set_bounds(self.GREEN_LOWER_HSV_BOUNDS, self.GREEN_UPPER_HSV_BOUNDS)
        color_filtered_frame = self.capture_and_color_filter()
        return np.mean(color_filtered_frame)
