import unittest
from src import count_bits
class CountBitsUnitTest(unittest.TestCase):

    def test_case_01(self):
        self.assetyEqual(count_bits(0), 0)


if __name__ == '__main__':
    unittest.main()