#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data


class CircularDoublyLinkedList:
    def __init__(self, nodes: list = None):
        self.head = None
        self.tail = None
        if nodes is not None:
            self.head = Node(data=nodes.pop(0))
            node = self.head
            for ele in nodes:
                temp_node = Node(data=ele)
                node.next = temp_node
                temp_node.prev = node
                node = node.next
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail:
                break
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        if self.head is None:
            return 'None'
        return ' <-> '.join(nodes)

    def clear(self):
        """ remove all nodes from linked list """
        self.head = None

    def remove_node(self, node_data):
        """ remove specific node from linked list """
        if self.head is None:
            raise Exception('Remove node from empty linked list')
        current_node = self.head
        while current_node:
            if current_node.data == node_data:
                if current_node == self.head:  # reset head
                    if current_node == self.tail:  # this linked list has only one node
                        self.head = self.tail = None
                        return
                    self.head = self.head.next
                elif current_node == self.tail:  # reset tail
                    self.tail = self.tail.prev
                prev_node = current_node.prev
                next_node = current_node.next
                next_node.prev = prev_node
                prev_node.next = next_node
                return
            if current_node == self.tail:  # finish loop
                break
            current_node = current_node.next
        raise Exception(f'{node_data} is not in linked list')

    def add_first(self, node):
        """ add new node as head """
        if self.head is None:  # empty linked list
            self.head = self.tail = node
            self.head.prev = self.head.next = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = self.tail
            self.tail.next = self.head

    def add_last(self, node):
        """ add new node as tail """
        if self.head is None:  # empty linked list
            self.head = self.tail = node
            self.head.prev = self.head.next = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail

    def insert_node(self, node, index):
        if index == 0:
            return self.add_first(node)
        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index:
                prev_node = current_node.prev
                prev_node.next = node
                node.prev = prev_node
                node.next = current_node
                current_node.prev = node
                return
            if current_node == self.tail:  # end loop
                return self.add_last(node)
            current_node = current_node.next
            current_index += 1


ll = CircularDoublyLinkedList(['a', 'b', 'c', 'd'])
print(ll, 'head:', ll.head, 'tail:', ll.tail)
for i in ll:
    print(i, 'prev:', i.prev, 'next,', i.next)
print('>>>>>>>>>>>>>>>>>')
ll.insert_node(Node('e'), 3)
print(ll, 'head:', ll.head, 'tail:', ll.tail)
for i in ll:
    print(i, 'prev:', i.prev, 'next,', i.next)
