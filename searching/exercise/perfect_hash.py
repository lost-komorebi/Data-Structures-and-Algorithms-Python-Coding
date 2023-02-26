#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   perfect_hash.py
@Time    :   2023/02/23 09:04:16
@Author  :   komorebi 
'''

"""
Problem-Solving-with-Algorithms-and-Data-Structures-Using-Python-SECOND-EDITION
5.6 Discussion Questions
4. Research perfect hash functions. 
Using a list of names (classmates, family members, etc.), 
generate the hash values using the perfect hash algorithm.
reference: 
Cichelli’s Method
https://courses.cs.vt.edu/~cs3114/Fall10/Notes/T17.PerfectHashFunctions.pdf
"""




from collections import Counter
class Cichelli:
    def __init__(self, li: list, g_max: int) -> None:
        self.li = li
        self.g_max = g_max
        self.hash_table = {}  # init a dic as a hash table

    def sort_by_letter_frequency(self):
        # Determine the frequency with which each first and last letter occurs
        letters = ''
        for i in self.li:
            letters += i[0]
            letters += i[-1]
        # Score the words by summing the frequencies of their first and
        # last letters, and then sort them in that order:
        self.li.sort(key=lambda x: Counter(letters)[
            x[0]]+Counter(letters)[x[-1]], reverse=True)

    def hash(self):
        for i in range(len(self.li)):
            self.hash1(self.li[i])
        while len(self.hash_table) != self.li:
            self.rehash()

    def hash1(self, word, g_first=0, g_last=0):
        while g_first < self.g_max or g_last < self.g_max:
            hash_value = (len(word) + g_first + g_last) % len(self.li)
            print(word, hash_value, g_first, g_last)
            if not self.hash_table.get(hash_value):
                self.hash_table[hash_value] = word
                break  # already found temporary perfect hash for current word
            else:
                if g_first < g_max:  # increase weight for first letter first
                    g_first += 1
                else:  # increase weight for last letter
                    g_last += 1

    def rehash(self, last_hashed_index=None):
        if not last_hashed_index:
            last_hashed_index = len(self.hash_table) - 1
            last_hashed_word = self.li[last_hashed_index]
            print(last_hashed_word)
            print(self.hash1(last_hashed_word, g_first=1))
        # if len(self.hash_table) != len(self.li):  # not all words has been hashed
        #     print(self.li[len(self.hash_table)-1])
        #     last_hashed_word = self.li[len(self.hash_table)-1]
        #     print(self.hash1(last_hashed_word, g_first=1))
        #     print(self.hash_table)


if __name__ == "__main__":
    g_max = 4  # start from 0
    # strings = ['calliope', 'clio', 'erato', 'euterpe', 'melpomene',
    #            'polyhymnia', 'terpsichore', 'thalia', 'urania']
    strings = ['abc', 'adc', 'aec', 'afc', 'ahc',
               'aic', 'ajc', 'akc', 'alc']
    c = Cichelli(strings, g_max)
    c.hash()
