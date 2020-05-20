import seaborn as sns
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01

# iterations = range(1400)
iterations = range(100)

plt.plot(iterations, bs_01)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()