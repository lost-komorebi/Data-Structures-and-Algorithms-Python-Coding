#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import random
import timeit
from timeit import Timer
from random import randint

# 1. Devise an experiment to verify that the list index operator is 𝑂(1).

get_item = Timer('li[index]', 'from __main__ import li, index')
set_item = Timer('li[index]=value', 'from __main__ import li, index, value')

for i in range(1000000, 100000001, 1000000):
    index = randint(0, i)
    value = randint(0, i)
    li = list(range(i))
    t1 = get_item.timeit(number=1000)
    t2 = set_item.timeit(number=1000)
    print("%15.6f,%15.6f" % (t1, t2))

# 2. Devise an experiment to verify that get item and set item are 𝑂(1)
# for dictionaries.

get_item = Timer('dic[index]', 'from __main__ import dic, index')
set_item = Timer('dic[index]=value', 'from __main__ import dic, index, value')

for i in range(1000000, 100000001, 1000000):
    index = randint(0, i)
    value = randint(0, i)
    dic = {j: None for j in range(i)}
    t1 = get_item.timeit(number=1000)
    t2 = set_item.timeit(number=1000)
    print("%15.7f,%15.7f" % (t1, t2))


# 3. Devise an experiment that compares the performance of the del
# operator on lists and dictionaries.

def dic_del(dic):
    idx = next(iter(dic))  # get first key
    del dic[idx]


del_on_list = Timer('del li[0]', 'from __main__ import li')
del_on_dict = Timer('dic_del(dic)', 'from __main__ import dic_del, dic')


for i in range(1000000, 100000001, 1000000):
    li = list(range(i))
    t1 = del_on_list.timeit(number=1000)
    dic = {j: None for j in range(i)}
    t2 = del_on_dict.timeit(number=1000)
    print("%15.7f,%15.7f" % (t1, t2))

# 4. Given a list of numbers in random order
# write a linear time algorithm to find the 𝑘th smallest number in the list.
# Explain why your algorithm is linear.


def kth_minimum(li: list, k: int) -> int:
    random_number = random.choice(li)  # pick a number randomly
    larger, smaller = [], []
    # iterate all element, divide li to two parts
    for i in li:
        if i > random_number:
            larger.append(i)
        else:
            smaller.append(i)
    # we have found len(li)-k number larger than random_number, so
    # random_number is the kth-number
    if len(smaller) == k:
        return random_number
    # smaller number quantity is less than k, so the kth-number in larger
    # number list
    elif len(smaller) < k:
        return kth_minimum(larger, k - len(smaller))
    # smaller number quantity is big than k, so the kth-number in smaller
    # number list
    else:
        return kth_minimum(smaller, k)


# 5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?


def kth_minimum1(li: list, k: int) -> int:
    """ O(nlogn) time complexity """
    li.sort()
    return li[k - 1]


if __name__ == '__main__':
    random_list = random.choices([i for i in range(1000)], k=10)
    for i in range(1, len(random_list)):
        assert kth_minimum(random_list, i) \
            == kth_minimum1(random_list, i) \
            == sorted(random_list)[i - 1]
