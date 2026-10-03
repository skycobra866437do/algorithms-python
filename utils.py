"""Reusable helper functions for algorithm implementations."""

from math import isqrt


def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of two integers."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the non-negative least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs((a // gcd(a, b)) * b)


def is_prime(number: int) -> bool:
    """Return whether an integer is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def sieve(limit: int) -> list[int]:
    """Return all prime numbers less than or equal to a non-negative limit."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if limit < 2:
        return []

    prime_flags = bytearray(b"\x01") * (limit + 1)
    prime_flags[0:2] = b"\x00\x00"

    for number in range(2, isqrt(limit) + 1):
        if prime_flags[number]:
            start = number * number
            count = ((limit - start) // number) + 1
            prime_flags[start : limit + 1 : number] = b"\x00" * count

    return [number for number, flag in enumerate(prime_flags) if flag]