#!/usr/bin/env python

import numpy as np

######################################################
# Indexing
#   The process of accessing items that exist in an
#   iterable or a sequence form.
######################################################

# Generate an array of 10 elements.
arr = np.arange(10)
print(arr)

print('first element:', arr[0])
print('second element:', arr[1])
print('last element:', arr[-1])
print('second last element:', arr[-2])
print()

arr_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('array:', arr_2)
print()
arr_2[0, 1] = 21
arr_2[1, 3] = 10
print('modified array:', arr_2)
print()


######################################################
# Slicing
#   The process of retrieving a specific portion or
#   part of an array or list.
#   Slicing can retrieve only the elements that are
#   continuous.
######################################################

# slice(start, stop, step)
so = slice(0, 5, 2) # From 0 to 5 in steps of 2, [0, 2, 4]
print('Slice:', so)
print('Original array:', arr)
print('Sliced array:', arr[so])
print()
# Slicing with :colon
arr_3 = np.arange(10)
slice_arr = arr[1: 9: 2] # start: stop: step: -> [1, 3, 5, 7]
print('Original array:', arr)
print('Sliced array:', slice_arr)
print()
# Slicing with negative index
arr_4 = np.arange(8) # -> [0,1,2,3,4,5,6,7]

print('Original array:', arr_4)
print('Sliced array:', arr_4[-1:-5: -1]) # From last to the fith from last, backtracking 1 by 1.

print('Sliced array:', arr_4[2: ])
print('Sliced array:', arr_4[: -3])
print('Sliced array:', arr_4[4: 8])
print()

##########################################
# Slicing of Multi-Dimensional Array
##########################################
arr_5 = np.arange(20).reshape(4,5)
print(arr_5)
print()

print('third row:', arr_5[2, :])
print('reverse of third row:', arr_5[2, ::-1])
print('values between row 1-3 and column 2-4')
print(arr_5[0:3, 1:4])

# Slicing using compound conditions

# Array of elements such that they are disible by 2 and larger than 5.
print(arr_5[(arr_5[:, :] % 2 == 0) & (arr_5 [:, :] > 5)])

# Index at position (0,1), (2,3) and (3,4)
print(arr_5[[0, 2, 3], [1, 3, 4]])

# Get corner values
print(arr_5[[0, 0, 3, 3],[0, 4, 0, 4]])
