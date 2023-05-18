from math import *
from Function import *


def derivative(function, epsilon=0.001):
    return lambda x: (function(x + epsilon) - function(x)) / epsilon


f = derivative(lambda x: x * x * x)

print(f(2))

ten = cf(10)
