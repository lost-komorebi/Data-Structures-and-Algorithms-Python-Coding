#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from stack_and_queue.deque import Deque
import sys
sys.path.append('..')


def palindrome_checker(string):
    d = Deque()
    for i in string.replace(' ', ''):
        d.add_rear(i)
    for i in range(d.size() // 2):
        front = d.remove_front()
        rear = d.remove_rear()
        if front != rear:
            return False
    return True


if __name__ == '__main__':
    print(palindrome_checker('abcdba'))
    print(palindrome_checker('madam'))
    print(palindrome_checker('I PREFER PI'))




