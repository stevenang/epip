import sys
import unittest
from src import parity

class ParityUnitTest(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(parity.parity_01(0), 0)

    def test_case_02(self):
        self.assertEqual(parity.parity_01(10), 0)

    def test_case_03(self):
        self.assertEqual(parity.parity_01(sys.maxsize), 1)


if __name__ == '__main__':
    unittest.main()
