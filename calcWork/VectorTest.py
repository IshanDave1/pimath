import unittest
from math import sqrt
from Vector import Vector


class VectorTest(unittest.TestCase):
    def setUp(self):
        self.vec1 = Vector(1, 2, 3)
        self.vec2 = Vector(4, 5, 6)
        self.vec3 = Vector(2, 4, 6)
        self.vec4 = Vector(0, 0, 0)

    def test_init(self):
        self.assertEqual(self.vec1.params, (1, 2, 3))
        self.assertEqual(self.vec2.params, (4, 5, 6))

    def test_repr(self):
        self.assertEqual(repr(self.vec1), "Vector(1, 2, 3)")
        self.assertEqual(repr(self.vec2), "Vector(4, 5, 6)")

    def test_add(self):
        result = self.vec1 + self.vec2
        self.assertEqual(result.params, (5, 7, 9))

    def test_sub(self):
        result = self.vec1 - self.vec2
        self.assertEqual(result.params, (-3, -3, -3))

    def test_dot(self):
        result = self.vec1.dot(self.vec2)
        self.assertEqual(result.params, (4, 10, 18))

    def test_mul(self):
        result = self.vec1 * 2
        self.assertEqual(result.params, (2, 4, 6))

    def test_div(self):
        result = self.vec3 / 2
        self.assertEqual(result.params, (1, 2, 3))

    def test_magnitude(self):
        result = self.vec1.magnitude()
        self.assertAlmostEqual(result, sqrt(14), delta=0.001)

    def test_is_zero(self):
        self.assertFalse(self.vec1.is_zero())
        self.assertTrue(self.vec4.is_zero())

    def test_is_parallel(self):
        self.assertTrue(self.vec1.is_parallel(self.vec3))
        self.assertFalse(self.vec1.is_parallel(self.vec2))


if __name__ == '__main__':
    unittest.main()
