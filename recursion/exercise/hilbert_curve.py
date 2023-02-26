#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   hilbert_curve.py
@Time    :   2023/02/16 16:10:50
@Author  :   komorebi 
'''
from turtle import *


def hilbert_curve(order, t):
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

    # if order > 0:
    #     t.up()
    #     t.goto(-100, 100)
    #     t.down()
    #     t.goto(-100, -100)
    #     t.goto(100, -100)
    #     t.goto(100, 100)
    #     t.left(90)


if __name__ == '__main__':
    t = Turtle()
    my_win = t.getscreen()
    hilbert_curve(1, t)
    my_win.exitonclick()
