# !/usr/bin/python

import math

def factorial(n):
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:
        raise OverflowError("n too large")

    result = 1
    factor = 2

    while factor <= n:
        result *= factor
        factor += 1
    return result
    