#This used to syle an error by shading the error
#It takes 3 parameters  x_value i.e normal x-axis in our graph. Lower bound and upper bound:can be done with list comprehension.
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

plt.plot(months,revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
#For lower  added and error of -10%
y_lower = [0.9 * i for i in revenue]
#For upper added and error of +10%
y_upper = [1.1 * i for i in revenue]
# I now used fill_between to shade the error
plt.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.show()