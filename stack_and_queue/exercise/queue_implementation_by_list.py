#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
It is possible to implement a queue such that both enqueue and dequeue have 𝑂(1) performance on average.
In this case it means that most of the time enqueue and dequeue will be 𝑂(1)
except in one particular circumstance where dequeue will be 𝑂(𝑛).
use a limited-size list to implement a queue
"""


class Queue:
    def __init__(self, max_size=10):
        self.items = [None for i in range(max_size)]

        self.max_size = max_size
        self.length = 0
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear is None

    def _is_full(self):
        if self.front == 0 and self.rear == self.max_size - 1:
            return True
        if self.front is not None and self.rear == self.front - 1:
            return True

    def _add_new_space(self):
        self.items.extend(None for i in range(self.max_size * 2))
        self.max_size *= 3

    def enqueue(self, value):
        need_to_more_space = self._is_full()
        if need_to_more_space:
            self._add_new_space()
        if self.is_empty():

            self.rear += 1
            self.front = self.rear

        elif self.front == 0 and self.rear < self.max_size - 1:
            self.rear += 1
            self.items[self.rear] = value
        elif self.front > 0 and self.rear == self.max_size - 1:
            self.rear = 0
            self.items[self.rear] = value
        else:  # 0 < rear < front
            self.rear += 1
            self.items[self.rear] = value
        self.items[0] = value
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty queue')
        if self.front < self.max_size - 1 and self.front != self.rear:
            self.items[self.front] = None
            self.front += 1
        elif self.rear < self.front == self.max_size - 1:
            self.items[self.front] = None
            self.front = self.rear
        elif self.front == self.rear is not None:  # last element
            self.items[self.front] = None
            self.front = self.rear = None
        self.length -= 1


if __name__ == '__main__':
    q = Queue(3)
    print(q.items, q.front, q.rear, q.length)
    q.enqueue(0)
    print(q.items, q.front, q.rear, q.length)
    q.enqueue(1)
    print(q.items, q.front, q.rear, q.length)
    q.enqueue(2)
    print(q.items, q.front, q.rear, q.length)

    q.dequeue()
    print(q.items, q.front, q.rear, q.length)
    q.dequeue()

    print(q.items, q.front, q.rear, q.length)
    q.enqueue(4)
    print(q.items, q.front, q.rear, q.length)
    q.dequeue()
    print(q.items, q.front, q.rear, q.length)
    q.enqueue(5)
    print(q.items, q.front, q.rear, q.length)
    q.dequeue()
    print(q.items, q.front, q.rear, q.length)
    q.enqueue(6)
    print(q.items, q.front, q.rear, q.length)
    # q.enqueue(3)
    # print(q.items, q.front, q.rear, len(q.items))
    # q.enqueue(4)
    # print(q.items, q.front, q.rear, len(q.items))
    # q.enqueue(5)
    # print(q.items, q.front, q.rear, len(q.items))
    # q.enqueue(6)
    # print(q.items, q.front, q.rear, len(q.items))
    # q.enqueue(7)
    # print(q.items, q.front, q.rear, len(q.items))
    # q.enqueue(8)
    # print(q.items, q.front, q.rear, len(q.items))
