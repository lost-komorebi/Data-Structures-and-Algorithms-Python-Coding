#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for ele in nodes:
                temp_node = Node(data=ele)
                node.next = temp_node
                temp_node.previous = node
                node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        return ' <-> '.join(nodes) + ' -> None' if self.head else 'None'

    def add_last(self, node):
        """ similar function as list.append() """
        if self.head is None:  # set node as head if the linked list is empty
            self.head = node
            return
        for current_node in self:  # after looping, current_node is the last node
            pass
        current_node.next = node
        node.previous = current_node

    def add_first(self, node):
        """ add a node as the first node """
        if self.head is None:  # set node as head if the linked list is empty
            self.head = node
            return
        node.next = self.head
        self.head.previous = node
        self.head = node

    def remove_node(self, target_node_data):
        """ remove target_node_data from linked list"""
        if self.head is None:
            raise Exception('delete from empty linked list')
        if self.head.data == target_node_data:
            self.head = self.head.next
            self.head.previous = None
            return
        else:
            previous_node = self.head
            for node in self:
                if node.data == target_node_data:
                    previous_node.next = node.next
                    if node.next is not None:  # node is not the last node of the linked list
                        node.next.previous = previous_node  # repoint the next node to previous node
                    return
                previous_node = node
        raise Exception(f'{target_node_data} not in linked list')

    def insert(self, index, new_node):
        """ insert new_node into to the linked list by specific index"""
        current_node = self.head
        current_index = 0
        if index == 0 or current_node is None:  # empty linked list
            return self.add_first(new_node)
        while current_node:
            if current_index == index:  # current_node is the node at the specific index
                current_node.previous.next = new_node
                new_node.next = current_node
                new_node.previous = current_node.previous
                current_node.previous = new_node
                return
            current_node = current_node.next
            current_index += 1
        return self.add_last(new_node)

    def clear(self):
        """ delete all nodes of linked list """
        self.head = None


ll = DoublyLinkedList()
ll.add_last(Node('b'))
ll.add_last(Node('c'))
ll.add_last(Node('d'))
ll.add_first(Node('a'))
print(ll)
for i in ll:
    print(i, i.next, i.previous)
ll.insert(1, Node('d'))
print(ll)
for i in ll:
    print(i, i.next, i.previous)
