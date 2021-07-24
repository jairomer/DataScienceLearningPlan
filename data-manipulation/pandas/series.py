#/usr/bin/env python3

import pandas as pd
import numpy as np

# Used the following tutorial as a learning path:
# https://medium.com/data-science-365/pandas-for-data-science-part-1-89bc231b3478

#############################################################
# The pandas series
#   pd.Series(data=..., index=..., dtype=..., name=...)
#
#############################################################

# Create a range from 1 to 10 in increments of 2.
an_array = np.arange(1, 10, 2)

# With default numerical index
ser_1 = pd.Series(an_array)
print(ser_1)

# With custom index
ser_2 = pd.Series(an_array, index=['a', 'b', 'c', 'd', 'e'])
print(ser_2)

# Parts of a series can be individually selected.
print(ser_2.index)
print(ser_2.values)

# Series can only be assembled from 1D data.
a = np.arange(1, 11).reshape(5, 2)
print(a)

try:
    ser_ex = pd.Series(a)
except:
    print("Series can only be assembled from unidimensional data types.")

# We can use both lists and dictionaries to assemble series.
# However, what about nested dictionaries?

d = {'a':1, 'b':[1, 2], 'c': {'1st': "first", '2nd':"second"}}

try:
    ser_ex = pd.Series(d)
    # Taken, this is perfectly legal.
    # This is interpreted as a series of objects.
    print(ser_ex)
except:
    print("Series can only be assembled from unidimensional dictionaries.")

# We can also create series using a scalar value.

ser_3 = pd.Series(5.3)
# This will be a series with a single value.
print(ser_3)

ser_4 = pd.Series(5.3, index=['1st', '2nd', '3rd'])
# This will be a series of 3 elements with the same value
print(ser_4)

# Selecting elements from a Series is done in the same way as Numpy Slices.

print(ser_1[1]) # Get value of second element
print(ser_2['b']) # Get value mapping from b

# More powerful notation involves the slice notation:
print(ser_1[0:3]) # Get a slice from first element to fourth

# And index labels
print(ser_2[['a', 'd']])

# You can also use conditions and Boolean operators to select elements from a series.
print(ser_1[ser_1 > 3]) # rows from ser_1 where value is larger than 3.

# Use numpy methods to make more complex queries.
print(ser_1[np.logical_and( ser_1>3 , ser_1 < 9)])

# Series are mutable

ser_2[2:] = 100 # Mass assign 100 to rows from the 3rd row onwards
print(ser_2)

# Operations and mathematical functions can be applied series-wide

print(ser_1 + ser_1)
print(ser_1 + ser_1/2)

# For further operations, check NumPy mathematical functions.
print(ser_1.mean())
