#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Definition : a series of numbers in which each number is the sum of the two preceding numbers. 
First two numbers by definition are 0 and 1.
Example : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ....
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = 10
    fibonacci(10)
