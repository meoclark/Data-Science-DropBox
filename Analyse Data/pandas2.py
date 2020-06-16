import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

print(df1.head())
print(df2.head())

import glob

student_files = glob.glob("exams*.csv")

df_list = []

for filename in student_files:
  df_list.append(pd.read_csv(filename))
  
students = pd.concat(df_list)

print(students.head())
print(len(students))

import pandas as pd
from students import students

print(students.columns)
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.head())
print(students.columns)
print(students.exam.value_counts())

duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())
students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())


# Splitting by Index

# Create the 'month' column
df['month'] = df.birthday.str[0:2]

# Create the 'day' column
df['day'] = df.birthday.str[2:4]

# Create the 'year' column
df['year'] = df.birthday.str[4:]


students['gender'] = students.gender_age.str[0]
students['age'] = students.gender_age.str[1:]
print(students.head())
students = students[['full_name','exam','grade','score','gender','age']]


# Splitting by Character
# Create the 'str_split' column
df['str_split'] = df.type.str.split('_')

# Create the 'usertype' column
df['usertype'] = df.str_split.str.get(0)

# Create the 'country' column
df['country'] = df.str_split.str.get(1)

name_split = students['full_name'].str.split(" ")
students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)

print(students.head())

print(students.dtypes)

# String Parsing 

# First, we can use what we know of regex to get rid of all of the dollar signs:

fruit.price = fruit['price'].replace('[\$,]', '', regex=True)
#Then, we can use the pandas function .to_numeric() to convert strings containing numerical values to integers or floats:
fruit.price = pd.to_numeric(fruit.price)


students.score = students['score'].replace('[\%,]', '', regex=True)

students.score = pd.to_numeric(students.score)

print(students.head())

# More String Parsing

print(students.grade.head())

students['grade'] = students['grade'].str.split('(\d+)', expand=True)[1]

print(students.dtypes)

students['grade'] = pd.to_numeric(students['grade'])

avg_grade = students['grade'].mean()

print(avg_grade)

# Missing Values

#Most of the time, we use one of two methods to deal with missing values.

# Method 1: drop all of the rows with a missing value
# We can use .dropna() to do this:
bill_df = bill_df.dropna()

score_mean = students.score.mean()

print(score_mean)

students = students.fillna(0)

score_mean_2 = students.score.mean()

print(score_mean_2)

# Project Cleaning US Census Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

#print(us_census.columns)
#print(us_census.dtypes)
print(us_census.head())

# Removing the dollar sign in the Income column
us_census.Income = us_census.Income.replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)
# Splitting Gender pop into two to grab them separatery
us_census.GenderPop = us_census.GenderPop.str.split('_')
# Creating a new column with values from GenderPop
us_census["Men"] = us_census['GenderPop'].str.get(0)
us_census["Women"] = us_census['GenderPop'].str.get(1)
# Slicing and getting the required indexes. removing M and F respectively
us_census["Men"] = us_census["Men"].str[:-1]
us_census["Women"] = us_census["Women"].str[:-1]
# Converting both columns to numerical data
us_census["Men"] = pd.to_numeric(us_census["Men"])
us_census["Women"] = pd.to_numeric(us_census["Women"])

print(us_census.head())
# A plot of the Women column and Income column
plt.scatter(us_census["Women"],us_census["Income"])
plt.show()

# Filling in the NAN values
us_census["Women"] = us_census["Women"].fillna(0)
print(us_census.Women)

#duplicates = us_census.duplicated()
# census = us_census.drop_duplicates()
