#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from base import LinkedList, Node
from random import randint


def partition(ll, n):
    if ll.head is None:
        return
    temp_list = []
    node = ll.head
    while node:
        if node.data < n:
            temp_list.insert(0, node.data)
        else:
            temp_list.append(node.data)
        node = node.next
    ll.head = Node(data=temp_list.pop(0))
    node = ll.head
    for ele in temp_list:
        temp_node = Node(ele)
        node.next = temp_node
        node = node.next


lists = [randint(1, 100) for i in range(10)]
my_ll = LinkedList(lists)
print(my_ll)
partition(my_ll, 50)
print(my_ll)
