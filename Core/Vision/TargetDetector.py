import cv2
import numpy as np
from Core.Vision.Camera import Camera


class TargetDetector:
    # A class to locate environment features with vision sensor

    DEFAULT_LOWER_HSV_BOUNDS = np.array([0, 0, 0])
    DEFAULT_UPPER_HSV_BOUNDS = np.array([179, 255, 255])

    GREEN_LOWER_HSV_BOUNDS = np.array([35, 50, 50])
    GREEN_UPPER_HSV_BOUNDS = np.array([75, 255, 255])

    def __init__(self, camera=Camera()):
        self.camera = camera
        self.hsv_low_bounds = self.DEFAULT_LOWER_HSV_BOUNDS
        self.hsv_high_bounds = self.DEFAULT_UPPER_HSV_BOUNDS
        self.target_found = False

        self.camera.open_capture()

    def scan_for_potential_targets(self):
        self.target_found = False
        while not self.target_found:
            avg_green_in_frame = self.get_avg_green()
            if avg_green_in_frame > 25:
                self.target_found = True
                return self.target_found

        return self.target_found

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

    def display(self):
        self.set_bounds(self.GREEN_LOWER_HSV_BOUNDS, self.GREEN_UPPER_HSV_BOUNDS)
        while True:
            img = self.capture_and_color_filter()
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    target_detector = TargetDetector()
    target_detector.display()
