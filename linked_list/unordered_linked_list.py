#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

    def get_prev(self):
        return self.prev

    def set_prev(self, new_node):
        self.prev = new_node


class UnorderedLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        result = []
        for node in self:
            result.append(str(node.value))
        return ' -> '.join(result)

    def add(self, value):
        temp = Node(value)
        if not self.head:
            self.head = self.tail = temp
            self.length += 1
            return
        cur = self.head
        while cur.next:
            cur = cur.get_next()
        cur.set_next(temp)
        temp.set_prev(cur)
        self.tail = temp
        self.length += 1

    def search(self, value):
        for node in self:
            if node.value == value:
                return node

    def remove(self, value):
        if self.is_empty():
            raise Exception('remove from empty linked list')
        for node in self:
            if node.value == value:
                if node == self.head:  # delete first node
                    if node != self.tail:
                        self.head = node.get_next()
                        node.get_next().set_prev(None)
                    else:  # linked list has only one node
                        self.head = self.tail = None
                elif node == self.tail:  # delete last node
                    self.tail = node.get_prev()
                    node.get_prev().set_next(None)
                else:
                    node.get_prev().set_next(node.get_next())
                    node.get_next().set_prev(node.get_prev())
                self.length -= 1
                return
        raise Exception(f'{value} not in linked list')

    def pop(self, index=None):
        if self.is_empty():
            raise Exception('remove from empty linked list')
        if index is not None:
            if index < -len(self) or index > len(self) - 1:
                raise Exception('Invalid index')
            if index < 0:  # convert negative index to positive index
                index = index + len(self)
        if index is None:
            index = len(self) - 1
        idx = 0
        for node in self:
            if idx == index:
                if node == self.head:  # delete first node
                    if node != self.tail:
                        self.head = node.get_next()
                        node.get_next().set_prev(None)
                    else:  # linked list has only one node
                        self.head = self.tail = None
                elif node == self.tail:  # delete last node
                    self.tail = node.get_prev()
                    node.get_prev().set_next(None)
                else:
                    node.get_prev().set_next(node.get_next())
                    node.get_next().set_prev(node.get_prev())
                self.length -= 1
                return
            idx += 1

    def is_empty(self):
        return self.length == 0

    def index(self, value):
        idx = 0
        for node in self:
            if node.value == value:
                return idx
            idx += 1

    def slice(self, start, end):
        if start < 0:
            start = start + len(self)
        if end < 0:
            end = end + len(self)
        if start > len(self) or start > end:
            return
        print(start, end)
        new_linked_list = UnorderedLinkedList()
        idx = 0
        for node in self:
            print(idx)
            if idx == start or start < idx < end:
                new_linked_list.add(node.get_value())
            if idx >= end:
                break
            idx += 1

        return new_linked_list


if __name__ == '__main__':
    li = [0, -1, 3, 2, 5, 4, 6, 9, 0, 7, 1, -2, 8, -3, -5]
    my_ll = UnorderedLinkedList()

    for i in li:
        my_ll.add(i)
        assert my_ll.search(i)
    print(my_ll.slice(-7, -5))
