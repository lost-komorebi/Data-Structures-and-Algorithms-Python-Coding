#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Implement two Queue ADT,
1. Using a list such that the rear of the queue is at the end of the list.
2. Using a list such that the rear of the queue is at the beginning of the list.
Design and implement an experiment to do benchmark comparisons of the two queue implementations.
"""
from timeit import Timer


class Queue1:
    """ the rear of the queue is at the end of the list """

    def __init__(self):
        self.items = []

    def init(self, n):
        self.items = list(range(n))

    def enqueue(self, item):
        """ time complexity O(1) """
        self.items.append(item)

    def dequeue(self):
        """ time complexity O(n) """
        self.items.pop(0)


class Queue2:
    """ the rear of the queue is at the beginning of the list """

    def __init__(self):
        self.items = []

    def init(self, n):
        self.items = list(range(n))

    def enqueue(self, item):
        """ time complexity O(n) """
        self.items.insert(0, item)

    def dequeue(self):
        """ time complexity O(1) """
        self.items.pop()


q1 = Queue1()
q2 = Queue2()
enqueue_q1 = Timer('q1.enqueue(i)', 'from __main__ import i, q1')
enqueue_q2 = Timer('q2.enqueue(i)', 'from __main__ import i, q2')

for i in range(1000000, 100000001, 1000000):
    t1 = enqueue_q1.timeit(number=1000)
    t2 = enqueue_q2.timeit(number=1000)
    print(i, "%15.7f,%15.7f" % (t1, t2))


dequeue_q1 = Timer('q1.dequeue()', 'from __main__ import q1')
dequeue_q2 = Timer('q2.dequeue()', 'from __main__ import q2')

for i in range(100000, 10000001, 100000):
    q1 = Queue1()
    q1.init(i)
    t1 = dequeue_q1.timeit(number=10)
    q2 = Queue2()
    q2.init(i)
    t2 = dequeue_q2.timeit(number=10)
    print(i, "%15.7f,%15.7f" % (t1, t2))


# conclusion
# According to those data, we can see if we use a list such that the rear of the queue is at the end of the list,
# Then its enqueue operator is O(1) time complexity and its dequeue operator is O(n) time complexity.
# If we use a list such that the rear of the queue is at the beginning of the list,
# Then its enqueue operator is O(n) time complexity and its dequeue
# operator is O(1) time complexity.
