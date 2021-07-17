import  numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
c = a*b
d = np.dot(a,b)
e = np.random.random((2,4))
print(np.min(e,axis=1))
# print(c)
# print(d)