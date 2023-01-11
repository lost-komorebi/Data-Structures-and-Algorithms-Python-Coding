#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
number of buckets = round(sqrt(number of elements))
appropriate bucket = ceil(value * number of buckets/maxvalue)
need more space
time complexity: O(N^2)
space complexity: O(N)
"""
import math
import random


def insertion_sort(li: list):
    for i in range(1, len(li)):
        j = i
        # compare element with elements which are in sorted area
        while li[j - 1] > li[j] and j > 0:
            li[j - 1], li[j] = li[j], li[j - 1]  # swap location
            j -= 1
    return li


def bucket_sort(li: list):
    n = round(math.sqrt(len(li)))  # number of buckets
    max_value = max(li)
    result = []
    for i in range(n):  # create 2d list
        result.append([])
    for _ in li:  # distribute elements into bucket
        index = math.ceil(_ * n / max_value) - 1
        result[index].append(_)
    result = [insertion_sort(i) for i in result]  # sorting
    return [j for i in result for j in i]


if __name__ == '__main__':
    my_list = []
    for x in range(10):
        my_list.append(random.uniform(0, 1))
    print(my_list)
    my_list = bucket_sort(my_list)
    print(my_list)
