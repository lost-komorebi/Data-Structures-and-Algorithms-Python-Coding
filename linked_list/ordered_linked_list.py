#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class OrderedLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(str(cur.get_value()))
            cur = cur.get_next()
        return ' -> '.join(nodes)

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.get_next()

    def add(self, value):
        temp = Node(value)
        cur = self.head
        prev = None
        while cur:
            if cur.get_value() > value:
                break
            prev = cur
            cur = cur.get_next()
        if prev is None:
            if cur is None:  # linked list has no node
                self.head = temp
                self.tail = temp
            else:  # linked list has only one node
                temp.set_next(self.head)
                self.head = temp
        else:
            prev.set_next(temp)
            temp.set_next(cur)
            if cur is None:  # cur is None, it means cur is the last node, so we need to point tail to it
                self.tail = temp
        self.length += 1

    def remove(self, value):
        # empty linked list
        if self.is_empty():
            raise Exception('empty in linked list')
        # value > tha largest value in current linked list
        if self.tail.get_value() < value:
            raise Exception(f'{value} not in linked list')
        cur = self.head
        prev = None
        found = False
        while not found and cur is not None:
            if cur.get_value() == value:
                found = True
            else:
                if cur.get_value() > value:
                    return Exception(f' {value} not in linked list')
                else:
                    prev = cur
                    cur = cur.next
        if prev is None:
            if self.head == self.tail:  # linked list has only one node
                self.head = self.tail = None
            else:  # delete self.head
                self.head = cur.get_next()
        else:
            prev.set_next(cur.get_next())
            if prev.get_next() is None:  # repoint tail
                self.tail = prev
        self.length -= 1

    def search(self, value):
        for node in self:
            if node.value == value:
                return node
            if node.value > value:
                return
        return

    def is_empty(self):
        return self.head is None

    def index(self, value):
        node_index = 0
        for node in self:
            if node.value == value:
                return node_index
            if node.value > value:
                return
            node_index += 1

    def pop(self, index=None):
        # empty linked list
        if self.is_empty():
            raise Exception('empty in linked list')
        if index is not None:
            if index < -len(self) or index > len(self) - 1:
                raise Exception('Invalid index')
            if index < 0:  # convert negative index to positive index
                index = index + len(self)
            # index = None, pop last
            cur = self.head
            prev = None
            current_index = 0
            while current_index != index and cur is not None:
                prev = cur
                cur = cur.next
                current_index += 1
            if prev is None:
                if self.tail == self.head:  # linked list has only one node
                    self.head = self.tail = None
                else:  # parameter index  = 0
                    self.head = cur.get_next()
            else:
                prev.set_next(cur.get_next())
                if prev.get_next() is None:
                    self.tail = prev
        else:  # index is None, pop last node
            cur = self.head
            prev = None
            while self.tail != cur and cur is not None:
                prev = cur
                cur = cur.next
            if prev is None:
                if self.tail == self.head:  # linked list has only one node
                    self.head = self.tail = None
                else:  # parameter index  = 0
                    self.head = cur.get_next()
            else:  # cur is tail
                prev.set_next(cur.get_next())
                self.tail = prev
        self.length -= 1


if __name__ == '__main__':
    li = [0, -1, 3, 2, 5, 4, 6, 9, 7, 1, -2, 8, -3, -5]
    my_ll = OrderedLinkedList()

    for i in li:
        my_ll.add(i)

    for i in li:
        assert my_ll.search(i).value == i
        assert my_ll.index(i) == sorted(li).index(i)
    for i in sorted(li):
        assert my_ll.search(i).value == i
