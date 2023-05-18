class Fraction:
    num : int
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
        return "{}/{}".format(self.num, self.denom) if (self.denom != 1 and self.num != 0) else str(self.num)

    def __add__(self, other: 'Fraction'):
        return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

    def __eq__(self, other: 'Fraction'):
        return self.num == other.num and self.denom == other.denom

    def sub(self, other):
        pass

    def multiply(self, other):
        pass
