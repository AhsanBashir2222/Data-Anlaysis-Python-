import numpy as np
array = np.array([1, 2, 3])
print(array+1)
# Vectorized match function
print(np.sqrt(array))
print(np.round(array))
print(np.pi*array*2)

# element wise
ar1 = np.array([1, 2, 3, 4])
ar2 = np.array([5, 6, 7, 8])
print(ar1+ar2)

# comparison operator
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr < 5)
arr[arr < 5] = 0
print(arr)
