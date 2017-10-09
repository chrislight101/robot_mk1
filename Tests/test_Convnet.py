import unittest
from Core.Learning.Convnet import Convnet


class ConvnetTest(unittest.TestCase):

    def setUp(self):
        self.convnet = Convnet()

    def tearDown(self):
        pass

    def test_ConvnetDetectsGreenTarget(self):
        # load image
        pass


if __name__ == '__main__':
    unittest.main()
