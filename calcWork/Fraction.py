class Fraction:
    num: int
    denom: int

    @staticmethod
    def gcd(n1: int, n2: int):
        return n2 if n1 == 0 else Fraction.gcd(n2 % n1, n1)

    def __init__(self, num: int, denom: int = 1):
        sign = -1 if (num <= 0 and denom > 0) or (num >= 0 and denom < 0) else 1
        num = int(abs(num))
        denom = int(abs(denom))
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = Fraction.gcd(num, denom)
        self.num = int(sign * (num // gcd))
        self.denom = int(denom // gcd)

    def __str__(self):
        return (
            f"{self.num}/{self.denom}"
            if (self.denom != 1 and self.num != 0)
            else str(self.num)
        )

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, int):
            return self + Fraction(other, 1)
        return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

    def __sub__(self, other) -> 'Fraction':
        if isinstance(other, int):
            return self - Fraction(other, 1)
        return Fraction(self.num * other.denom - self.denom * other.num, self.denom * other.denom)

    def __mul__(self, other) -> 'Fraction':
        if isinstance(other, int):
            return self * Fraction(other, 1)
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __truediv__(self, other) -> 'Fraction':
        if isinstance(other, int):
            return self / Fraction(other, 1)
        return Fraction(self.num * other.denom, self.denom * other.num)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self.num == other.num and self.denom == other.denom
        return False

