#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   sierpinski_triangle.py
@Time    :   2023/02/15 10:12:49
@Author  :   komorebi 
'''

from turtle import *


def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color) # choose the color for filling the shape
    my_turtle.up()
    my_turtle.goto(points[0])
    my_turtle.down()
    my_turtle.begin_fill()
    # draw a closed geographical objects 
    my_turtle.goto(points[1])
    my_turtle.goto(points[2])
    my_turtle.goto(points[0])
    my_turtle.end_fill()


def get_mid(p1, p2):
    """ get middle point """
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


def sierpinski(points, degree, my_turtle):
    """ points: 3 vertices of the triangle """
    color_map = ['blue', 'red', 'green',
                 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree - 1, my_turtle
                   )
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   degree - 1, my_turtle
                   )
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   degree - 1, my_turtle
                   )


my_turtle = Turtle()
my_win = my_turtle.getscreen()
my_points = [(-300, -150), (0, 300), (300, -150)]
sierpinski(my_points, 4, my_turtle)
my_win.exitonclick()
