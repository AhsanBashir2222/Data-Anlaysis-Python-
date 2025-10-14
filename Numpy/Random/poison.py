# how many time a event occur in specific amount of time
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.poisson(lam=2, size=10)
print(x)
# for visualization
sns.displot(random.poisson(lam=2, size=10))
plt.show()
