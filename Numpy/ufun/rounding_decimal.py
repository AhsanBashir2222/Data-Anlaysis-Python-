import numpy as np
# truncate remove the decimal
arr = np.trunc([-3.456, -5.774])
print(arr)

print("around : ")
abc = np.around(3.2334, 2)
print(abc)
# ceil
w1 = np.ceil([-3.112, 3.56])
print("ceil : ", w1)
