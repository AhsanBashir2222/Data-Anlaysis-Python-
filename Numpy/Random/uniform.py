from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# l=0,h=1,s=the shape of return array
x = random.uniform(size=(2, 3))
print(x)
sns.displot(random.uniform(size=1000), kind="kde")
plt.show()
