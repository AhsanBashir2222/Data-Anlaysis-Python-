from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# multinomial
x = random.multinomial(n=6, pvals=[0.1, 0.2, 0.3, 0.23, 0.12, 0.32])
print(x)
# exponential
# scale=reverse of rate
# size=return shape
x = random.exponential(scale=2, size=(2, 3))
print(x)

# chi is used to verify that data is correct or not
x = random.chisquare(df=2, size=(2, 3))
print(x)
# rayleigh
x = random.rayleigh(scale=2, size=(2, 3))
print(x)
print("Pareto")
# pareto 20 effort and 80 result
x = random.pareto(a=2, size=(2, 3))
print(x)
# zip
x = random.zipf(a=2, size=1000)
sns.displot(x[x < 10])
plt.show()
