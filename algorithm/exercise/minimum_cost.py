#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Problem Statement:
- 2D Matrix is given
- Each cell has a cost associated with it for accessing
- We need to start from (0.0) cell and go till (n-1,n-1) cell - We can go only to right or down cell from current cell
- Find the way in which the cost is minimum
"""


def minimum_cost(matrix, m, n):
    """ formula: cost(m,n) = 2d_list[m][n] + min(cost(m, n-1), cost(m-1, n))"""
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return matrix[0][0]
    else:
        option1 = minimum_cost(matrix, m - 1, n)
        option2 = minimum_cost(matrix, m, n - 1)
        print('option1', m - 1, n, matrix[m - 1][n])
        print('option2', m, n - 1, matrix[m][n - 1])
        return matrix[m][n] + min(option1, option2)


if __name__ == '__main__':
    matrix = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]
    row = len(matrix)
    column = len(matrix[0])
    print(minimum_cost(matrix, row - 1, column - 1))
