from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.normal(size=(2, 3))
print(x)

# loc is mean and scale is standard deviation
z = random.normal(loc=1, scale=2, size=(2, 3))
print(z)

sns.displot(random.normal(size=100), kind="kde")
plt.show()
