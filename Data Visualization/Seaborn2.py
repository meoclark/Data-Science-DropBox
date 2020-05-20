#Seaborn Distributions
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Add your code below:
sns.barplot(data = df,x = "label",y = "value")
plt.show()


# KDE plots Part 1
#KDE stands for Kernel Density Estimator. A KDE plot gives us the sense of a univariate as a curve.
# A univariate dataset only has one variable
#KDE plots are preferable to histograms because depending on how you group the data into bins and the width of the bins,
# you can draw wildly different conclusions about the shape of the data

# to plot a kde plot we ue sns.kdeplot(), it takes two arguments. Data,Shade.
# data - the univariate dataset being visualized, like a Pandas DataFrame, Python list, or NumPy array
# shade - a boolean that determines whether or not the space underneath the curve is shaded

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Add your code below:
sns.kdeplot(set_one,shade = True)
sns.kdeplot(set_two,shade = True)
sns.kdeplot(set_three,shade = True)
sns.kdeplot(set_four,shade = True)
plt.legend(['set_one', 'set_two', 'set_three', 'set_four'])
plt.show()

# Box Plot
# The box plot (also known as a box-and-whisker plot) 
#can’t tell us about how our dataset is distributed, like a KDE plot.
# But it shows us the range of our dataset,
#gives us an idea about where a significant portion of our data lies, and whether or not any outliers are present.
# Add your code below:
sns.boxplot(data=df, x='label', y='value')
plt.show()

# Violin Plots
#Seaborn gives us another option for comparing distributions - a violin plot. 
#Violin plots provide more information than box plots because instead of mapping each individual data point,
# we get an estimation of the dataset thanks to the KDE.

sns.violinplot(data=df, x="label", y="value")
plt.show()
