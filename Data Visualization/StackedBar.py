#To make stacked Bars, use the keyword bottom as a parameter
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)),sales1)
plt.bar(range(len(drinks)),sales2,bottom = sales1)


plt.legend(["Location 1","Location 2"],loc=1)
plt.show()