from math import *
# exec(open('C:/Users/win 10/Desktop/Projects/Python/pimath/calcWork/Vector.py').read())
from Function import *


def derivative(function, epsilon=0.001):
    return lambda x: (function(x + epsilon) - function(x)) / epsilon


f = derivative(lambda x: x * x * x)

print(f(2))

ten = cf(10)
