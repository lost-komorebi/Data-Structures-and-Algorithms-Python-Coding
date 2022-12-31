#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """ print function """
        ll_string = ''
        temp_node = self.head
        while temp_node:
            ll_string += str(temp_node.value) + ','
            if temp_node == self.tail:  # stop loop when finish the first loop
                break
            temp_node = temp_node.next
        ll_string = ll_string.strip(',')  # removing tailing commas
        if len(ll_string):
            return '[' + ll_string + ']'
        else:
            return '[]'

    def insert(self, value, index: int):
        """ insert node into linked list at the specific index"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # the last node always references the first node
        else:
            if index == 0:
                temp_node = self.head
                self.head = new_node  # set new_node as the first node
                self.head.next = temp_node  # first node references to the former first node
                self.tail.next = self.head  # the last node always references the first node
            elif index == -1:
                temp_node = self.tail
                temp_node.next = new_node  # add new_node after former tail node
                self.tail = new_node   # set new_node as tail node
                self.tail.next = self.head  # the last node always references the first node
            else:
                current_index = 0
                current_node = self.head
                while current_index < index - 1:
                    current_node = current_node.next
                    current_index += 1
                    if current_node == self.tail:  # stop loop when finish the first loop
                        break
                # parameter index greater than length of linked list, add node
                # at the end of the linked list
                if current_node == self.tail:
                    current_node.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head
                else:
                    next_node = current_node.next
                    current_node.next = new_node
                    new_node.next = next_node

    def traversal(self):
        """ traversal linked list """
        current_node = self.head
        while current_node:
            if current_node == self.tail:
                break
            current_node = current_node.next

    def get(self, value):
        """ find the first node which value equal to the parameter value """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node.value
            else:
                if current_node == self.tail:
                    break
                else:
                    current_node = current_node.next

    def delete(self, index=-1):
        """ delete node from linked list which node's index equal to parameter index """
        current_node = self.head
        if not current_node:
            raise IndexError('delete from empty linked list')
        if current_node == self.tail:  # this linked has only one node
            self.head = self.tail = None  # empty linked list
        if index == 0:
            self.head = current_node.next
            self.tail.next = self.head
        elif index == -1:
            while current_node:
                if current_node.next == self.tail:
                    break
                current_node = current_node.next
            self.tail = current_node   # current node is the penult node
            self.tail.next = self.head
        else:
            current_index = 0
            while current_index < index - 1:
                if current_node.next == self.tail:
                    raise IndexError('delete index out of range')
                current_node = current_node.next
                current_index += 1
            if current_node.next == self.tail:
                self.tail = current_node
                self.tail.next = self.head
            else:
                next_node = current_node.next.next
                current_node.next = next_node

    def clear(self):
        """ remove all nodes from linked list """
        self.head = self.tail = None


my_ll = CircularSinglyLinkedList()
my_ll.insert(0, 0)
print(my_ll)
my_ll.insert(1, 1)
print(my_ll.head.value)
print(my_ll.head.next.value)
print(my_ll.tail.value)
print(my_ll.tail.next.value)
