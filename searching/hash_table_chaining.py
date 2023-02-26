#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   hash_table_chaining.py
@Time    :   2023/02/26 13:55:45
@Author  :   komorebi 
'''


"""
Implement a hash table with chaining collision resolution
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class UnorderedLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def __repr__(self) -> str:
        result = []
        for node in self:
            result.append(f'< {node.key}: {node.value} >')
        return ' -> '.join(result)

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def add(self, key, value):
        temp = Node(key, value)
        if not self.head:
            self.head = self.tail = temp
            self.length += 1
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = temp
        temp.prev = cur
        self.tail = temp
        self.length += 1

    def search(self, key):
        for node in self:
            if node.key == key:
                return node

    def remove(self, key):
        if self.is_empty():
            raise Exception('remove from empty linked list')
        for node in self:
            if node.key == key:
                if node == self.head:  # delete first node
                    if node != self.tail:
                        self.head = node.next
                        node.next.prev = None
                    else:  # linked list has only one node
                        self.head = self.tail = None
                elif node == self.tail:  # delete last node
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                self.length -= 1
                return
        raise Exception(f'{key} not in linked list')

    def is_empty(self):
        return self.length == 0

class HashTable:
    def __init__(self) -> None:
        self.size = 5
        self.data = [UnorderedLinkedList() for _ in range(self.size)]
        self.length = 0

    def put(self, key, data):
        # calculate index
        index = self.hash(key)
        # current index is empty, we just need to add key-value pair
        if self.data[index].is_empty():
            self.data[index].add(key, data)
            self.length += 1         
        else: # current index is not empty
            node = self.data[index].search(key)  
            if not node: # key is not in linked list
                self.data[index].add(key, data) # add key-value pair
                self.length += 1
                return
            # key in linked list, but value is different, so update value
            if node.value != data:  
                node.value = data

    def get(self, key):
        index = self.hash(key)
        if self.data[index].is_empty():
            return 
        else:
            node = self.data[index].search(key)
            if node:
                return node.value
             
    def delete(self, key):
        # calculate index
        index = self.hash(key)
        # current index is empty, raise error 
        if self.data[index].is_empty():
            raise Exception(f'{key} is not in hash table')    
        else: # current index is not empty
            node = self.data[index].search(key)  
            if not node:
                raise Exception(f'{key} is not in hash table')
            else:
                self.data[index].remove(key)
                self.length -= 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self[key] else False

    def __len__(self):
        return self.length

    def __delitem__(self, key):
        self.delete(key)

    def hash(self, key):
        """ calculate the index of current key-value pair in hash table """
        return key % self.size

if __name__ == '__main__':  
    my_ht = HashTable()
    my_ht[10] = 'cat'
    my_ht[11] = 'dog'
    my_ht[12] = "duck"
    my_ht[13] = "rabbit"
    my_ht[14] = "lion"
    my_ht[15] = "tiger"
    my_ht[16] = "bird"
    my_ht[17] = "cow"
    my_ht[18] = "goat"
    my_ht[19] = "pig"
    my_ht[20] = "chicken"
    for i in my_ht.data:
        print(i)
    print(my_ht[10], my_ht[19])
    my_ht[10] = 'lucky'
    del my_ht[19]
    print(my_ht[10], my_ht[19])