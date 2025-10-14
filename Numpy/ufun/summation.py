import numpy as np

n1 = np.array([1, 2, 3, 4])
n2 = np.array([2, 3, 4, 5])
n3 = np.sum([n1, n2])
print("Sum :", n3)

# axix
n1 = np.array([1, 2, 3, 4])
n2 = np.array([2, 3, 4, 5])
v3 = np.sum([n1, n2], axis=1)
print("Sum for axis : ", v3)

# cumsum add previous also

abc = np.array([1, 2, 3, 4, 5])
a = np.cumsum(abc)
print("Cumsum : ", a)
