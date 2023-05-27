from Fraction import Fraction
from unittest import TestCase


class TestFraction(TestCase):

    def test_gcd(self):
        self.assertEqual(Fraction.gcd(50, 10), 10)
        self.assertEqual(Fraction.gcd(29, 30), 1)
        with self.assertRaises(TypeError):
            Fraction.gcd('a', 'b')

    def test_init(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_str(self):
        self.assertEqual(str(Fraction(1, 2)), '1/2')
        self.assertEqual(str(Fraction(10, 20)), '1/2')
        self.assertEqual(str(Fraction(25, 15)), '5/3')
        self.assertEqual(str(Fraction(20, 10)), '2')
        self.assertEqual(str(Fraction(-1, 2)), '-1/2')
        self.assertEqual(str(Fraction(1, -2)), '-1/2')
        self.assertEqual(str(Fraction(-1, -2)), '1/2')
        self.assertEqual(str(Fraction(0, -2)), '0')
        self.assertEqual(str(Fraction(10)), '10')

    def test_eq(self):
        self.assertEqual(Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(Fraction(-1, -2), Fraction(1, 2))
        self.assertEqual(Fraction(4, 2), Fraction(6, 3))
        self.assertEqual(Fraction(4, -2), -2)
        self.assertEqual(Fraction(0, -2), Fraction(0, 70))

    def test_add(self):
        self.assertEqual(Fraction(2, 7) + Fraction(3, 8), Fraction(37, 56))
        self.assertEqual(Fraction(2, 7) + 1, Fraction(9, 7))

    def test_sub(self):
        self.assertEqual(Fraction(2, 7) - Fraction(3, 8), Fraction(-5, 56))
        self.assertEqual(Fraction(5, 4) - Fraction(1, 4), Fraction(1, 1))
        self.assertEqual(Fraction(0, 5) - Fraction(3, 7), Fraction(-3, 7))
        self.assertEqual(Fraction(3, 2) - Fraction(4, 2), Fraction(-1, 2))
        self.assertEqual(Fraction(3, 2) - 1, Fraction(1, 2))

    def test_mul(self):
        self.assertEqual(Fraction(2, 7) * Fraction(3, 8), Fraction(3, 28))
        self.assertEqual(Fraction(5, 4) * Fraction(1, 4), Fraction(5, 16))
        self.assertEqual(Fraction(0, 5) * Fraction(3, 7), Fraction(0, 1))
        self.assertEqual(Fraction(3, 2) * Fraction(4, 2), Fraction(3))
        self.assertEqual(Fraction(3, 2) * 6, 9)

    def test_div(self):
        self.assertEqual(Fraction(2, 7) / Fraction(3, 8), Fraction(16, 21))
        self.assertEqual(Fraction(5, 4) / Fraction(1, 4), Fraction(5, 1))
        self.assertEqual(Fraction(0, 5) / Fraction(3, 7), Fraction(0, 1))
        self.assertEqual(Fraction(3, 2) / Fraction(4, 2), Fraction(3, 4))
        self.assertEqual(Fraction(3, 2) / 2, Fraction(3, 4))
        with self.assertRaises(ValueError):
            Fraction(5, 3) / Fraction(0, 7)
            Fraction(5, 3) / 0
