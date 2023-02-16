#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   fractal_tree.py
@Time    :   2023/02/15 09:37:43
@Author  :   komorebi 
'''

from turtle import *
import random


def tree(length_of_branch, thickness, t):
    if length_of_branch > 5:
        t.speed('fastest')
        t.width(thickness)
        if length_of_branch > 30:
            t.color('brown')
        else:
            t.color('green')
        t.forward(length_of_branch)
        random_angel = random.randint(15, 30)
        random_reduction = random.randint(10, 15)
        t.right(random_angel)
        tree(length_of_branch-random_reduction,
             thickness-random_reduction/5, t)
        t.left(2*random_angel)
        tree(length_of_branch-random_reduction,
             thickness-random_reduction/5, t)
        t.right(random_angel)
        if length_of_branch > 30:
            t.color('brown')
        else:
            t.color('green')
        t.backward(length_of_branch)


t = Turtle()
my_win = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
tree(110, 22, t)
my_win.exitonclick()
