#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class SubStack:
    def __init__(self, length):
        self.length = length
        self.list = []

    def __repr__(self):
        return '\n'.join(map(str, reversed(self.list)))

    def is_full(self):
        if len(self.list) == self.length:
            return True
        return False

    def is_empty(self):
        if not self.list:
            return True
        return False

    def push(self, data):
        if self.is_full():
            raise Exception('Full stack')
        self.list.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception('Empty stack')
        return self.list.pop()


class Stack:
    def __init__(self, length):
        self.length = length
        self.list = []

    def pop(self):
        """ return and remove last element from last substack """
        if self.is_empty():
            raise Exception('Empty stack')
        data = self.list[-1].pop()
        if self.list[-1].is_empty():  # remove last substack if last substack is empty
            self.list.pop()
        return data

    def push(self, data):
        """ push element into last substack """
        if self.is_empty() or self.list[-1].is_full():  # add new substack
            self.list.append(SubStack(self.length))
        self.list[-1].push(data)

    def pop_at(self, index):
        """ return and remove element from specific substack """
        if self.is_empty():
            raise Exception('Empty stack')
        try:
            self.list[index]
        except IndexError:
            raise Exception('list index out of range')
        else:
            data = self.list[index].pop()
            if self.list[index].is_empty(
            ):  # remove specific substack if specific substack is empty
                self.list.pop(index)
            return data

    def is_empty(self):
        if not self.list:
            return True
        return False
