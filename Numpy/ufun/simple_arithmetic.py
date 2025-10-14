import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 6, 7, 8, 9])
arr3 = np.add(arr1, arr2)
print(arr3)

print("subtract : ")
z1 = np.array([5, 4, 3, 2, 1])
z2 = np.array([1, 2, 3, 4, 5])
z3 = np.subtract(z1, z2)
print(z3)

print("for power : ")
a1 = np.array([44, 55, 66, 77])
a2 = np.array([2, 3, 4, 5])
a3 = np.power(a1, a2)
print(a3)

print("for divide : ")
b1 = np.array([33, 44, 55, 66, 77])
b2 = np.array([3, 4, 5, 6, 7])
b3 = np.divmod(b1, b2)
print(b3)

print("for absolute : ")
c1 = np.array([-33, 44, -55, 66, 77])
c2 = np.array([3, -4, 5, -6, 7])
c3 = np.absolute(c1)
print(c3)
