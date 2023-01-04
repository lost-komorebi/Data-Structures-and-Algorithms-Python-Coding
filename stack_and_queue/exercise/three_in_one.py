#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
""" Describe how you could use a single Python list to implement three stacks. """


class Stack:
    def __init__(self, stack_num, stack_size):
        self.stack_size = stack_size
        self.list = (stack_num * self.stack_size) * [None]

    def __repr__(self):
        return ' '.join(map(str, self.list))

    def get_stack(self, stack_num):
        start = (stack_num - 1) * self.stack_size
        end = start + self.stack_size
        return [self.list[start: end], start, end]

    def is_full(self, stack_num):
        if self.get_stack(stack_num)[0].count(None) == 0:
            return True
        return False

    def is_empty(self, stack_num):
        if self.get_stack(stack_num)[0].count(None) == self.stack_size:
            return True
        return False

    def push(self, stack_num, data):
        if self.is_full(stack_num):
            raise Exception('Full stack')
        stack = self.get_stack(stack_num)[0]
        for index, i in enumerate(stack):
            if i is None:  # update first element which is None
                self.list[self.get_stack(stack_num)[1] + index] = data
                return

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Empty stack')
        stack = self.get_stack(stack_num)[0]
        if self.is_full(stack_num):
            data = self.list[self.get_stack(stack_num)[2] - 1]
            self.list[self.get_stack(stack_num)[2] - 1] = None
            return data
        for index, data in enumerate(stack):
            if data is not None and stack[index +
                                          1] is None:  # pop last element which is not None
                self.list[self.get_stack(stack_num)[1] + index] = None
                return data


my_stack = Stack(3, 3)
print(my_stack)
my_stack.push(1, 0)
my_stack.push(1, 1)
my_stack.push(1, 2)
print(my_stack)
my_stack.pop(1)
print(my_stack)
my_stack.pop(1)
print(my_stack)
my_stack.push(3, 2)
print(my_stack)
my_stack.pop(2)
