#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   in_place_heap_sort.py
@Time    :   2023/04/30 23:11:10
@Author  :   komorebi 
'''


""" 
use in place max heap to sort list in ascending order 
in this code snippet, index starts from 0, 
so index of left child is 2 * parent + 1 and index of right child is 2 * parent + 2
1. first, we use a list as input and start heapifying from the last parent, thus allowing us to 
establish a max heap
2. then we reduce the size by one and swap the first element and last element, hence the biggest
element is at the last postion
3. re-heapify the heap, and repeat step 2 until there is no more element in the heap
"""




from random import randint
def heapsort_inplace(li: list) -> None:
    # heapify the input list
    size = len(li)  # size of heap
    heapify(li, size)

    # swapping last and first elements
    # re-heapify the unsorted portion of the list after each extraction
    while size > 1:
        size -= 1
        li[0], li[size] = li[size], li[0]
        percolate_down(li, 0, size)


def heapify(li: list, size: int) -> None:
    # start at the last parent node and percolate down to establish the heap
    for i in range((size - 2) // 2, -1, -1):
        percolate_down(li, i, size)


def percolate_down(li: list, i: int, size: int) -> None:
    max_index = i
    # index starts from 0
    left = 2 * i + 1
    right = 2 * i + 2

    # find the larger child
    if left < size and li[left] > li[max_index]:
        max_index = left
    if right < size and li[right] > li[max_index]:
        max_index = right

    # swap current node with the larger child, if needed
    if max_index != i:
        li[i], li[max_index] = li[max_index], li[i]
        percolate_down(li, max_index, size)


if __name__ == "__main__":
    li = [15, 87, 4, 111, 43, 56, 3, 222, 48, 87, 11]
    heapsort_inplace(li)
    assert li == sorted(li)
    li = [randint(0, 1000) for i in range(randint(0, 100))]
    heapsort_inplace(li)
    assert li == sorted(li)
