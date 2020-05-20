#Basic Line Plot
from matplotlib import pyplot as plt

y_values = [0, 1, 2, 3, 4]
x_values = [200, 400, 650, 800, 850]
plt.plot(x_values,y_values)
plt.show()
#This will output a single line of graph

#Basic Line Plot II .Multiple plots can be displayed on the same axis to compare them.

from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time,revenue)
plt.plot(time,costs)
plt.show()
#This will plot tghe two graphs on the same axis

#To specify color of lines.
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')

#Linestyles
# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')

#Marker
# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')

#Combination of the three
plt.plot(days, money_spent, color='green', linestyle='--')
plt.plot(days, money_spent_2, color='#AAAAAA',  marker='o')

#See Matplotlib Documentation for more

from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time,revenue,color='purple',linestyle = '--')
plt.plot(time,costs,color = '#82edc9',marker = 's')
plt.show()

