"""
tests/test_utils.py
~~~~~~~~~~~~~~~~~~~
Unit tests for my_package.utils.
"""

import pytest
from my_package.utils import add, subtract, multiply, divide, is_palindrome


# ──────────────────────────────────────────────
# add
# ──────────────────────────────────────────────
class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_zero(self):
        assert add(0, 0) == 0


# ──────────────────────────────────────────────
# subtract
# ──────────────────────────────────────────────
class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 7) == -4

    def test_same_numbers(self):
        assert subtract(5, 5) == 0


# ──────────────────────────────────────────────
# multiply
# ──────────────────────────────────────────────
class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(99, 0) == 0

    def test_negative(self):
        assert multiply(-2, 5) == -10

    def test_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)


# ──────────────────────────────────────────────
# divide
# ──────────────────────────────────────────────
class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Division by zero"):
            divide(5, 0)

    def test_negative_divisor(self):
        assert divide(-9, 3) == -3.0


# ──────────────────────────────────────────────
# is_palindrome
# ──────────────────────────────────────────────
class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_non_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive(self):
        assert is_palindrome("RaceCar") is True

    def test_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_char(self):
        assert is_palindrome("x") is True
