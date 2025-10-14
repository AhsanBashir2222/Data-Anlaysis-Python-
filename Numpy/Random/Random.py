from numpy import random
# Random between 1-100
x = random.randint(100)
print(x)

# random float b/w 0-1
x = random.rand()
print(x)

# size
x = random.randint(100, size=(5))
print(x)

# 2-d with 3 row
x = random.randint(100, size=(3, 4))
print(x)

x = random.rand(5)
print(x)

x = random.rand(3, 4)
print(x)

# choice
x = random.choice([1, 2, 3, 4, 5])
print(x)
# 2-D
x = random.choice([2, 3, 4, 5,], size=(3, 6))
print(x)
