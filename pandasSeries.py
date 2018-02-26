import pandas as pd
import numpy as np
import matplotlib as plt
s=pd.Series([1,3,5,np.nan,6,8])
print(s)

dates=pd.date_range('20181001',periods=6)
print(dates)



c=pd.Timestamp('20130102')
print(c)
print("***********")
d=np.array([3]*4,dtype='int32')
print(d)
print("*********************")



df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)


dd=df2.dtypes
print(dd)

ind=df2.index
print(ind)

hd=df2.head()
print(hd)

tl=df2.tail(2)
print(tl)

col=df2.columns
print(col)

val=df2.values
print(val)

st=df2.sort_index(axis=1,ascending=False)
print(st)

sl=df2['A']
print(sl)











