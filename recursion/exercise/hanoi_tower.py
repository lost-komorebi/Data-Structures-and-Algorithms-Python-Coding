#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   hanoi_tower.py
@Time    :   2023/02/16 14:53:03
@Author  :   komorebi 
'''

"""
Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.
"""


class Stack:
    def __init__(self, name):
        self.defined_name = name
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def hanoi_tower(n, from_rod, to_rod, mid_rod):
    if n > 0:
        hanoi_tower(n - 1, from_rod, mid_rod, to_rod)
        print(f'move {n} from {from_rod} to {to_rod}')
        hanoi_tower(n - 1, mid_rod, to_rod, from_rod)


def hanoi_tower1(n, from_rod, to_rod, mid_rod):
    """ use stacks to represent towers """
    if n > 0:
        hanoi_tower1(n - 1, from_rod, mid_rod, to_rod)
        disk = from_rod.pop()
        to_rod.push(disk)
        print(
            f'move {disk} from {from_rod.defined_name} to {to_rod.defined_name}')
        print(
            f'after moving, the distribution of each stack: \n\
            {from_rod.defined_name}:{from_rod.items}, {to_rod.defined_name}:{to_rod.items}, {mid_rod.defined_name}:{mid_rod.items}')
        hanoi_tower1(n - 1, mid_rod, to_rod, from_rod)


if __name__ == '__main__':
    from_stack = Stack('a')
    to_stack = Stack('c')
    mid_stack = Stack('b')
    n = 3
    for i in reversed(range(1, n+1)):
        from_stack.push(i)
    hanoi_tower(n, 'a', 'c', 'b')
    print('>>>>>>>')
    hanoi_tower1(n, from_stack, to_stack, mid_stack)
