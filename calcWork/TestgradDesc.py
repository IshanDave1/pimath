from unittest import TestCase

from calcWork.Vector import Vector
from gradDesc import gd_general


class TestgradDesc(TestCase):
    def setUp(self):
        def f(v: Vector) -> float:
            x, y, z = v.params
            return x * x + 4 * y * y + 6 * z * z - 20 * x - 16 * y + 24 * z

        self.f = f

    def test_gd_general(self):
        self.assertEqual(gd_general(self.f, Vector(1, 3, 5), 0.1, 0.001), Vector(10, 2, -2))
