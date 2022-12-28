#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


def factorial(n):
    """ calculate factorial of n"""
    assert 0 <= n == int(n), 'N must be a positive integer or 0!'
    if n in [0, 1]:
        return n
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """ calculate the nth(starts from 0) fibonacci """
    assert 0 <= n == int(n), 'N must be a positive integer or 0!'
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    """ calculate the sum of each(unit, ten, hundred ...)  digit"""
    assert 0 <= n == int(n), 'N must be a positive integer or 0!'
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def get_power(base, exp):
    """ get base to the exp-th (power) """
    assert int(exp) == exp, 'The exponent must be an integer number'
    if exp == 0:
        return
    elif exp == 1:
        return base
    elif exp < 0:  # x⁻ⁿ =  1 / xⁿ
        return 1 / (base * get_power(base, -exp - 1))
    return base * get_power(base, exp - 1)


def gcd(x, y):
    """ Using Euclidean to get the greatest common divisor """
    assert int(x) == x and int(y) == y, 'The numbers must be integer'
    if y == 0:
        return x
    else:
        return gcd(abs(y), abs(x % y))  # the divisors of -n and n are the same


def binary_convertor(n):
    """ convert decimal to binary """
    assert 0 <= n == int(n), 'N must be a positive integer or 0!'
    if n == 0:
        return 0
    return n % 2 + 10 * (binary_convertor(n // 2))



