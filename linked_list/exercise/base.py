#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, nodes: list = None):
        self.head = None
        self.tail = None
        if nodes is not None:
            self.head = Node(data=nodes.pop(0))
            node = self.head
            for ele in nodes:
                node.next = Node(data=ele)
                node = node.next
            self.tail = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return ' -> '.join([str(_.data) for _ in self])

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def add_linked_list(self, ll):
        node = self.tail
        node.next = ll.head
        self.tail = ll.tail


if __name__ == '__main__':
    l1 = LinkedList([1, 2, 3])
    l2 = LinkedList([1, 2, 3])
    print(l1 == l2)
