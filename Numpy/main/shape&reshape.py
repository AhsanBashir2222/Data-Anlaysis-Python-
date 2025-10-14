import numpy as np
# d-1 shape
n1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(n1)
print(n1.shape)
# d-2 shape
n2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(n2)
print(n2.shape)
# ndim
n3 = np.array([1, 2, 3, 4, 5, 6], ndmin=5)
print(n3)
print("shape of array : ", n3.shape)


# reshape
n4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = n4.reshape(4, 3)
print(newarr)
#
abc = np.array([1, 2, 3, 4, 5, 6, 7, 8])
n = abc.reshape(2, 2, -1)
print(n)
