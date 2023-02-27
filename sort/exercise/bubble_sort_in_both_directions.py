#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   bubble_sort_simultaneous.py
@Time    :   2023/02/27 13:53:39
@Author  :   komorebi 
'''

"""
A bubble sort can be modified to “bubble” in both directions. 
The first pass moves “up” the list, and the second pass moves “down.” 
This alternating pattern continues until no more passes are necessary. 
Implement this variation .
"""
import random
def bubble_sort(li:list) -> None:
    """
    sort from two directions
    from left to right to find the largest number during first loop duration
    then the second largest 
    from right to left to find the smallest number during first loop duration
    then the second smallest
    until the list is sorted, stop looping  
    """
    for i in range(len(li) - 1):
        need_swap = False
        for j in range(len(li) - 1 - i): # start from left
            if li[j] > li[j+1]:  # if current value > next right value, swap them
                need_swap = True
                li[j], li[j+1] = li[j+1], li[j]
        print('up',li)
        need_swap = False
        for x in range(len(li) - 2 - i, 0 , -1): # start from right
            if li[x] < li[x-1]: # if current value < next left value, swap them
                need_swap = True
                li[x-1], li[x] = li[x], li[x-1]
        print('down',li)
        if need_swap == False:  # list is sorted
            break

if __name__ == '__main__':
    li = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(li)
    print(li)
    bubble_sort(li)
    print(li)