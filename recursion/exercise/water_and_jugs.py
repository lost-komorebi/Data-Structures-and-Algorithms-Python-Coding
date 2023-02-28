#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   water_and_jugs.py
@Time    :   2023/02/16 19:10:54
@Author  :   komorebi 
'''

"""
Write a program to solve the following problem: 
You have two jugs: a 4-gallon jug and a 3-gallon jug. 
Neither of the jugs have markings on them. 
There is a pump that can be used to fill the jugs with water. 
How can you get exactly two gallons of water in the 4-gallon jug?
reference: https://github.com/bnmnetp/CS160/blob/ad4f47ec083857bc2f328839ceb3f0105b5c4291/08_Recursion/waterjug.rst
"""


class State:
    def __init__(self, capacity1: int, capacity2: int, goal: list) -> None:
        self.state = [0, 0]  # water amount in jug1, water amout in jug2
        self.goal = goal
        self.capacity1 = capacity1
        self.capacity2 = capacity2

    def fill_jug1(self):
        self.state[0] = self.capacity1

    def fill_jug2(self):
        self.state[1] = self.capacity2

    def empty_jug1(self):
        self.state[0] = 0

    def empty_jug2(self):
        self.state[1] = 0

    def pour_jug1_to_jug2(self):
        # the amount of water that jug2 still can add
        jug2_valid_capacity = self.capacity2 - self.state[1]
        if self.state[0] > jug2_valid_capacity:
            self.state[0] = self.state[0] - jug2_valid_capacity
            self.state[1] = self.capacity2
        else:
            self.state[1] = self.state[1] + self.state[0]
            self.state[0] = 0

    def pour_jug2_to_jug1(self):
        # the amount of water that jug1 still can add
        jug1_valid_capacity = self.capacity1 - self.state[0]
        if self.state[1] > jug1_valid_capacity:
            self.state[0] = self.capacity1
            self.state[1] = self.state[1] - jug1_valid_capacity
        else:
            self.state[0] = self.state[0] + self.state[1]
            self.state[1] = 0

    def is_jug1_full(self):
        return self.state[0] == self.capacity1

    def is_jug2_empty(self):
        return self.state[1] == 0

    def __str__(self):
        return f'jug1 water amount {self.state[0]}L, jug2 water amount {self.state[1]}L'

    def search(self):
        if self.goal[0] > max(self.capacity1, self.capacity2):
            return "It's impossible to get {self.goal[0]} L water by jug1 and jug2"
        if self.goal[0] % self.gcd(self.capacity1, self.capacity2) != 0:
            return "It's impossible to get {self.goal[0]} L water by jug1 and jug2"
        else:
            if self.goal[0] == 0:
                return
            if self.goal[0] == self.capacity1: # goal equal to capacity of jug1
                self.fill_jug1()
                print(self)
            while self.state != self.goal:
                if self.is_jug2_empty():
                    self.fill_jug2()
                    print(self)
                if not self.is_jug1_full():
                    self.pour_jug2_to_jug1()
                    print(self)
                if self.is_jug1_full():
                    self.empty_jug1()
                    print(self)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
if __name__ == '__main__':
    start = State(4, 3, [4, 0])
    start.search()
