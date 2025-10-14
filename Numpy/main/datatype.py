import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Creating array with define data type
ar = np.array([1, 2, 3, 4], dtype='S')
print(ar)
print(arr.dtype)
# astype
ab = np.array([1, 2, 3, 4])
neww = ab.astype(int)
print(neww)
