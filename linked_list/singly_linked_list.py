#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:

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

    def insert(self, value, index):
        """ insert a node into a specific location on the linked list """
        new_node = Node(value)
        if self.head is None:  # this is an empty linked list
            self.head = new_node
            self.tail = new_node
        else:
            if index == 0:
                temp_node = self.head
                self.head = new_node
                new_node.next = temp_node
            elif index == -1:
                temp_node = self.tail
                self.tail = new_node
                temp_node.next = new_node
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
                    current_node.next = new_node  # put parameter node after current_node
                    new_node.next = temp_node  # put parameter node before the node at the parameter index
                else:  # parameter index lager than length of linked list, put node at the end of linked list
                    temp_node = self.tail
                    self.tail = new_node
                    temp_node.next = new_node

    def traversal(self):
        """ traversal singly linked list by printing """
        current_node = self.head
        if not current_node:  # This linked list is not exist.
            print('This linked list has no nodes')
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def get(self, value):
        """ search for a node in a singly linked list """
        current_node = self.head
        if not current_node:  # This linked list is not exist.
            print('This linked list has no nodes')
        while current_node:
            if current_node.value == value:
                return current_node.value
            current_node = current_node.next
        return None

    def delete(self, index=-1):
        """ delete a specific node from a linked list """
        current_node = self.head
        if not current_node:
            raise IndexError('delete from empty linked list')
        if index == 0:
            if self.head == self.tail:  # linked list has only one node
                self.head = None
                self.tail = None
            else:
                self.head = current_node.next
        elif index == -1:
            if self.head == self.tail:  # linked list has only one node
                self.head = None
                self.tail = None
            else:
                next_node = current_node.next  # declare the next node of current_node
                while next_node != self.tail:
                    current_node = next_node
                    next_node = next_node.next
                current_node.next = None
                self.tail = current_node  # current_node is the penult node
        else:
            if self.head == self.tail:  # linked list has only one node
                self.head = None
                self.tail = None
            else:
                current_index = 0
                while current_index < index - 1:
                    if current_node.next:
                        current_node = current_node.next  # current_node is the node before node_to_delete
                        current_index += 1
                    else:
                        raise IndexError('delete index out of range')
                else:
                    node_to_delete = current_node.next
                    next_node = node_to_delete.next  # the node after node_to_delete
                    current_node.next = next_node

    def clear(self):
        """ remove all nodes from linked list """
        self.head = self.tail = None


singly_linked_list = SinglyLinkedList()
singly_linked_list.insert(0, 0)
singly_linked_list.insert(2, -1)
singly_linked_list.insert(1, 1)
singly_linked_list.insert(4, 4)
singly_linked_list.insert(3, 3)


# traversal
singly_linked_list.traversal()

print(singly_linked_list)
singly_linked_list.clear()
print(singly_linked_list)
