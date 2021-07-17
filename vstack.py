import numpy as np
A = np.array([1,1,1])
B = np.array([2,3,5])
C = np.vstack((A,B))
D = np.hstack((A,B))

# split
A = np.arange(12).reshape(3,4)
print(A)
print(np.split(A,2,axis=1))
# 1 是列
print(np.split(A,3,axis=0))
