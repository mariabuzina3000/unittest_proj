import unittest
from utils.arrs import get
from utils.arrs import my_slice


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], -1, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([], 1), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -5, 3), [1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4], -3, 3), [2, 3])


