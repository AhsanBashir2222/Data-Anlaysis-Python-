import numpy as np
np1 = np.array([1, -3, 2, 4, 6, 7, 9])
print("square root")
# squareroot of each element
print(np.sqrt(np1))
# absulote
print("absolute")
print(np.absolute(np1))

# print exponent
print("exponent")
print(np.exp(np1))

# min/max
print("min")
print(np.min(np1))

print("sign negative or positive")
print(np.sign(np1))


# vector
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = []
for i, j in zip(x, y):
    z.append(i+j)

print(z)
print("numpy has add function")
a = [5, 4, 3, 2, 1]
b = [6, 3, 4, 5, 7]
c = np.add(a, b)
print(c)
