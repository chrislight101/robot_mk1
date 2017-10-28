from cv2 import VideoCapture
from cv2 import destroyAllWindows


class Camera:

    DEFAULT_CAPTURE = 0
    SECONDARY_CAPTURE = 1

    def __init__(self):
        self.cap = VideoCapture(self.DEFAULT_CAPTURE)
        self.cap = VideoCapture()

    def open_capture(self):
        self.cap.open(0)

    def close_capture(self):
        self.cap.release()
        destroyAllWindows()

    def is_cap_opened(self):
        return self.cap.isOpened()

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame
