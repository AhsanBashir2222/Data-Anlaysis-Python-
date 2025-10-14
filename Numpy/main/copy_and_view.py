import numpy as np
# copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# view
ab = np.array([1, 2, 3, 4, 5])
a = ab.view()
ab[0] = 43
print(ab)
print(a)
