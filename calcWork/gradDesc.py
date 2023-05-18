import logging
from typing import Callable
from Vector import Vector

#logging.basicConfig(level=logging.INFO)
delta = 0.001


def gd_general(f: Callable[[Vector], float], guess: Vector, lr: float = 0.1, threshold: float = 0.01):
    def ivec(index, length):
        return Vector(*[delta if i == index else 0 for i in range(length)])

    value = f(guess)
    grad = (Vector(*[f(guess + ivec(i, len(guess))) for i in range(len(guess))])
            -
            (Vector.ones(len(guess)) * value)
            ) / delta
    guess = guess - grad * lr
    logging.info(f"guessing {guess} grad is {grad}")
    return guess if grad.magnitude() < threshold else gd_general(f, guess, lr, threshold)
