import numpy as np
import pandas as pd

s = pd.Series([1,3,6,np.nan,44,143])
#print(s)
dates = pd.date_range('20190218',periods=6)
#print (dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20190218'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print (df2)
#print (df2.index)
#print (df2.columns)
#print (df2.values)
#print (df2.describe())
#print (df2.T)
print (df2.sort_index(axis=1,ascending=False))

df3 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print (df3)
print (df3.loc['20190220']) #用标签来选择数据
print (df3.iloc[3]) #用位置来选择数据，第三行
print (df3.ix[:3,['A','C']])
print (df3[df3.A>8])