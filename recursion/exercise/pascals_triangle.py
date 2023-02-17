#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   pascals_triangle.py
@Time    :   2023/02/17 11:18:45
@Author  :   komorebi 
'''
"""
Pascal’s triangle
    1
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1
"""


def pascals_triangle_by_row(row):
    """ return the nth row of pascals_tiangle as a 1d list"""
    if row == 0:
        return []
    elif row == 1:
        return [1]
    else:
        last_row = pascals_triangle_by_row(row - 1)
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        return new_row


def pascals_triangle(row):
    """ return the first n rows of pascals triangle as a 2d list"""
    if row == 0:
        return []
    elif row == 1:
        return [[1]]  # 2d list
    else:
        result = pascals_triangle(row - 1)
        last_row = result[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)
        return result


if __name__ == '__main__':
    for i in range(1, 11):
        print(pascals_triangle_by_row(i))
    for i in pascals_triangle(10):
        print(i)
