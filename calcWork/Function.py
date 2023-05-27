import math


class Function:
    def __init__(self, val_at, deri_at, strp):
        self.val_at = val_at
        self.deri_at = deri_at
        self.strp = strp

    def __call__(self, x):
        return self.val_at(x)

    def __add__(self, other):
        if isinstance(other, Function):
            val_at = lambda x: self(x) + other(x)
            deri_at = lambda x: self.deri_at(x) + other.deri_at(x)
            strp = f"({self.strp} + {other.strp})"
            return Function(val_at, deri_at, strp)
        elif isinstance(other, (int, float)):
            val_at = lambda x: self(x) + other
            deri_at = self.deri_at
            strp = f"({self.strp} + {other})"
            return Function(val_at, deri_at, strp)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Function):
            val_at = lambda x: self(x) * other(x)
            deri_at = lambda x: self.deri_at(x) * other(x) + self(x) * other.deri_at(x)
            strp = f"({self.strp} * {other.strp})"
            return Function(val_at, deri_at, strp)
        elif isinstance(other, (int, float)):
            val_at = lambda x: self(x) * other
            deri_at = lambda x: self.deri_at(x) * other
            strp = f"({self.strp} * {other})"
            return Function(val_at, deri_at, strp)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Function):
            val_at = lambda x: self(x) - other(x)
            deri_at = lambda x: self.deri_at(x) - other.deri_at(x)
            strp = f"({self.strp} - {other.strp})"
            return Function(val_at, deri_at, strp)
        elif isinstance(other, (int, float)):
            val_at = lambda x: self(x) - other
            deri_at = self.deri_at
            strp = f"({self.strp} - {other})"
            return Function(val_at, deri_at, strp)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Function):
            val_at = lambda x: self(x) / other(x)
            deri_at = lambda x: (self.deri_at(x) * other(x) - self(x) * other.deri_at(x)) / (
                other(x) ** 2)
            strp = f"({self.strp} / {other.strp})"
            return Function(val_at, deri_at, strp)
        elif isinstance(other, (int, float)):
            val_at = lambda x: self(x) / other
            deri_at = lambda x: self.deri_at(x) / other
            strp = f"({self.strp} / {other})"
            return Function(val_at, deri_at, strp)
        return NotImplemented

    def __repr__(self):
        return self.strp

    def __str__(self):
        return self.strp

    def composition(self, other):
        val_at = lambda x: self(other(x))
        deri_at = lambda x: self.deri_at(other(x)) * other.deri_at(x)
        strp = f"{self.strp.replace('x', other.strp)}"
        return Function(val_at, deri_at, strp)


def cf(const):
    return Function(lambda x: const, lambda x: 0, str(const))


def pf(power):
    return Function(lambda x: x ** power, lambda x: power * (x ** (power - 1)), f"x^{power}")


def sinf(func):
    return Function(lambda x: math.sin(func(x)), lambda x: math.cos(func(x)) * func.deri_at(x),
                    f"sin({func.strp})")


def cosf(func):
    return Function(lambda x: math.cos(func(x)), lambda x: -math.sin(func(x)) * func.deri_at(x),
                    f"cos({func.strp})")


sinx = Function(lambda x: math.sin(x), lambda x: math.cos(x), "sin(x)")
cosx = Function(lambda x: math.cos(x), lambda x: -1 * math.sin(x), "cos(x)")
