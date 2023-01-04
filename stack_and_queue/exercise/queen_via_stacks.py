#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Stack:
    def __init__(self):
        self.list = []

    def __repr__(self):
        return '\n'.join(map(str, reversed(self.list)))

    def __iter__(self):
        for i in self.list:
            yield i

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        if not self.list:
            return True
        return False


class Queue:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def en_queue(self, data):
        self.list1.push(data)

    def de_queue(self):
        if self.list1.is_empty():
            raise Exception('No elements in stack1')
        while not self.list1.is_empty():
            data = self.list1.pop()
            self.list2.push(data)
        self.list2.pop()
        while not self.list2.is_empty():
            data = self.list2.pop()
            self.list1.push(data)


stack1 = Stack()
stack2 = Stack()
my_queue = Queue(stack1, stack2)
my_queue.en_queue(1)
my_queue.en_queue(2)
my_queue.en_queue(3)
print(stack1)
print('>>>>>>>>>>>>')
my_queue.de_queue()
print(stack1)
print('>>>>>>>>>>>>')
print(stack2)
