#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   priority_queue.py
@Time    :   2023/03/11 11:10:39
@Author  :   komorebi 
'''

"""
Using the BinaryHeap class, implement a new class called PriorityQueue. 
Your PriorityQueue class should implement the constructor, plus the enqueue and dequeue methods.
"""
from max_heap import MaxHeap
class PriorityQueue(MaxHeap):
    def __init__(self) -> None:
        self.q = MaxHeap()

    def enqueue(self, value):
        self.q.insert(value) 

    def dequeue(self):
        return self.q.del_max() 


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(1)
    pq.enqueue(2)
    pq.enqueue(3)
    pq.enqueue(4)
    pq.enqueue(5)
    print(pq.dequeue())

