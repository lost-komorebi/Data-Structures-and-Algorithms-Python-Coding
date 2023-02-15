#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   fractal_tree.py
@Time    :   2023/02/15 09:37:43
@Author  :   komorebi 
'''

from turtle import *

def tree(length_of_branch, t):
    if length_of_branch > 5:
        t.forward(length_of_branch)
        t.right(20)
        tree(length_of_branch-15, t)
        t.left(40)
        tree(length_of_branch-10, t)
        t.right(20)
        t.backward(length_of_branch)



t = Turtle()
my_win = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110, t)
my_win.exitonclick()
