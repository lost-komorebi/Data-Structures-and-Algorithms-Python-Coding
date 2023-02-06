#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def hot_potato(li: list, num: int):
    q = Queue()
    for i in li:
        q.enqueue(i)

    while q.size() > 1:
        # remove first n number and put at the end of the queue, like a circle
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6]
    print(hot_potato(li, 7))
