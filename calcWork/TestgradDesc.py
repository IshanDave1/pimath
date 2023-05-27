from unittest import TestCase

from calcWork.Vector import Vector
from gradDesc import gd_general
import numpy as np
import matplotlib.pyplot as plt


class TestgradDesc(TestCase):
    def setUp(self):
        def f(v: Vector) -> float:
            x, y, z = v.params
            return x * x + 4 * y * y + 6 * z * z - 20 * x - 16 * y + 24 * z

        self.f = f

        self.points = []

        def linear(m, c):
            return lambda x: m * x + c

        x = np.arange(0, 10, 0.5)
        e = 3 * np.random.uniform(-1, 1, size=x.shape[0])
        y = linear(3, 0)(x) + e
        plt.plot(x, y, '.')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Plot of (X, Y) Tuples')

        # Show the plot

        print(y)

        def sq_cost(v: Vector) -> float:
            m, c = v.params
            return sum((y0 - (m * x0 + c)) ** 2 for (x0, y0) in zip(x, y))

        print(sq_cost(Vector(3,0)))
        vector = gd_general(sq_cost, Vector(1,2), 0.0008, 0.1)
        print(vector)
        plt.plot(np.arange(0, 10, 0.5),  vector.params[0] * x + vector.params[1])

        plt.show()

    def test_gd_general(self):
        pass
        # self.assertEqual(gd_general(self.f, Vector(1, 3, 5), 0.1, 0.001), Vector(10, 2, -2))
