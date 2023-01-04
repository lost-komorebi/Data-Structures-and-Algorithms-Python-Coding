#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
How would you design a stack which,
in addition to push and pop,
has a function min which returns the minimum element?
Push, pop and min should all operate in O(1).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min_value = data  # record the min_value of whole stack when this node is the top

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return ' -> '.join([str(i.data) for i in self])


class StackByLinkedList:
    def __init__(self):
        self.linked_list = LinkedList()

    def __repr__(self):
        return '\n'.join([str(i.data) for i in self.linked_list])

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        return False

    def push(self, data):
        node = Node(data)
        if self.is_empty():
            self.linked_list.head = node
            self.linked_list.head.min_value = data
        else:
            if self.linked_list.head.min_value < data:
                node.min_value = self.linked_list.head.min_value
            node.next = self.linked_list.head  # add next reference
            self.linked_list.head = node  # set new head

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty stack')
        node = self.linked_list.head.data
        self.linked_list.head = self.linked_list.head.next  # set new head to next node
        return node

    def min(self):
        if self.linked_list.head is None:
            return None
        return self.linked_list.head.min_value


my_stack = StackByLinkedList()
print(my_stack.min())
my_stack.push(3)
my_stack.push(2)
my_stack.push(4)
my_stack.push(1)
my_stack.push(0)
my_stack.pop()
print(my_stack.min())
