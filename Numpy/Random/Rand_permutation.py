from numpy import random
import numpy as np

# for shaffle, donot make another
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
# per leave the original unchanged,and new array will occur

print(random.permutation(arr))
