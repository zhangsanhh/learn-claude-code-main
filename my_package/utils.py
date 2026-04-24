"""
utils.py
~~~~~~~~
Common utility functions for my_package.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (case-insensitive, ignores spaces).

    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
