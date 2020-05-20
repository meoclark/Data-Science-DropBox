from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Keyword yerr is used to indicate the error and capsize to show the vertical line
plt.bar(range(len(ounces_of_milk)),ounces_of_milk,yerr=error,capsize = 5)
plt.show()