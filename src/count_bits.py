import random
import unittest

# This code test
def count_bits(data: int):
    num_of_bits = 0
    while data:
        num_of_bits += data & 1
        data >>= 1
    return num_of_bits

class CountBitsUnitTest(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(count_bits(0), 0)

    def test_case_02(self):
        self.assertEqual(count_bits(1234567890), 12)

    def test_case_03(self):
        self.assertEqual(count_bits(9876543210), 15)


if __name__ == '__main__':
    unittest.main()

