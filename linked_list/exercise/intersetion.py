#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from base import LinkedList


def intersection(l1, l2):
    node1 = l1.head
    node2 = l2.head
    if len(l1) > len(l2):
        for i in range(len(l1) - len(l2)):
            node1 = node1.next
    else:
        for i in range(len(l2) - len(l1)):
            node2 = node2.next
    while node1:
        if node1 == node2:
            return node1
        node1 = node1.next
        node2 = node2.next


def intersection1(l1, l2):
    for node1 in l1:
        for node2 in l2:
            if node1 == node2:
                return node1


common_list = LinkedList([9, 1, 6])
l1 = LinkedList([1, 2, 3, 4, 5, 6, 7])
l2 = LinkedList([1, 2, 3, 4, 5, 6])
l1.add_linked_list(common_list)
l2.add_linked_list(common_list)
print(l1)
print(l2)
print(intersection(l1, l2))
print(intersection1(l1, l2))
