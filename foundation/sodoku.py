#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import timeit
from timeit import Timer


def recursive_binary_search(li: list, n: int, start: int = None, end: int = None) -> bool:
    if start is None:
        start = 0
    if end - start == 0:
        return False
    mid_point = (start + end) // 2
    if li[mid_point] == n:
        return True
    elif n < li[mid_point]:
        return recursive_binary_search(li, start, mid_point-1, n)
    else:
        return recursive_binary_search(li[mid_point+1:], n)


if __name__ == '__main__':
    li = [0, 1, 2, 3]
    n = 5
    print(recursive_binary_search(li, 5))
