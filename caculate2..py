import numpy as np
A = np.arange(2,14).reshape((3,4))
print(A)
# print(np.argmin(A))
# print(np.argmax(A)) #数列里最大或者最小的索引
print(np.transpose(A))
print(np.clip(A,5,10)) #筛选数