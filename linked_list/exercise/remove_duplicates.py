#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from base import LinkedList


def remove_duplicates(ll):
    if ll.head is None:
        return
    list_values = []
    node = ll.head
    list_values.append(node.data)
    while node.next:
        if node.next.data not in list_values:
            list_values.append(node.next.data)
            node = node.next
        else:
            node.next = node.next.next
    return ll


def remove_duplicates1(ll):
    if ll.head is None:
        return
    node = ll.head
    while node.next:
        if node.next.data == node.data:
            node.next = node.next.next
        node = node.next


my_ll = LinkedList([1, 2, 3, 3, 1, 2, 3])
print(my_ll)
remove_duplicates(my_ll)
print(my_ll)
remove_duplicates1(my_ll)
print(my_ll)
