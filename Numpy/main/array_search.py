import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 4, 3, 4])
x = np.where(arr == 4)
print(x)

# search sorted
ab = np.array([1, 2, 3, 4, 5])
y = np.searchsorted(ab, 3, side='left')
print(y)
