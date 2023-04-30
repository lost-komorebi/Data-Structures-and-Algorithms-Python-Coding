#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   timsort.py
@Time    :   2023/04/30 22:56:45
@Author  :   komorebi 
'''
"""
Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort.

Timsort was designed to take advantage of runs of consecutive ordered elements that already exist in most real-world data, 
natural runs. It iterates over the data collecting elements into runs and simultaneously putting those runs in a stack. 
Whenever the runs on the top of the stack match a merge criterion, they are merged. 
This goes on until all data is traversed; then, all runs are merged two at a time and only one sorted run remains. 
The advantage of merging ordered runs instead of merging fixed size sub-lists (as done by traditional mergesort) 
is that it decreases the total number of comparisons needed to sort the entire list.

Each run has a minimum size, which is based on the size of the input and is defined at the start of the algorithm. 
If a run is smaller than this minimum run size, insertion sort is used to add more elements to the run until the minimum run size is reached.
"""




from random import randint
def timsort(li: list) -> list:
    minrun = 32
    n = len(li)

    # insertion sort for small runs
    for i in range(0, n, minrun):
        insertion_sort(li, i, min((i + minrun - 1), n - 1))
    # merge sort for sorted runs
    size = minrun
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(li, start, mid + 1, end + 1)
        size *= 2


def insertion_sort(li: list, start: int = 0, end: int = None) -> None:
    if end is None:
        end = len(li) - 1
    for i in range(start + 1, end + 1):
        key = li[i]
        while i > start and key < li[i-1]:
            li[i] = li[i - 1]
            i -= 1
        li[i] = key


def merge(li: list, start: int, mid: int, end: int) -> None:
    # if left or right is None, just return
    # because another side is already ordered, we don't need to merge anymore
    if start > mid or mid > end:
        return
    # initiate i and j to the start of left and right sublists respectively
    i, j = start, mid

    result = []

    while i < mid and j < end:
        # compare elements of left and right sublists, and appends smaller element to reult
        if li[i] < li[j]:
            result.append(li[i])
            i += 1
        else:
            result.append(li[j])
            j += 1

    # adds any remaining element in the left sublist append to result
    while i < mid:
        result.append(li[i])
        i += 1
    # adds any remaining element in the right sublist append to result
    while j < end:
        result.append(li[j])
        j += 1
    # replace slice of li between 'start' and 'end' with sorted result
    li[start:end] = result


if __name__ == "__main__":
    li = [15, 87, 111, 4, 43, 56, 3, 222, 48, 87, 11]
    timsort(li)
    assert li == [3, 4, 11, 15, 43, 48, 56, 87, 87, 111, 222]
    li = [randint(0, 1000) for i in range(randint(0, 100))]
    timsort(li)
    assert li == sorted(li)
