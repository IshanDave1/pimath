from unittest import TestCase
from Matrix import Matrix


class TestMatrix(TestCase):
    def setUp(self):
        self.m1 = Matrix([[1, 2], [3, 4]])
        self.m2 = Matrix([[-2, 5], [4, -1]])
        self.m3 = Matrix([[1, 3, 2], [5, 2, 6], [2, 7, 3]])
        self.m4 = Matrix([[1.0444442, 3.004, 5.256], [-5.45, -6325666, -3878], [36545.45, -63.25666, -3.878]])
        self.m5 = Matrix([[2, 1, 3], [0, -1, 2]])

    def test_init(self):
        self.assertEqual(self.m1.params, [[1, 2], [3, 4]])

    def test_repr(self):
        self.assertEqual(repr(self.m1), "[1|2]\n[3|4]")
        self.assertEqual(repr(self.m4),
                         "[1.0444442|3.004    |5.256    ]\n[-5.45    |-6325666 |-3878    ]\n[36545.45 |-63.25666|-3.878   ]")

    def test_eq(self):
        self.assertNotEqual(self.m1, self.m3)
        self.assertEqual(self.m1, Matrix([[1.0001, 2.0001], [3.0002, 4.001]]))

    def test_add(self):
        self.assertEqual(self.m1 + self.m2, Matrix([[-1, 7], [7, 3]]))

    def test_sub(self):
        self.assertEqual(self.m1 - self.m2, Matrix([[3, -3], [-1, 5]]))

    def test_zeroes(self):
        zero_matrix = Matrix.zeros(3, 2)
        expected_result = Matrix([[0, 0], [0, 0], [0, 0]])
        self.assertEqual(zero_matrix, expected_result)

    def test_mul_scalar(self):
        scalar = 2
        expected_result = Matrix([[2, 4], [6, 8]])
        self.assertEqual(self.m1 * scalar, expected_result)

    def test_mul_matrix(self):
        expected_result = Matrix([[2, 1, 3], [6, 1, 9]])
        self.assertEqual(self.m1 * self.m5, expected_result)
        self.assertRaises(ValueError, lambda: self.m1 * self.m3)  # Matrices with incompatible dimensions

    def test_div_scalar(self):
        scalar = 2
        expected_result = Matrix([[0.5, 1], [1.5, 2]])
        self.assertEqual(self.m1 / scalar, expected_result)

    def test_zero_matrix(self):
        zero_matrix = Matrix([[0, 0], [0, 0]])
        self.assertTrue(zero_matrix.is_zero())
        self.assertFalse(self.m1.is_zero())

    def test_ones(self):
        ones_matrix = Matrix.ones(2, 2)
        expected_result = Matrix([[1, 1], [1, 1]])
        self.assertEqual(ones_matrix, expected_result)
