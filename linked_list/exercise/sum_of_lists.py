#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from base import LinkedList
from random import randint
from functools import reduce


def fn(x, y):
    return x * 10 + y


def sum_of_lists(l1, l2):
    l1_list = [i.data for i in l1]
    l1_list.reverse()
    l2_list = [i.data for i in l2]
    l2_list.reverse()
    l1_value = reduce(fn, l1_list)
    l2_value = reduce(fn, l2_list)
    temp_list = list(str(l1_value + l2_value))
    temp_list.reverse()
    return LinkedList(temp_list)


list1 = LinkedList([randint(1, 9) for _ in range(10)])
list2 = LinkedList([randint(1, 9) for _ in range(10)])
print(list1)
print(list2)
print(sum_of_lists(list1, list2))
