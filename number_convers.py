"""
This file contains functions that performs natural numbers conversion
"""

MAX_16_BIT_NUMBER = 65535


def is_natural_number(number) -> bool:
    """Checks if value is a natural number"""
    return isinstance(number, int) and number >= 0


def convert_natural_number(number: int) -> str:
    """Converts a natural number to binary"""
    if not is_natural_number(number):
        raise ValueError("Not a natural number")

    if number > MAX_16_BIT_NUMBER:
        raise ValueError("Number exceeds 16 bits")

    return bin(number)[2:]
