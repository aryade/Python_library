import pytest
import math


class TestFactorial_1:
    def test_negative_value(self):
        with pytest.raises(ValueError, match="n must be >= 0"):
            assert factorial(-1)

    def test_float_value(self):
        with pytest.raises(ValueError,
                           match="n must be exact integer"):
            assert factorial(30.1)

    def test_large_value(self):
        with pytest.raises(OverflowError, match="n too large"):
            assert factorial(1e100)

    def test_single_value(self):
        assert factorial(0) == 1

    def test_list(self):
        output = [1, 1, 2, 6, 24, 120]
        for n in range(6):
            assert factorial(n) == output[n]

    def test_scientific_notation(self):
        with pytest.raises(OverflowError,
                           match="int too large to convert to float"):
                "{:e}".format(factorial(1000))


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