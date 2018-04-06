from cv2 import VideoCapture, destroyAllWindows, imshow, waitKey


class Camera:

    DEFAULT_CAPTURE = 0
    SECONDARY_CAPTURE = 1

    def __init__(self):
        self.cap = VideoCapture(self.DEFAULT_CAPTURE)
        self.cap.open(1)
        self.center_x = int(self.cap.get(3) / 2)
        self.center_y = int(self.cap.get(4) / 2)

    def close_capture(self):
        self.cap.release()
        destroyAllWindows()

    def is_cap_opened(self):
        return self.cap.isOpened()

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame


if __name__ == '__main__':
    camera = Camera()
    while True:
        img = camera.get_frame()
        imshow('img', img)
        key = waitKey(1) & 0xFF
        if key == ord('q'):
            break
    camera.close_capture()
