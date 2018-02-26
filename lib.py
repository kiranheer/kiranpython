import pandas as pd
import numpy as np
import matplotlib as plt

#url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv('E:\kiranpython\kiranpython\Project1\autodataset.csv')

print(df)

headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compressionratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
print(headers)

