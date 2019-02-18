import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

#print (df3.loc['20190220']) #用标签来选择数据
#print (df3.iloc[3]) #用位置来选择数据，第三行
#print (df3.ix[:3,['A','C']]) #弃用了
#print (df3[df3.A>8])
df3.iloc[2,2]=123 # 使用iloc进行修改
df3.loc ['20190220','B']=1122
#df3['F']=np.nan #新添加一列元素
#print (df3)
df3.iloc[1,1]=np.nan
print(df3)
#print(df3.dropna(axis=0,how='any')) #将含有空数据的行删除
#print(df3.fillna(value=100))

dafr = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
dafr1 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
dafr2 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res = pd.concat([dafr,dafr1,dafr2],axis=0,ignore_index=True)
print (res)

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'E':['E0','E1','E2','E3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3'],
                    'E':['E0','E1','E2','E3']})
print (pd.merge(left,right,on='key',suffixes=['_left','_right'])) #默认的合并方法为inner，只找相同的内容进行合并而看其他的内容；outer将没有的数据进行空处理，添加NaN
# 重复的列名进行添加改变加以区分

##绘图
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
#data.plot()
data2 = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data2 = data2.cumsum()
ax = data2.plot.scatter(x='A',y='B',color='Blue',label='Class1')
data2.plot.scatter(x='A',y='C',color='Green',label='Class2',ax=ax)
plt.show()

