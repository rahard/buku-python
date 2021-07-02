import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
b = np.array([[3,3,3],[5,5,5],[5,3,1]])
print(b)

c = a+b
print(c)

d = np.matmul(a, b)
print(d)
