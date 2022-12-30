#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """ add print function for linked list"""
        node_str = ''
        node = self.head  # initializing node to head
        while node:
            node_str += str(node.value) + ','
            node = node.next
        node_str = node_str.strip(',')  # removing the tail commas
        if len(node_str):
            return '[' + node_str + ']'
        else:
            return '[]'

    def insert(self, node, index):
        if self.head is None:  # this is an empty linked list
            self.head = node
            self.tail = node
        else:
            if index == 0:
                temp_node = self.head
                self.head = node
                node.next = temp_node
            elif index == -1:
                temp_node = self.tail
                self.tail = node
                temp_node.next = node
            else:
                temp_index = 0
                current_node = self.head
                while temp_index < index - 1:
                    current_node = current_node.next
                    temp_index += 1
                # current_node is the node before parameter index, so temp_node
                # is the node at the parameter index
                if current_node:
                    temp_node = current_node.next
                    current_node.next = node  # put parameter node after current_node
                    node.next = temp_node  # put parameter node before the node at the parameter index
                else:  # parameter index lager than length of linked list, put node at the end of linked list
                    temp_node = self.tail
                    self.tail = node
                    temp_node.next = node


single_linked_list = SingleLinkedList()
node0 = Node(0)
single_linked_list.insert(node0, 0)
print(single_linked_list)
node2 = Node(2)
single_linked_list.insert(node2, -1)
print(single_linked_list)
node1 = Node(1)
single_linked_list.insert(node1, 1)
print(single_linked_list)
node4 = Node(4)
single_linked_list.insert(node4, 4)
print(single_linked_list)
node5 = Node(5)
single_linked_list.insert(node5, 5)
print(single_linked_list)
node6 = Node(6)
single_linked_list.insert(node6, 6)
print(single_linked_list)
node7 = Node(7)
single_linked_list.insert(node7, 7)
print(single_linked_list)
node3 = Node(3)
single_linked_list.insert(node3, 3)
print(single_linked_list)
