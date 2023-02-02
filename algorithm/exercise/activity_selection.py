#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Given N number of activities with their start and end times.
We need to select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.
"""


def select(activities):
    # sort all activities order by finish time
    activities.sort(key=lambda x: x[2])
    result = []
    for activity in activities:
        # iterate all activities to find activity which start time larger or
        # equal to finish time of last arranged activity's
        if not result or activity[1] >= result[-1][2]:
            result.append(activity)
    return len(result)


if __name__ == '__main__':
    activities = [
        ['A1', 0, 6],
        ['A2', 3, 4],
        ['A3', 1, 2],
        ['A4', 5, 8],
        ['A5', 5, 7],
        ['A6', 8, 9]
    ]
    select(activities)
