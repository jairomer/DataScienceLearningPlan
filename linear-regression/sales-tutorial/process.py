#/usr/bin/env python3

import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# This is nice and good, but most of the data
# cleaning needs context aware modifications.
#
# For instance: We cannot assign a random state from
# different countries.
def cleanNan(data: pd.DataFrame, column: str):
    uniques = []
    for i in data[column]:
        # lesson: Use pandas type system to handle NaNs.
        if i not in uniques and not pd.isnull(i):
            uniques.append(i)
    print(uniques)
    subs = lambda x: x if not pd.isnull(x) else random.choice(uniques)
    data[column] = data[column].apply(subs)
    print(data[column])

# Read CSV
data_file = 'sales_data_sample.csv'
data = None
working_data = None
# Lesson: Different CSVs can have different encodings.

with open(data_file, encoding="iso-8859-1") as f:
    data = pd.read_csv(f, sep=",")

    #print(data.corr())
    #print(data.describe())
    #print(data.describe(include=object))
    working_data = data.select_dtypes(exclude=[object])
    #print(working_data.corr())

# Select variables
## We want to predict the number of sales from all the others.
## Y is the sales column.
## X is the rest of the columns.

x_data = working_data[working_data.columns.difference(['SALES'])]
y_data = working_data['SALES']

print(x_data.describe())
print(y_data.describe())

# Split data
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)

# Instantiate and fit model into linear regression.
linreg = LinearRegression()
linreg.fit(x_train, y_train)


# Obtain predictions
y_pred = pd.Series(linreg.predict(x_test))
#print()
#print("Predicted: ")
#print( y_pred)
#print()
#print("Real: ")
#print(y_test)

# Evaluate the model performance.
print("RMSE: ", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("mean absolute error: ", metrics.mean_absolute_error(y_test, y_pred))

scr = linreg.score(x_test, y_test)
print('Coefficient of determination:', scr )
print("###")
print("Model")
print("Intercept: ")
print(linreg.intercept_)
print()
print("Coefficients:")
print(linreg.coef_)
print()
