#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from base import LinkedList


def find_nth(ll, n):
    """ use len function """
    if ll.head is None or n > len(ll):
        return
    else:
        length = -len(ll)
        node = ll.head
        while node:
            if abs(length) == n:
                return node
            length += 1
            node = node.next


def find_nth1(ll, n):
    """ do not use len function """
    node1 = ll.head
    node2 = ll.head

    for i in range(n):
        if node2 is None:
            return
        node2 = node2.next

    while node2:
        node1 = node1.next
        node2 = node2.next
    return node1


my_ll = LinkedList([1, 2, 3, 4, 5])
print(my_ll)
print(find_nth(my_ll, 4))
print(find_nth1(my_ll, 4))
