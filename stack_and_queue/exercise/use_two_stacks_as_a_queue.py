#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
It is possible to implement a queue such that both enqueue and dequeue have 𝑂(1) performance on average.
In this case it means that most of the time enqueue and dequeue will be 𝑂(1)
except in one particular circumstance where dequeue will be 𝑂(𝑛).
use two stacks as a queue
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def dequeue(self):
        if not self.outbox.items:  # outbox is None
            while self.inbox.items:
                self.outbox.push(self.inbox.pop())
            return self.outbox.pop()
        else:
            return self.outbox.pop()

    def enqueue(self, value):
        self.inbox.push(value)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
