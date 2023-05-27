# exec(open('C:/Users/win 10/Desktop/Projects/Python/pimath/calcWork/Vector.py').read())
from math import *


class Vector:
    tolerance = 0.001

    def __init__(self, *params):
        self.params = params

    def __repr__(self):
        return f"Vector({str(self.params)[1:-1]})"

    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(*[self.params[i] + other for i in range(len(self.params))])
        elif isinstance(other, Vector):
            if len(self.params) != len(other.params):
                raise ValueError("Vector lengths are not compatible for addition.")
            else:
                return Vector(*[self.params[i] + other.params[i] for i in range(len(self.params))])
        else:
            raise TypeError("Unsupported operand type for addition.")

    def __sub__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(*[self.params[i] - other for i in range(len(self.params))])
        elif isinstance(other, Vector):
            if len(self.params) != len(other.params):
                raise ValueError("Vector lengths are not compatible for subtraction.")
            else:
                return Vector(*[self.params[i] - other.params[i] for i in range(len(self.params))])
        else:
            raise TypeError("Unsupported operand type for subtraction.")

    def dot(self, other) -> float:
        if len(self.params) != len(other.params):
            raise ValueError("Vector lengths are not compatible for dot.")
        return sum(self.params[i] * other.params[i] for i in range(len(self.params)))

    def __mul__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(*[self.params[i] * other for i in range(len(self.params))])
        elif isinstance(other, Vector):
            if len(self.params) != len(other.params):
                raise ValueError("Vector lengths are not compatible for element-wise multiplication.")
            else:
                return Vector(*[self.params[i] * other.params[i] for i in range(len(self.params))])
        else:
            raise TypeError("Unsupported operand type for multiplication.")

    def __truediv__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(*[self.params[i] / other for i in range(len(self.params))])
        elif isinstance(other, Vector):
            if len(self.params) != len(other.params):
                raise ValueError("Vector lengths are not compatible for element-wise division.")
            else:
                return Vector(*[self.params[i] / other.params[i] for i in range(len(self.params))])
        else:
            raise TypeError("Unsupported operand type for division.")

    def __len__(self):
        return len(self.params)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return len(self.params) == len(other.params) and all(
            abs(param) < self.tolerance for param in (self - other).params)

    def magnitude(self) -> float:
        return sqrt(sum(ai ** 2 for ai in self.params))

    def is_zero(self) -> bool:
        return all(abs(param) < self.tolerance for param in self.params)

    def is_parallel(self, other: 'Vector') -> bool:
        ratio = self.params[0] / other.params[0]
        return all(abs(ratio - self.params[i] / other.params[i]) < Vector.tolerance for i in range(len(self.params)))

    @staticmethod
    def zeroes(dim: int) -> 'Vector':
        return Vector(*[0 for _ in range(dim)])

    @staticmethod
    def ones(dim: int) -> 'Vector':
        return Vector(*[1 for _ in range(dim)])
