import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
a = np.prod(a1)
print(a)

#
b1 = np.array([1, 2, 3, 4, 5])
b2 = np.array([1, 2, 3, 4, 5])
b3 = np.prod([b1, b2])
print("B3 : ", b3)

b1 = np.array([1, 2, 3, 4, 5])
b2 = np.array([1, 2, 3, 4, 5])
x3 = np.prod([b1, b2], axis=1)
print("x_axis : ", x3)
