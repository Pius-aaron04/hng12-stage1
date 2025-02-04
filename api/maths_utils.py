"""
Defines math utility functions
"""

from math import isqrt
import requests

def is_even(number: int) -> bool:
    '''checks the parity of a number

    number: int
    rtype: bool

    returns true if number is even
    '''

    return number % 2 == 0

def is_perfect(number: int) -> bool:
    '''Checks if a number is a perfect square

    number: int
    rtype: bool

    returns true if number is a perfect square
    '''

    sqrt = isqrt(number) # gets the square root of the number

    return sqrt ** 2 == number # confirms square root


def get_fact(number: int, fact_type: str="math") -> str:
    '''fetch fun fact about `number` via a public web API

    number: int
    rtype: str fun fact message
    '''

    if fact_type not in ['math', 'trivial', 'year', 'date']:
        raise Exception('Unsupported fun fact path type')

    r = requests.get(f'http://numbersapi.com/{number}/{fact_type}')

    return r.text

def is_armstrong(number: int) -> bool:
    str_n = str(number)

    sum_ = 0

    for digit in str_n:
        sum_ += int(digit) ** 3

    return sum_ == number


def is_prime(number: int) -> bool:
    '''checks if a number is a prime

    number: int
    rtype: bool
    '''

    if number <= 1:
        return False
    for i in  range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
