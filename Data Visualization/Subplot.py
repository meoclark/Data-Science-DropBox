#The command plt.subplot() needs three arguments to be passed into it:
#The number of rows of subplots
#The number of columns of subplots
#The index of the subplot we want to create

#For instance, the command plt.subplot(2, 3, 4) would create “Subplot 4” from the figure above.

from matplotlib import pyplot as plt

# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()


from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
plt.subplot(1,2,1)
plt.title("Temp vs Month")
plt.plot(months,temperature)
plt.subplot(1,2,2)
plt.title("Flights vs Temp")
plt.plot(temperature,flights_to_hawaii,marker = 'o')
plt.show()

