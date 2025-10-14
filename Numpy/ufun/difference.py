import numpy as np
arr = np.array([10, 15, 25, 5])
new = np.diff(arr)
print(new)

# 2-d
ar = np.array([10, 15, 25, 5])
ab = np.diff(ar, n=2)
print(ab)
