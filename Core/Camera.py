from cv2 import VideoCapture


class Camera:

    DEFAULT_CAPTURE = 0
    SECONDARY_CAPTURE = 1

    def __init__(self):
        self.cap = VideoCapture(self.DEFAULT_CAPTURE)

    def open_capture(self):
        return self.cap.open(0)

    def is_cap_opened(self):
        return self.cap.isOpened()

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame
