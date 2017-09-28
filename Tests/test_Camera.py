import unittest
from Core.Camera import Camera


class CameraTest(unittest.TestCase):

    def setUp(self):
        self.camera = Camera()

    def tearDown(self):
        pass

    def test_OpenCapture(self):
        self.assertTrue(self.camera.open_capture())

    def test_GetFrame(self):
        frame = self.camera.get_frame()
        self.assertIsNotNone(frame)


if __name__ == '__main__':
    unittest.main()
