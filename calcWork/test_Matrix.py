from unittest import TestCase
from Matrix import Matrix


class TestMatrix(TestCase):
    def setUp(self):
        self.m1 = Matrix([[1, 2], [3, 4]])
        self.m2 = Matrix([[1.0444442,3.004],[-5.45,-6325666]])

    def test_init(self):
        self.assertEqual(self.m1.params, [[1, 2], [3, 4]])

    def test_repr(self):
        #self.assertEqual(repr(self.m1), "[1  2 ]\n[3  4 ]")
        print(self.m2.__repr__())
