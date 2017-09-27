import unittest

from Core.System import System


class SystemTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.system = System()

    def tearDown(self):
        pass

    def test_StateIsStartAtInit(self):
        self.assertTrue(self.system.get_current_state(), System.STATE_START)


if __name__ == '__main__':
    unittest.main()
