import numpy as np

ar=np.array([[1,2,3],[4,5,6]])
print(ar)
print(ar.ndim)
print('shape:',ar.shape)
print('size:',ar.size)

ar2=np.array([1,2,3],dtype=np.float)
print(ar2.dtype)

ar3 = np.zeros((3,4))
print(ar3)

ar4 = np.arange(1,20,2)#从1到20, 步长为2
ar5 = np.arange(12).reshape((3,4))
print(ar4)
print(ar5)
print(ar4<10)

ar6 = ar5.reshape((4,3))
ar5_dot = np.dot(ar5,ar6)#矩阵的乘法
print(ar5_dot)

ar7 = np.arange(3,15).reshape((3,4))
print(ar7)
print(ar7[2,:])#第二行所有的数
for row in ar7:
    print(row)#迭代所有的行
for column in ar7.T:
    print(column)#迭代所有的列
for item in ar7.flat:
    print(item)#迭代出所有的元素

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
C = np.vstack((A,B))# 垂直合并vertical stack 对应行处理，在行增加
D = np.hstack((A,B))# 横向合并horizontal stack 对应列处理，在列增加
E = np.concatenate((A,B,A),axis=1) #列处理相加
print(C)
print(D)
print(E)