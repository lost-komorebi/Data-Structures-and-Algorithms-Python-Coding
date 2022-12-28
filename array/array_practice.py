#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://docs.python.org/3/library/array.html
__author__ = 'komorebi'

from array import *


# 1. Create an array and traverse.

print('1. Create an array and traverse.')
my_array = array('i', [1, 2, 3, 4, 5])
for i in my_array:
    print(i)

# 2. Access individual elements through indexes

print('2. Access individual elements through indexes')
print('Access the first element', my_array[0])
print('Access the last element', my_array[-1])


# 3. Append any value to the array using append() method

print('3. Append any value to the last of array using append() method')
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method

print('4. Insert value in an array using insert() method')
my_array.insert(0, 0)
print(my_array)

my_array.insert(3, 3)
print(my_array)

my_array.insert(8, 7)
print(my_array)

# 5. Extend python array using extend() method

print('5. Extend python array using extend() method')
print('Add another array to the end of an array')
array1 = array('i', [200, 201])
my_array.extend(array1)
print(my_array)

# 6. Add items from list into array using fromlist() method

print('6. Add items from list into array using fromlist() method')
print('Add list to the end of an array')
list1 = [100, 101]
my_array.fromlist(list1)
print(my_array)

# 7. Remove any array element using remove() method

print('7. Remove the first occurrence of specific element using remove() method')
my_array.remove(3)
print(my_array)


# 8. Remove last array element using pop() method

print('8. Remove last array element using pop() method')
my_array.pop()
print(my_array)


# 9. Fetch any element through its index using index() method

print('9. Fetch any element through its index using index() method')
print(my_array.index(3))


# 10. Reverse a python array using reverse() method

print('10. Reverse a python array using reverse() method')
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method

print('11. Get array buffer information through buffer_info() method')
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method

print('12. Check for number of occurrences of an element using count() method')
print(my_array.count(3))

# 13. Convert array to string using tobytes() method

print('13. Convert array to string using tobytes() method')
my_bytes = my_array.tobytes()
print(my_bytes)


# 14. Append a string to char array using frombytes() method

print('14. Append a string to char array using frombytes() method')
my_array = array('i')
my_array.frombytes(my_bytes)
print(my_array)

# 15. Convert array to a python list with same elements using tolist() method

print('15. Convert array to a python list with same elements using tolist() method')
print(type(my_array), my_array)
my_list = my_array.tolist()
print(type(my_list), my_list)

# 16. Slice Elements from an array

print('16. Slice Elements from an array')
print(my_array[1:5])
print(my_array[:])
print(my_array[::-1])
