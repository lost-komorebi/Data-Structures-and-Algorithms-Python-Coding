#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   hash_table.py
@Time    :   2023/02/19 14:16:35
@Author  :   komorebi 
'''


class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None for i in range(11)]
        self.data = [None for i in range(11)]
        self.length = 0

    def put(self, key, value):
        start_slot = self.hash(key)
        position = start_slot
        if self.slots[position] is None:
            self.slots[position] = key
            self.data[position] = value
            self.length += 1
        else:
            while self.slots[position] is not None and self.slots[position] != key:
                position = self.rehash(position)
                if position == start_slot:  # we have finished looping through all slots one time
                    raise Exception('full hash table')
            if self.slots[position] is None:
                self.slots[position] = key
                self.data[position] = value
                self.length += 1
            else:
                # replace old value when self.slots[position] == key
                self.data[position] = value

    def get(self, key):
        start_slot = self.hash(key)
        position = start_slot
        if self.slots[position] == key:
            return self.data[position]
        while self.slots[position] != key:
            position = self.rehash(position)
            if self.slots[position] == key:
                return self.data[position]
            if position == start_slot:  # we have finished looping through all slots one time
                return None

    def __len__(self):
        return self.length

    def delete(self, key):
        start_slot = self.hash(key)
        position = start_slot
        if self.slots[position] == key:
            self.slots[position] = None
            self.data[position] = None
            self.length -= 1
        else:
            while self.slots[position] != key:
                position = self.rehash(position)
                if position == start_slot:  # we have finished looping through all slots one time
                    raise Exception(f"KeyError: '{key}'")
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                self.length -= 1

    def exist(self, key):
        return True if self[key] else False

    def hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self[key] else False


if __name__ == '__main__':
    h = HashTable()
    h[11] = 'cat'
    h[22] = 'dog'
    h[33] = "duck"
    h[44] = "rabbit"
    h[55] = "lion"
    h[66] = "tiger"
    h[77] = "bird"
    h[88] = "cow"
    h[99] = "goat"
    h[110] = "pig"
    h[121] = "chicken"
    print(h.slots, h.data, len(h))
    h[33] = "dolphin"
    h.delete(33)
    print(h.slots, h.data, len(h))
    h[122] = "elephant"
    print(h.slots, h.data, len(h))
    print(11 in h)
