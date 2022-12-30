#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import numpy as np
__author__ = 'komorebi'

# 1. How to find the missing number in an integer array of from 1 to 100?


def find_missing(n: list):
    return int(100 * 101 / 2) - sum(n)


n = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
     60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
     88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(find_missing(n))

# 2. Write a program to find all pairs of integers whose sum is equal to a
# given number


def find_pairs(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i + j == target:
                print(i, target - i)


print(find_pairs([1, 2, 3, 4, 5], 5))

# 3. How to check if an array contains a given number?


def if_in(array, target):
    if target in array:
        return True
    else:
        return False


print(if_in(np.array([1, 2, 3]), 3))

# 4. How to find maximum product of two integers in an  array which all
# elements are positive?


def find_max_product(array: numpy.array):
    array = np.sort(array)
    return array[-1] * array[-2]


my_array = np.array([1, 2, 3, 4, 5, 20, 100, 6, 33, 99])
print(find_max_product(my_array))


# 5. Detect if all elements in a list is unique.


def detect_unique(in_list):
    return True if len(set(in_list)) == len(in_list) else False


my_list = [1, 2, 3, 4, 5, 20, 100, 6, 33, 99]
print(detect_unique(my_list))


# 6. Check if two given string are permutation or not.


def check_permutation(s1, s2):
    return True if sorted(s1.lower()) == sorted(s2.lower()) else False


string1 = 'keep'
string2 = 'peek'
print(check_permutation(string1, string2))


# 7. Rotate an image represented by an NXN matrix by 90 degree

def rotate(array):
    shape = array.shape
    new_array = np.empty((shape[1], shape[0]))
    for i in range(shape[0]):
        new_array[:, shape[0]-i-1] = array[i, :]
    return new_array


my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(rotate(my_array))

