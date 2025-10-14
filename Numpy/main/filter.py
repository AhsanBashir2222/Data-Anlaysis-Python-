import numpy as np
arr = np.array([41, 42, 43, 44])
x = arr[[True, False, False, True]]
print(x)


#
arr1 = np.array([41, 42, 43, 44])
filter_array = arr1 > 42
newarr = arr1[filter_array]
print(filter_array)
