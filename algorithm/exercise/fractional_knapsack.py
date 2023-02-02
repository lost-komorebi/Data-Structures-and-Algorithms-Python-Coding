#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Given the weights and values of N items,
in the form of {value, weight} put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In Fractional Knapsack, we can break items for maximizing the total value of the knapsack
we cannot use one item repeatedly
"""


def fractional_knapsack(weight, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    max_value = 0
    for item in items:
        if weight > item[1]:  # weight > item.weight
            max_value += item[0]
            weight -= item[1]
        else:  # weight < item.weight
            ratio = weight / item[1]
            max_value += ratio * item[0]
            weight -= weight * ratio

    return max_value


if __name__ == '__main__':
    weight = 50
    items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
    fractional_knapsack(weight, items)
