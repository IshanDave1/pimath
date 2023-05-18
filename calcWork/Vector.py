# exec(open('C:/Users/win 10/Desktop/Projects/Python/pimath/calcWork/Vector.py').read())
from math import *

tolerance = 0.001


class Vector:
    def __init__(self, *params):
        self.params = params

    def __repr__(self):
        return f"Vector({str(self.params)[1:-1]})"

    def __add__(self, other):
        return Vector([self.params[i] + other.params[i] for i in range(len(self.params))])

    def __sub__(self, other):
        return Vector([self.params[i] + other.params[i] for i in range(len(self.params))])

    def dot(self, other):
        return Vector([self.params[i] * other.params[i] for i in range(len(self.params))])

    def __mul__(self, scalar):
        return Vector([ai * scalar for ai in self.params])

    def __truediv__(self, scalar):
        return Vector([ai / scalar for ai in self.params])

    def magnitude(self):
        return sqrt(sum(ai ** 2 for ai in self.params))

    def is_zero(self):
        return all(param == 0 for param in self.params)

    def is_parallel(self, other):
        ratio = self.params[0] / other.params[0]
        return all(abs(ratio - self.params[i] / other.params[i]) < tolerance for i in range(len(self.params)))
