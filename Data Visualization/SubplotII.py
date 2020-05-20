#Adjusts x-axis default of 0.1
plt.subplots_adjust(bottom=0.2)

#Adjusts y-axis. Default of 0.125
plt.subplots_adjust(left=0.13)

#Adjusts the figure. Default of 0.9
plt.subplots_adjust(right=1.0)

#Adjusts the horizontal space btw the adjacent subplots. Default 0.2
plt.subplots_adjust(wspace=0.2)

#Adjusts the vertical space btw the adjacent subplots. Default 0.2
plt.subplots_adjust(hspace=0.2)

#Adjusts the top margin, with a default of 0.9
plt.subplots_adjust(top=0.2)

#It can take multiple arguments
plt.subplots_adjust(top=0.95, hspace=0.25)


# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Subplot Adjust
plt.subplots_adjust(wspace=0.35)

plt.show()

from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
#Column is how many box you want to show side by side
plt.subplot(2,1,1)
plt.plot(x,straight_line)
plt.subplot(2,2,3)
plt.plot(x,parabola)
plt.subplot(2,2,4)
plt.plot(x,cubic)
plt.subplots_adjust(wspace=0.35,bottom = 0.2)
plt.show()
