# !/usr/bin/python

def factorial(n):
    """
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large

    >>> factorial(0)
    1

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> "{:e}".format(factorial(1000))
    Traceback (most recent call last):
        ...
    OverflowError: int too large to convert to float
    """

    import math
    if not n >= 0:
        raise ValueError('n must be >= 0')
    if math.floor(n) != n:
        raise ValueError('n must be exact integer')
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError('n too large')
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()