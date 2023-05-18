import unittest
from Function import *


class FunctionTest(unittest.TestCase):
    _one = cf(1)
    _opf = cf(1.5)
    _iden = pf(1)
    _x_sq = pf(2)

    def test_cf(self):
        self.assertEqual(FunctionTest._one(12), 1)
        self.assertEqual(FunctionTest._one.deri_at(56), 0)
        self.assertEqual(FunctionTest._opf.strp, str(1.5))

    def test_pf(self):
        self.assertEqual(FunctionTest._x_sq(2), 4)
        self.assertEqual(FunctionTest._x_sq.deri_at(2), 4)
        self.assertEqual(FunctionTest._x_sq.strp, "x^2")

    def test_sinf(self):
        sin_func = sinf(FunctionTest._iden)
        self.assertAlmostEqual(sin_func(math.pi), 0)
        self.assertAlmostEqual(sin_func.deri_at(math.pi), -1)
        self.assertEqual(sin_func.strp, "sin(x^1)")

    def test_cosf(self):
        func = cf(1)
        cos_func = cosf(func)
        self.assertAlmostEqual(cos_func(0), math.cos(func(0)))
        self.assertAlmostEqual(cos_func.deri_at(0), -math.sin(func(0)) * func.deri_at(0))
        self.assertEqual(cos_func.strp, f"cos({func.strp})")

    def test_add(self):
        f1 = cf(2)
        f2 = pf(3)
        result = f1 + f2
        self.assertEqual(result(1), f1(1) + f2(1))
        self.assertEqual(result.deri_at(1), f1.deri_at(1) + f2.deri_at(1))
        self.assertEqual(result.strp, f"({f1.strp} + {f2.strp})")

    def test_multiply(self):
        f1 = cf(2)
        f2 = pf(3)
        result = f1 * f2
        self.assertEqual(result(1), f1(1) * f2(1))
        self.assertEqual(result.deri_at(1), f1.deri_at(1) * f2(1) + f1(1) * f2.deri_at(1))
        self.assertEqual(result.strp, f"({f1.strp} * {f2.strp})")

    def test_subtract(self):
        f1 = cf(2)
        f2 = pf(3)
        result = f1 - f2
        self.assertEqual(result(1), f1(1) - f2(1))
        self.assertEqual(result.deri_at(1), f1.deri_at(1) - f2.deri_at(1))
        self.assertEqual(result.strp, f"({f1.strp} - {f2.strp})")

    def test_multiply_by_scalar(self):
        f = cf(2)
        scalar = 3
        result = f * scalar
        self.assertEqual(result(1), scalar * f(1))
        self.assertEqual(result.deri_at(1), scalar * f.deri_at(1))
        self.assertEqual(result.strp, f"({f.strp} * {scalar})")

    def test_divide(self):
        f1 = cf(6)
        f2 = pf(2)
        result = f1 / f2
        self.assertAlmostEqual(result(2), f1(2) / f2(2))
        self.assertAlmostEqual(
            result.deri_at(2),
            (f1.deri_at(2) * f2(2) - f1(2) * f2.deri_at(2)) / (f2(2) ** 2),
        )
        self.assertEqual(result.strp, f"({f1.strp} / {f2.strp})")

    def test_composite(self):
        f1 = cf(0.25 * math.pi)
        f2 = pf(2)
        f3 = sinx
        f4 = sinf(f1)
        f5 = f2.composition(f4)
        result = f3.composition(f2)  # sin(x^3)

        self.assertAlmostEqual(result(math.sqrt(math.pi)), 0)
        self.assertAlmostEqual(result.deri_at(math.sqrt(math.pi)), math.cos(math.pi) * 2 * math.sqrt(math.pi))
        self.assertEqual(result.strp, "sin(x^2)")

        self.assertEqual(f5(6.7), f5(8.3))
        self.assertAlmostEqual(f5(3.4), 1 / 2)
        self.assertAlmostEqual(f5.deri_at(7.9), 0)
        self.assertEqual(f5.strp, "sin(0.7853981633974483)^2")


print(__name__)
if __name__ == '__main__':
    unittest.main(verbosity=5, exit=False)
