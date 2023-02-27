#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   hash_table.py
@Time    :   2023/02/19 14:16:35
@Author  :   komorebi 
'''
import random

class HashTable:

    def __init__(self, size:int=11):
        self.size = size
        self.slots = [None for i in range(self.size)]
        self.data = [None for i in range(self.size)]
        self.length = 0

    # def put(self, key, value):
    #     """ old function without resize """
    #     start_slot = self.hash(key)
    #     position = start_slot
    #     if self.slots[position] is None:
    #         self.slots[position] = key
    #         self.data[position] = value
    #         self.length += 1
    #     else:
    #         while self.slots[position] is not None and self.slots[position] != key:
    #             position = self.rehash(position)
    #             if position == start_slot:  # we have finished looping through all slots one time
    #                 raise Exception('full hash table')
    #         if self.slots[position] is None:
    #             self.slots[position] = key
    #             self.data[position] = value
    #             self.length += 1
    #         else:
    #             # replace old value when self.slots[position] == key
    #             self.data[position] = value

    def put(self, key, value):
        #print(key, value, self.slots, self.data)
        """ put key-value pair into hash table """
        hash_value = self.hash(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
            self.length += 1
        else:
            if self.slots[hash_value] == key:  # key is equal, but value is not equal, update value
                if self.data[hash_value] != value:
                    self.data[hash_value] = value
            else:
                time = 0 
                rehash_value = self.quadratic_rehash(hash_value, time)
                start_position = rehash_value
                # recursive call to find a available position to put
                while self.slots[rehash_value] != None and self.slots[rehash_value] != key:
                    time += 1
                    rehash_value = self.quadratic_rehash(rehash_value, time)
                    # loop to the first slot, it means cannot find a empty slot for current key, 
                    # so resize hash table
                    if rehash_value == start_position: 
                        self.resize()
                # after recursive call, one circumstance is to find a empty slot
                if self.slots[rehash_value] is None:
                    self.slots[rehash_value] = key
                    self.data[rehash_value] = value
                    self.length += 1
                else:  # another circumstance is find a non empty slot, but need to update value
                    self.data[rehash_value] = value
        # when the load factor reaches 0.7, resize the hash table
        if self.get_load_factor() >= 0.7:
            self.resize()

    def resize(self):
        # remove empty slots
        old_slots = [_ for _ in self.slots if _ is not None]
        old_data = [_ for _ in self.data if _ is not None]
        self.size *= 3  # magnify the size
        self.slots = [None for i in range(self.size)]
        self.data = [None for i in range(self.size)]
        self.length = 0
        # loop throught old date to reput
        for key, value in zip(old_slots, old_data):
            self.put(key, value)
        


    def get(self, key):
        hash_value = self.hash(key)
        if self.slots[hash_value] == key:
            return self.data[hash_value]
        time = 0
        rehash_value = self.quadratic_rehash(hash_value, time)
        position = rehash_value
        while self.slots[rehash_value] != key:
            time += 1
            rehash_value = self.quadratic_rehash(rehash_value, time)
            # loop to the first slot, it means cannot find the key in hash table 
            if rehash_value == position:  # we have finished looping through all slots one time
                return None
        if self.slots[rehash_value] == key:
                return self.data[rehash_value]

    def __len__(self):
        return self.length

    def delete(self, key):
        hash_value = self.hash(key)
        if self.slots[hash_value] == key:
            self.slots[hash_value] = None
            self.data[hash_value] = None
            self.length -= 1
        else:
            time = 0
            rehash_value = self.quadratic_rehash(hash_value, time)
            position = rehash_value
            while self.slots[rehash_value] != key:
                time += 1
                rehash_value = self.quadratic_rehash(rehash_value, time)
                # loop to the first slot, it means cannot find the key in hash table 
                if rehash_value == position:  # we have finished looping through all slots one time
                    raise Exception(f"KeyError: '{key}'")
            if self.slots[rehash_value] == key:
                self.slots[rehash_value] = None
                self.data[rehash_value] = None
                self.length -= 1
        
    def get_load_factor(self):
        return self.length / self.size

    def exist(self, key):
        return True if self[key] else False

    def hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        """ linear probing """
        return (old_hash + 1) % self.size
    
    def quadratic_rehash(self, old_hash, time):
        """ quadratic probing """
        return (old_hash + time**2) % self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self[key] else False
    
    def __delitem__(self, key):
        self.delete(key)


if __name__ == '__main__':
    my_ht = HashTable()
    dic = {}
    for i in range(0,100,11):
        value = random.uniform(0,1)
        my_ht[i] = value
        dic[i] = value
    print(my_ht.slots)
    print(my_ht.data)
    print(dic)
    for i in dic:
        if my_ht[i] != dic[i]:
            print(i,my_ht[i],dic[i])
    for i in dic:
        del my_ht[i]
    print(my_ht.slots)
    print(my_ht.data)
    print(len(my_ht))