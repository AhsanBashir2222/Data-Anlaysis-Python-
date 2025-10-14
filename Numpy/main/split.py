import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
#
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
nw = np.array_split(arr2, 3)
print(nw)
