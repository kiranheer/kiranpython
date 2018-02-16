import pandas as pd
import numpy as np
import matplotlib as plt
url="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url, header=None)
df.head(url)
print(df)

excel=pd.read_excel(url)
print(excel)
son=pd.read_json(url)
print(son)



