#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
""" use python to implement a deque data structure """


class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise Exception("Cannot remove from a empty deque")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Cannot remove from a empty deque")
        return self.items.pop()
