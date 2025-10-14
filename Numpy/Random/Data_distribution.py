from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.2, 0.3, 0.5, 0.0], size=(10))
print(x)

# 2-D
x = random.choice([3, 5, 7, 9], p=[0.2, 0.3, 0.5, 0.0], size=(3, 4))
print(x)
