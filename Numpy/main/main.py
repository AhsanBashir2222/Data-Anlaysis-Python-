import numpy as np

array = np.array([1, 2, 3, 4])
array = array*2
print(array)
# 0 dimensional array

array = np.array('A')
print(array.ndim)
# 1 dimensional array

array = np.array([['A', 'B', 'C'],
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I']])
print(array.ndim)

# 3 dimensions
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', '0'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'E', 'Z']]])

print(array.ndim)
print(array.shape)
print(array[0][0][0])
word = array[0, 0, 0] + array[0, 2, 1] + \
    array[2, 0, 0]+array[0, 0, 0]+array[1, 1, 1]
print(word)
