#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
""" create stack by using linked list """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        else:
            node.next = self.linked_list.head
            self.linked_list.head = node

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty stack')
        node = self.linked_list.head.data
        self.linked_list.head = self.linked_list.head.next
        return node

    def peek(self):
        if self.is_empty():
            raise Exception('Empty stack')
        return self.linked_list.head.data

    def delete_stack(self):
        self.linked_list.head = None


if __name__ == '__main__':
    my_stack = StackByLinkedList()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    print(my_stack)
    while not my_stack.is_empty():
        my_stack.pop()
        my_stack.pop()
    print(my_stack)
