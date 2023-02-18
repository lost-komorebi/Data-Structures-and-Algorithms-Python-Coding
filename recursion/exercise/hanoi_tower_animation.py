#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   hanoi_tower_animation.py
@Time    :   2023/02/18 10:42:46
@Author  :   komorebi 
'''
"""
Modify the Tower of Hanoi program using turtle graphics to animate the movement of the disks. 
Hint: You can make multiple turtles and have them shaped like rectangles.
"""

from turtle import Turtle, Screen
COLOR_MAP = ['blue', 'red', 'green', 'black', 'yellow', 'violet', 'orange']


class Disk(Turtle):

    def __init__(self, size):
        """ draw disk """
        super(Disk, self).__init__()
        self.size = size
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=size)
        self.color(COLOR_MAP[size])
        self.speed('slowest')  # to see animation clearly

    def move(self, coordinate):
        self.goto(coordinate)

    def get_size(self):
        return self.size


class Stack(Turtle):
    def __init__(self, name, coordinate: tuple):
        super(Stack, self).__init__()
        self.defined_name = name
        self.items = []
        self.draw(coordinate)

    def push(self, disk: Disk):
        cor = self.get_disk_coordinate()
        disk.goto(cor)
        self.items.append(disk)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)

    def draw(self, coordinate: tuple):
        """ draw rod """
        self.hideturtle()
        self.penup()
        self.goto(coordinate)
        self.pendown()
        self.color('black')
        self.forward(50)
        self.backward(100)
        self.forward(50)
        self.left(90)
        self.forward(100)
        self.coordinate = coordinate
        self.write_name()

    def get_own_coordinate(self):
        return self.coordinate

    def get_disk_coordinate(self):
        """ calculate coordinate for next disk to be added """
        own_coordinate = self.get_own_coordinate()  # get rod coordinate
        x_cor = own_coordinate[0]
        y_cor = own_coordinate[1] + 10 + 20 * len(self)
        return (x_cor, y_cor)

    def write_name(self):
        """ add name for rod """
        pen = Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(self.get_own_coordinate()[
            0], self.get_own_coordinate()[1] - 40)
        pen.pendown()
        pen.write(self.defined_name, move=False,
                  align='center', font=('Arial', 20, 'normal'))


def hanoi_tower(n, from_rod, to_rod, mid_rod):
    """ use stacks to represent towers """
    if n > 0:
        hanoi_tower(n - 1, from_rod, mid_rod, to_rod)
        disk = from_rod.pop()
        to_rod.push(disk)
        print(
            f'move {disk.get_size()} from {from_rod.defined_name} to {to_rod.defined_name}')
        hanoi_tower(n - 1, mid_rod, to_rod, from_rod)


if __name__ == '__main__':
    screen = Screen()

    from_stack = Stack('a', (-200, -100))
    mid_stack = Stack('b', (0, -100))
    to_stack = Stack('c', (200, -100))

    n = 4

    for i in reversed(range(1, n+1)):
        disk = Disk(i)
        from_stack.push(disk)

    hanoi_tower(n, from_stack, to_stack, mid_stack)
    screen.exitonclick()
