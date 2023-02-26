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
    def __init__(self, amount1, amount2) -> None:
        # amount1 is the water amount in jug which capacity is 4
        # amount2 is the water amount in jug which capacity is 3
        self.state = [amount1, amount2]

    def fill_jug1(self):
        self.state[0] = 4

    def fill_jug2(self):
        self.state[1] = 3

    def empty_jug1(self):
        self.state[0] = 0

    def empty_jug2(self):
        self.state[1] = 0

    def pour_jug1_to_jug2(self):
        # the amount of water that jug2 still can add
        jug2_valid_capacity = 3 - self.state[1]
        if self.state[0] > jug2_valid_capacity:
            self.state[0] = self.state[0] - jug2_valid_capacity
            self.state[1] = 3
        else:
            self.state[1] = self.state[1] + self.state[0]
            self.state[0] = 0

    def pour_jug2_to_jug1(self):
        # the amount of water that jug1 still can add
        jug1_valid_capacity = 4 - self.state[0]
        if self.state[1] > jug1_valid_capacity:
            self.state[0] = 4
            self.state[1] = self.state[1] - jug1_valid_capacity
        else:
            self.state[0] = self.state[0] + self.state[1]
            self.state[1] = 0

    def __eq__(self, __o: object) -> bool:
        return self.state[0] == __o.state[0] and self.state[1] == __o.state[1]

    def search(self, start, goal, moves):
        print(start.state)
        if start.state[0] == 2:
            return
        else:
            (self.fill_jug1 or self.fill_jug2 or self.empty_jug1 or self.empty_jug2 or self.pour_jug1_to_jug2 or self.pour_jug2_to_jug1)
            self.search(start, goal, moves)
        # elif start.state[0] == 0:
        #     self.fill_jug1()
        #     print('fill_jug1')
        #     self.search(start, goal, moves)
        # elif start.state[1] == 0:
        #     self.fill_jug2()
        #     print('fill_jug2')
        #     self.search(start, goal, moves)
        # elif start.state[1] == 3:
        #     self.pour_jug2_to_jug1()
        #     print('pour_jug2_to_jug1')
        #     self.search(start, goal, moves)
        # elif start.state[0] == 4:
        #     self.empty_jug1()
        #     print('empty_jug1')
        #     self.search(start, goal, moves)

        # elif start.state[0] > 0:
        #     self.pour_jug1_to_jug2()
        #     print('pour_jug1_to_jug2')
        #     self.search(start, goal, moves)
        # elif start.state[1] > 0:
        #     self.pour_jug2_to_jug1()
        #     print('fuck pour_jug2_to_jug1')
        #     self.search(start, goal, moves)


if __name__ == '__main__':
    start = State(0, 0)
    goal = State(2, 0)
    moves = []
    start.search(start, goal, moves)
