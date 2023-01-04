#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" using limited list to perform queue """


class Queue:
    def __init__(self, length):
        self.list = []
        self.length = length

    def __repr__(self):
        return ' '.join(map(str, self.list))

    def de_queue(self):
        if self.is_empty():
            raise Exception('Empty queue')
        return self.list.pop(0)

    def en_queue(self, data):
        if self.is_full():
            raise Exception('This queue is full')
        self.list.append(data)

    def is_empty(self):
        if not self.list:
            return True
        return False

    def is_full(self):
        if len(self.list) == self.length:
            return True
        return False

    def clear(self):
        self.list = None

    def peek(self):
        if self.is_empty():
            raise Exception('empty queue')
        else:
            return self.list[0]


my_q = Queue(3)
print(my_q.is_empty())
my_q.en_queue(1)
my_q.en_queue(2)
my_q.en_queue(3)
print(my_q.is_full())
print(my_q)
print(my_q.peek())
print(my_q)
print(my_q.de_queue())
print(my_q)
print(my_q.is_empty())
