#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


def radix_sorting(li: list) -> list:

    n = len(str(max(li)))  # get length of max number
    for l in range(n):
        buckets = [[] for i in range(10)]  # create 10 buckets
        for i in li:
            # put each number into different buckets according to its digit number, then ten's digit
            # then hundred's digit ......
            buckets[(i // (10**l)) % 10].append(i)
        # put numbers back and then continue compare next digit number
        li = [i for sub in buckets for i in sub]
    return li


if __name__ == '__main__':
    li = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81, 111]
    assert radix_sorting(li) == sorted(li)
