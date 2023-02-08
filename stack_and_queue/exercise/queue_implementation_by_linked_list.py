#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
It is possible to implement a queue such that both enqueue and dequeue have 𝑂(1) performance on average.
In this case it means that most of the time enqueue and dequeue will be 𝑂(1)
except in one particular circumstance where dequeue will be 𝑂(𝑛).
Use linked list to implement a queue, thus allowing that both enqueue and dequeue have 𝑂(1) performance
"""
from timeit import Timer


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_tail(self, value):
        temp = Node(value)
        if not self.head:
            self.head = self.tail = temp
        else:
            self.tail.set_next(temp)
            self.tail = temp

    def remove_head(self):
        if self.is_empty():
            raise Exception('Remove from empty linked list')
        self.head = self.head.get_next()

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.get_next()

    def __str__(self):
        result = []
        for node in self:
            result.append(str(node.value))
        return ' -> '.join(result)


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def init(self, n):
        for i in range(n):
            self.items.add_tail(i)

    def enqueue(self, value):
        self.items.add_tail(value)

    def dequeue(self):
        self.items.remove_head()


q = Queue()

enqueue_q = Timer('q.enqueue(i)', 'from __main__ import i, q')


for i in range(1000000, 100000001, 1000000):
    t = enqueue_q.timeit(number=1000)
    print(i, "enqueue_time: %15.7f" % t)


dequeue_q = Timer('q.dequeue()', 'from __main__ import q')


for i in range(100000, 10000001, 100000):
    q = Queue()
    q.init(i)
    t = dequeue_q.timeit(number=1000)
    print(i, "dequeue_time: %15.7f" % t)
