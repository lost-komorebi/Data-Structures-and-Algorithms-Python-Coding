#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class CircularQueue:
    def __init__(self, length):
        self.length = length
        self.list = [None] * self.length
        self.start = -1
        self.end = -1

    def __repr__(self):
        return ' '.join(map(str, self.list))

    def en_queue(self, data):
        if self.is_full():
            raise Exception('This queue is full')
        if self.end == self.length - 1:  # it means self.end is at the last of the list
            self.end = 0
        else:
            self.end += 1
            if self.start == -1:
                self.start = 0
                self.end = 0
        self.list[self.end] = data

    def de_queue(self):

        if self.is_empty():
            raise Exception('Empty queue')
        data = self.list[self.start]
        start = self.start
        if self.start == self.end:  # queue has only one element
            self.clear()
        elif self.start == self.length - 1:  # self.start is at the last index
            self.start = 0
        else:
            self.start += 1
        self.list[start] = None
        return data

    def is_empty(self):
        if self.start == self.end == -1:
            return True
        return False

    def is_full(self):
        if self.start == 0 and self.end == (self.length - 1):
            return True
        elif self.start - self.end == 1:
            return True
        return False

    def peek(self):
        return self.list[self.start]

    def clear(self):
        self.list = []
        self.start = -1
        self.end = -1


my_q = CircularQueue(3)
my_q.en_queue(1)
my_q.en_queue(2)
my_q.en_queue(3)
print(my_q)
print(my_q.de_queue())
print(my_q)
my_q.en_queue(4)
print('111', my_q)
print(my_q.peek())
