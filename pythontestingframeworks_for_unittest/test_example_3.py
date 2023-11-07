import unittest
import math

class TestFactorial_2(unittest.TestCase):
    def test_negative_value(self):
        print('Negative Number Test')
        with self.assertRaises(ValueError, msg="n must be >= 0"):
            factorial(-1)

    def test_float_value(self):
        print('Float Value Test')
        with self.assertRaises(ValueError,
                               msg="n must be exact integer"):
            factorial(30.1)

    def test_large_value(self):
        print('Large Value Test')
        with self.assertRaises(OverflowError, msg="n too large"):
            factorial(1e100)

    def test_single_value(self):
        print('Single Value Test')
        self.assertEqual(factorial(0), 1)

    def test_list_comprehension(self):
        print('List Comprehension Test')
        self.assertEqual([factorial(n) for n in range(6)],
                         [1, 1, 2, 6, 24, 120])

    def test_scientific_notation(self):
        print('Scientific Notation Test')
        with self.assertRaises(OverflowError,
                        msg="int too large to convert to float"):
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