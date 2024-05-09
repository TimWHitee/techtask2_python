import unittest
from main import *

class Test(unittest.TestCase):

    def test_min(self):
        self.assertEqual(min_([1,2,3,4,5]), 1)

    def test_max(self):
        self.assertEqual(max_([1,2,3,4,5]), 5)

    def test_sum(self):
        self.assertEqual(sum_([1,2,3,4,5]), 15)

    def test_mult(self):
        self.assertEqual(mult_([1,2,3,4,5]), 2*3*4*5)

unittest.main()
