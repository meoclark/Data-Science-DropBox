#Plotting Bars with Seaborn
#sns.bar() it takes 3 parameters at least. Data = df,x column = "string", y column = "String"
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("results.csv")
print(df)


sns.barplot(data= df,x= "Gender",y= "Mean Satisfaction")
plt.show()

# Understanding Aggregate
#An aggregate statistic, or aggregate, is a single number used to describe a set of data. e.g mean,median,mode,standard deviation
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]
print(assignment1)
asn1_median = np.median(assignment1.grade)
print(asn1_median)

# Plotting Aggregates
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")
sns.barplot(data = gradebook,x = "assignment_name",y = "grade")
plt.show()

# Modifying Error Bars
#By default, Seaborn uses something called a bootstrapped confidence interval.
#this interval means that “based on this data, 95% of similar situations would have an outcome within this range”
#“if we gave this assignment to many, many students, we’re confident
# that the mean score on the assignment would be within the range represented by the error bar”.
#You can add standard deviation instead of using the confidence interval by adding a parameter. ci = "sd"
sns.barplot(data=gradebook, x="name", y="grade",ci = 'sd')
plt.show()


#Calculating Different aggregates. you can use the keyword estimator to pass in the function executable within a list.
df = pd.read_csv("survey.csv")
print(df)
sns.barplot(data = df, x = "Gender", y = "Response", estimator = len)
plt.show()

sns.barplot(data = df, x = "Gender", y = "Response", estimator = np.median)
plt.show()

# Aggregating by multple columns
#The hue parameter adds a nested categorical variable to the plot.
df = pd.read_csv("survey.csv")
sns.barplot(data= df, x = "Age Range",y = "Response", hue = "Gender")
plt.show()



#To review the seaborn workflow:
#1. Ingest data from a CSV file to Pandas DataFrame.
df = pd.read_csv('file_name.csv')

#2. Set sns.barplot() with desired values for x, y, and set data equal to your DataFrame.
sns.barplot(data=df, x='X-Values', y='Y-Values')

#3. Set desired values for estimator and hue parameters.
sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value')

#4. Render the plot using plt.show().
plt.show()


