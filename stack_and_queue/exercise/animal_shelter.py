#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Node:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.next = None

    def __repr__(self):
        return f'{self.name}:{self:animal_type}'


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
        return ' -> '.join(f'{i.name}:{i.animal_type}' for i in self)


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __repr__(self):
        return ' '.join(f'{i.name}:{i.animal_type}' for i in self.linked_list)

    def en_queue(self, name, animal_type):
        if self.is_empty():
            self.linked_list.head = Node(name, animal_type)
            self.linked_list.tail = self.linked_list.head
        else:
            node = self.linked_list.tail
            node.next = Node(name, animal_type)
            self.linked_list.tail = node.next

    def de_queue_any(self):
        """ remove the first node from queue """
        if self.is_empty():
            raise Exception('empty queue')
        node = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:  # the queue has only one node
            self.clear()
        else:
            self.linked_list.head = self.linked_list.head.next
        return f'{node.name}:{node.animal_type}'

    def de_queue_type(self, animal_type):
        """ remove the first specific node from queue """
        if self.is_empty():
            raise Exception('empty queue')
        node = self.linked_list.head
        if node.animal_type == animal_type:  # head of queue
            if node == self.linked_list.tail:  # the queue only has one node
                self.clear()
                return f'{node.name}:{node.animal_type}'
            self.linked_list.head = node.next  # point head to next node
            return f'{node.name}:{node.animal_type}'
        while node.next:
            next_node = node.next
            if node.next.animal_type == animal_type:
                if node.next == self.linked_list.tail:
                    self.linked_list.tail = node
                node.next = next_node.next
                return f'{next_node.name}:{next_node.animal_type}'
            node = node.next
        raise Exception(f"This queue has no '{animal_type}'")

    def de_queue_dog(self):
        self.de_queue_type('dog')

    def de_queue_cat(self):
        self.de_queue_type('cat')

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        return False

    def clear(self):
        self.linked_list.head = self.linked_list.tail = None


my_q = Queue()

my_q.en_queue('dami', 'cat')
my_q.en_queue('ermi', 'cat')
my_q.en_queue('wangcai', 'dog')
my_q.en_queue('laifu', 'dog')
print(my_q)
print(my_q.de_queue_any())
print(my_q)
print(my_q.de_queue_cat())
my_q.de_queue_cat()
print(my_q)
