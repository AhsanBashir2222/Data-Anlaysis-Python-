import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

arr1 = np.array([[1, 2, 3], [2, 3, 4]])
for x in arr1:
    print(x)

#
for x in arr1:
    for y in x:
        print(y)


# enumerate
arr2 = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
for idx, x in np.ndenumerate(arr2):
    print(idx, x)
