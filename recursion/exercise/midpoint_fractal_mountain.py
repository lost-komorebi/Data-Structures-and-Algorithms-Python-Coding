#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :    midpoint_fractal_mountain.py
@Time    :   2023/02/15 11:18:36
@Author  :   komorebi 
'''
"""
Find or invent an algorithm for drawing a fractal mountain. 
Given two x points, using a recursive function to find mid point, keep doing like.
Each x coordinate we need to pick a random y coordinate.
"""




from turtle import *
from random import uniform
def get_mid(point1, point2):
    return (point1 + point2) / 2


def get_all_xpoints(xpoints, order):
    """ calculate all xpoints according to given start and end """
    if order > 0:
        new_points = []
        xpoints = get_all_xpoints(xpoints, order-1)
        for i in range(len(xpoints) - 1):
            mid = get_mid(xpoints[i], xpoints[i + 1])
            if mid not in new_points:
                new_points.append(mid)
        xpoints.extend(new_points)
        xpoints = sorted(xpoints)
    return xpoints


def get_points(xpoints, ypoints):
    all_points = []
    for i in xpoints:
        y_point = uniform(ypoints[0], ypoints[1])
        all_points.append([i, y_point])
    return all_points


def draw(points, color, t):
    t.up()
    t.fillcolor(color)
    t.begin_fill()
    for i in points:
        t.goto(i)
        t.down()
    t.goto(400, -400)
    t.goto(-400, -400)
    t.goto(points[0])
    t.end_fill()
    t.hideturtle()


def main(xpoints, ypoints, color, order, t):
    all_xpoints = get_all_xpoints(xpoints, order)
    points = get_points(all_xpoints, ypoints)
    draw(points, color, t)


if __name__ == '__main__':
    xpoints1 = [-400, 400]
    ypoints1 = [100, 200]
    xpoints2 = [-400, 400]
    ypoints2 = [-100, 0]
    t = Turtle()
    t.speed('fastest')
    my_win = t.getscreen()
    my_win.bgcolor('cornflowerblue')
    main(xpoints1, ypoints1, 'green', 3, t)
    main(xpoints2, ypoints2, 'dark green', 3, t)
    my_win.exitonclick()
