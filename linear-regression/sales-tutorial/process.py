#/usr/bin/env python3

import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

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
#with open(data_file, encoding=) as f:
# Lesson: Different CSVs can have different encodings.
with open(data_file, encoding="iso-8859-1") as f:
    data = pd.read_csv(f, sep=",")
    cleanNan(data, "TERRITORY")
    cleanNan(data, "STATE")
#    print(data.describe())
#    print(data.describe(include=object))


# 1. Visualization
#graphs = sns.pairplot(data)
#plt.show()






