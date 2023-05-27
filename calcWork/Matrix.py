# exec(open('C:/Users/win 10/Desktop/Projects/Python/pimath/calcWork/Vector.py').read())
import itertools
from math import *
from typing import List
from itertools import chain


class Matrix:
    tolerance = 0.001

    @staticmethod
    def almostEq(a: float, b: float) -> bool:
        return abs(a - b) < Matrix.tolerance

    def __init__(self, params):
        for one_d in params:
            if len(one_d) != len(params[0]):
                raise ValueError("Can't have Matrix with different length rows")
        self.params = params
        self.dim = (len(params), len(params[0]))
        self.rows = len(params)
        self.cols = len(params[0])

    def __repr__(self):
        len_max = max(len(str(ele)) for one_d in self.params for ele in one_d)
        return "\n".join(
            ["[" + "|".join(str(ele).ljust(len_max, ' ') for ele in one_d) + "]" for one_d in self.params])

    @staticmethod
    def zeros(r, c):
        return Matrix([[0 for _ in range(c)] for _ in range(r)])

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.dim == other.dim and all(
            Matrix.almostEq(e1, e2) for e1, e2 in zip(itertools.chain(*self.params), itertools.chain(*self.params)))

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if isinstance(other, (int, float)):
            return Matrix([[self.params[i][j] + other for j in range(self.cols)] for i in range(self.rows)])
        elif isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrices must be of the same dimension for addition.")
            return Matrix(
                [[self.params[i][j] + other.params[i][j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            raise TypeError("Unsupported operand type for addition.")

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if isinstance(other, (int, float)):
            return Matrix([[self.params[i][j] - other for j in range(self.cols)] for i in range(self.rows)])
        elif isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrices must be of the same dimension for subtraction.")
            return Matrix(
                [[self.params[i][j] - other.params[i][j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            raise TypeError("Unsupported operand type for subtraction.")

    def __mul__(self, other) -> 'Matrix':
        if isinstance(other, (int, float)):
            return Matrix([[self.params[i][j] * other for j in range(self.cols)] for i in range(self.rows)])
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrix dimensions are not compatible for multiplication.")
            result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
            for i, j , k in itertools.product(range(self.rows), range(other.cols) , range(self.cols)):
                    result[i][j] += self.params[i][k] * other.params[k][j]
            return Matrix(result)
        else:
            raise TypeError("Unsupported operand type for multiplication.")

    def __truediv__(self, other) -> 'Matrix':
        if isinstance(other, (int, float)):
            return Matrix([[self.params[i][j] / other for j in range(self.cols)] for i in range(self.rows)])
        else:
            raise TypeError("Unsupported operand type for division.")

