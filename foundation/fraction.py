#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" use python to implement a fraction class """


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise Exception('Numerator must be int')
        if not isinstance(denominator, int) or denominator == 0:
            raise Exception('Denominator must be a non-zero int')
        gcd = self.gcd(denominator, numerator)
        self.numerator = numerator // gcd  # maintain the lowest term
        self.denominator = denominator // gcd

    def gcd(self, m, n):
        """ calculate greatest common divisor """
        if n == 0:
            return 1
        while n != 0 and m % n != 0:
            m, n = n, m % n
        return n

    def get_num(self):
        return self.numerator

    def get_den(self):
        return self.denominator

    def __str__(self):
        if self.denominator < 0:
            return '-' + str(self.numerator) + '/' + str(abs(self.denominator))
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        if self * Fraction(-1, 1) == other:
            return 0
        else:
            self.numerator = self.numerator * other.denominator \
                + other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
            return Fraction(self.numerator, self.denominator)

    def __sub__(self, other):
        if self == other:
            return 0
        else:
            self.numerator = self.numerator * other.denominator \
                - other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
            return Fraction(self.numerator, self.denominator)

    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num == second_num

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        reciprocal = Fraction(other.denominator, other.numerator)
        return self.__mul__(reciprocal)

    def __lt__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num < second_num

    def __gt__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num > second_num

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    # __radd__ = __add__
    # __iadd__ = __add__
    # __repr__ = __str__


if __name__ == '__main__':
    my_f1 = Fraction(2, -4)
    my_f2 = Fraction(1, 2)
    print(my_f1, my_f2)
    print(my_f1 + my_f2)
    print(my_f1 - my_f2)
    print(my_f1 * my_f2)
    print(my_f1 / my_f2)
    print(my_f1 > my_f2)
    print(my_f1 < my_f2)
    print(my_f1 >= my_f2)
    print(my_f1 <= my_f2)
    print(my_f1 == my_f2)
    print(my_f1 != my_f2)
    print(my_f1)
    print(my_f1 + 4)
    my_f1 += 1
    print(my_f1)
