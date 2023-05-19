from mathematical_objects import Fraction
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
        self.assertEqual(Fraction(1, 2).__str__(), '1/2')
        self.assertEqual(Fraction(10, 20).__str__(), '1/2')
        self.assertEqual(Fraction(25, 15).__str__(), '5/3')
        self.assertEqual(Fraction(20, 10).__str__(), '2')
        self.assertEqual(Fraction(-1, 2).__str__(), '-1/2')
        self.assertEqual(Fraction(1, -2).__str__(), '-1/2')
        self.assertEqual(Fraction(-1, -2).__str__(), '1/2')
        self.assertEqual(Fraction(0, -2).__str__(), '0')
        self.assertEqual(Fraction(10).__str__(), '10')

    def test_eq(self):
        self.assertTrue(Fraction.__eq__(Fraction(1, 2), Fraction(1, 2)))
        self.assertTrue(Fraction.__eq__(Fraction(-1, -2), Fraction(1,
                        2)))
        self.assertTrue(Fraction.__eq__(Fraction(0, -2), Fraction(0,
                        70)))

    def test_add(self):
        self.assertTrue(Fraction.__eq__(Fraction.__add__(Fraction(2,
                        7), Fraction(3, 8)), Fraction(37, 56)))