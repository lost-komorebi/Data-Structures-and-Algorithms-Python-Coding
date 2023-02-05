#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        s = self.items.pop()
        return s

    def is_empty(self):
        return self.items == []


def base_converter(n, base):
    digits = '0123456789ABCDE'
    my_stack = Stack()
    while n > 0:
        remainder = n % base
        n = n // base

        my_stack.push(remainder)
    result = ''
    while not my_stack.is_empty():
        result += str(digits[my_stack.pop()])
    return result


if __name__ == '__main__':
    print(base_converter(128745123, 16))
    print(base_converter(25, 8))
    print(base_converter(256, 16))
    print(base_converter(26, 26))
