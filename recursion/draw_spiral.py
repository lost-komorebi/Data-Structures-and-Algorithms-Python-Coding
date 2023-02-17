#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   draw_spiral.py
@Time    :   2023/02/14 21:38:42
@Author  :   komorebi 
'''


from turtle import *

my_turtle = Turtle()  # init a turtle object
my_win = my_turtle.getscreen()  # init window


def draw_spiral(my_turtle, length_of_line):
    if length_of_line > 0:
        my_turtle.forward(length_of_line)
        my_turtle.right(90)
        draw_spiral(my_turtle, length_of_line-5)


def draw_spiral1(my_turtle, length_of_line):
    while length_of_line > 0:
        my_turtle.forward(length_of_line)
        my_turtle.right(90)
        length_of_line -= 5


draw_spiral(my_turtle, 100)
draw_spiral1(my_turtle, 100)
my_win.exitonclick()
