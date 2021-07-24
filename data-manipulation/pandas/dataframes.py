#/usr/bin/env python

import pandas as pd
import numpy as np

# Used the following tutorial as a learning path:
# https://medium.com/data-science-365/pandas-for-data-science-part-1-89bc231b3478

#############################################################
# The pandas dataframe
#   pd.DataFrame(data=..., index=..., columns=...)
#
#############################################################
#
# data arguments include:
# - A two-dimensional ndarray
# - A dictionary of dictionaries
# - A dictionary of lists
# - A dictionary of (pandas) series
#

# a 2D ndarray
an_array = np.array([[15, 85], [25, 90], [26, 70], [24, 80]])

ser_1 = pd.DataFrame(an_array,
                     index=['1st', '2nd', '3rd', '4th'],
                     columns=['age', 'marks'])

print(ser_1)

# A dictionary of dictionaries
a_dict = {'name': {'Ru':'Rukshan', 'Pr':'Prasadi', 'Gi':'Gihan', 'Ha':'Hansana'},
          'age' : {'Ru':25, 'Pr': 25, 'Gi': 26, 'Ha':24},
          'marks': {'Ru':85, 'Pr':90, 'Gi':70, 'Ha':80}}
# Notice that:
## Internal keys will become the row indexes.
## External keys will become the column indexes.

df_1 = pd.DataFrame(a_dict)
print(df_1)
print()
# What happens if the internal keys are not consistent?
b_dict = {'name': {'a':'Rukshan', 'Pr':'Prasadi', 'X':'Gihan', 'Ha':'Hansana'},
          'age' : {'Ru':25, 'Pr': 25, 'Gi': 26, 1:24},
          'marks': {'Ru':85, 'Pr':90, 'l':70, 'Ha':80}}

try:
    df_ex = pd.DataFrame(b_dict)
    print(df_ex)
    print()
    # Taken, the result will be a larger dataset with multiple rows but empty values.
except:
    print("Internal keys inside a dictionary of dictionares needs to be consistent")
    print("in order to correctly assemble a data frame.")

# Using dictionary series

ind =['Ru', 'Pr', 'Gi', 'Ha'] # row index
ser1 = pd.Series(['Rukshan', 'Prasadi', 'Gihan', 'Hansana'],index=ind)
ser2 = pd.Series([25, 25, 26, 24], index=ind)
ser3 = pd.Series([85, 90, 70, 80], index=ind)

# A dictionary of series
a_dict = {'name': ser1, 'age': ser2, 'marks': ser3}

df_3 = pd.DataFrame(a_dict)
print(df_3)
print()

# Create a dataframe from a file.
#   Pandas supports many different file formats or data sources
#   out of the box, each of them with the prefix read_*
#
#
# df = pd.read_csv('/this/is/a/file', sep='\t')
# df.index = ['Ru', 'Pr', 'Gi', 'Ha']

# Selecting elements from a DataFrame
#   DataFrames can be accessed in a great variety of ways.
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
#

# Value mutability
# Access as a matrix.
df_3.iloc[0, 2] = 100
print(df_3)
print()

# Size mutability, adding new rows and columns
df_4 = df_3

# Add a new column
df_4['grade'] = ['A', 'A+', 'B', 'A']

# Add a new row
try:
    df_4.loc['Ma'] = ['Manisha', 25, 65]
except:
    print("Remember that the number of attributes of a row must")
    print("match the number of columns.")

df_4.loc['Ma'] = ['Manisha', 25, 65, 'C+']

print(df_4)
print()

# Each column in a dataframe is a series.
age_series = df_4['age']
print(age_series)
print()

