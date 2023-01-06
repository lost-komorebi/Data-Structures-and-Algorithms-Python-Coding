#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" using linked list to perform a queue """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def __repr__(self):
        return ' -> '.join([str(i.data) for i in self])


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __repr__(self):
        return ' '.join([str(i.data) for i in self.linked_list])

    def en_queue(self, data):
        if self.is_empty():
            self.linked_list.head = Node(data)
            self.linked_list.tail = self.linked_list.head
        else:
            node = self.linked_list.tail
            node.next = Node(data)
            self.linked_list.tail = node.next

    def de_queue(self):
        if self.is_empty():
            raise Exception('empty queue')
        node = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:  # remove the last node
            self.linked_list.head = None
            self.linked_list.tail = None
        else:
            self.linked_list.head = self.linked_list.head.next
        return node.data

    def peek(self):
        if self.is_empty():
            raise Exception('empty queue')
        return self.linked_list.head.data

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        return False

    def clear(self):
        self.linked_list.head = None
        self.linked_list.tail = None


if __name__ == '__main__':
    my_q = Queue()
    print(my_q.linked_list)
    print(my_q.is_empty())
    my_q.en_queue(1)
    my_q.en_queue(2)
    my_q.en_queue(3)

    print(my_q.de_queue())
    print(my_q.de_queue())
    print(my_q.de_queue())
    print(my_q.linked_list, my_q.linked_list.head, my_q.linked_list.tail)
    #print(my_q.peek())
