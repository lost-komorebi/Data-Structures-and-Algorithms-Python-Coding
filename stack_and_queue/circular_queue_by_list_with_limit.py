#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class CircularQueue:
    def __init__(self, length):
        self.list = length * [None]
        self.length = length
        self.start = -1
        self.end = -1

    def en_queue(self, data):
        if self.is_full():
            raise Exception('This queue is full')
        if self.is_empty():
            self.list.append(data)
            self.start = 0
            self.end = 0
        else:
            if self.start < self.end < self.length - 1:
                self.list.append(data)
                self.end += 1
            else:
                self.list.append(data)
                self.end = self.length - self.end - 1

    def de_queue(self):
        if self.is_empty():
            raise Exception('Empty queue')
        self.start += 1
        return self.list.pop(0)

    def is_empty(self):
        if self.start == self.end == -1:
            return True

    def is_full(self):
        if self.start == 0 and self.end == self.length - 1:
            return True
        elif self.start - self.end == 1:
            return True
        return False

    def peek(self):
        return self.list[0]

    def clear(self):
        self.list = None
