import pandas as pd
import numpy as np
import matplotlib as plt

url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url)

print(df)

headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compressionratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
print(headers)

df.columns=headers
   
    
q=df.head(10)
print(q)

s=df.tail(10)
print(s)

type=df.dtypes
print(type)

drp=df.dropna(subset=["price"],axis=0,inplace=True)
print(drp)

print(df.iloc[1,1])

print(df.dropna())

print(df.replace('20130102','162'))

mean=df["symboling"].mean()
print(mean)

