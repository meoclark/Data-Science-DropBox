# Variance 

import numpy as np

dataset = [3, 5, -2, 49, 10]
variance = np.var(dataset)


import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

teacher_one_grades = [80.24, 81.15, 81.29, 82.12, 82.52, 82.54, 82.76, 83.37, 83.42, 83.45, 83.47, 83.79, 83.91, 83.98, 84.03, 84.69, 84.74, 84.89, 84.95, 84.95, 85.02, 85.18, 85.53, 86.29, 86.83, 87.29, 87.47, 87.62, 88.04, 88.5]
teacher_two_grades = [65.82, 70.77, 71.46, 73.63, 74.62, 76.53, 76.86, 77.06, 78.46, 79.81, 80.64, 81.61, 81.84, 83.67, 84.44, 84.73, 84.74, 85.15, 86.55, 88.06, 88.53, 90.12, 91.27, 91.62, 92.86, 94.37, 95.64, 95.99, 97.69, 104.4]

#Set these two variables equal to the variance of each dataset using NumPy
teacher_one_variance = np.var(teacher_one_grades)
teacher_two_variance = np.var(teacher_two_grades)


#Histogram
plt.hist(teacher_one_grades, alpha = 0.75, label = "Teacher 1 Scores", bins = 7)
plt.hist(teacher_two_grades, alpha = 0.5, label = "Teacher 2 Scores", bins = 30)
plt.title("Student test grades in two different classes")
plt.xlabel("Grades")
plt.legend()
plt.show()

print("The mean of the test scores in teacher one's class is " + str(np.mean(teacher_one_grades)))
print("The mean of the test scores in teacher two's class is " + str(np.mean(teacher_two_grades)))

print("The variance of the test scores in teacher one's class is " +str(teacher_one_variance))
print("The variance of the test scores in teacher two's class is " +str(teacher_two_variance))


# Standard Deviation


nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)


# Quartiles
from song_data import songs
import matplotlib.pyplot as plt
import numpy as np

q1 = np.quantile(songs, 0.25)
q2 = np.quantile(songs, 0.5)
q3 = np.quantile(songs, 0.75)

plt.hist(songs, bins = 200)
plt.axvline(x=q1, label="Q1", c = '#6400e4')
plt.axvline(x=q2, label="Q2", c = '#fd4d3f')
plt.axvline(x=q3, label="Q3", c = '#4fe0b0')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.legend()
plt.show()


# Quantiles

# Define twenty_third_percentile here:
twenty_third_percentile = np.quantile(songs,0.23)


quartiles = np.quantile(songs,[0.25, 0.5, 0.75])
deciles = np.quantile(songs,[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
tenth = 3



# INTERQUARTILE RANGE

from song_data import songs
from scipy.stats import iqr

#Create the variables interquartile_range here:
interquartile_range  = iqr(songs)

# Ignore the code below here
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")



  # Project Life Expectancy by Country
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

print(data.head())

life_expectancy = data["Life Expectancy"]

life_expectancy_quartiles = np.quantile(life_expectancy, [0.25,0.50,0.75])

print(life_expectancy_quartiles)

plt.hist(life_expectancy)
plt.show()

gdp = data["GDP"]

median_gdp = np.quantile(gdp,0.5)
print(median_gdp)


low_gdp = data[data['GDP'] <= median_gdp]

high_gdp = data[data['GDP'] > median_gdp]

low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25,0.50,0.75])

high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25,0.50,0.75])

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()





