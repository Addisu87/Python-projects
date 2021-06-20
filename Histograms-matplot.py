import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

mu = 80
sigma = 7
x = np.random.normal(mu, sigma, size = 200)

fig, ax = plt.subplots()

print(ax.hist(x, 20))
print(ax.set_title("New Histogram"))
print(ax.set_xlabel('bin range'))
print(ax.set_ylabel('frequency'))

print(fig.tight_layout())
print(plt.show())
