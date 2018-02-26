import pandas as pd
import numpy as np
import matplotlib as plt

#url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv('E:/kiranpython/kiranpython/Project1/autodataset.csv')
print(df)

s=df.tail(10)
print(s)

type=df.dtypes
print(type)

print(df.replace('20130102','162'))

mean=df["fuel-type"].mean()
print(mean)
