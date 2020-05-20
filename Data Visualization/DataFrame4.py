## Adding a column
# The new column you are adding must be the same length with the existing tables
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df["Quantity"] = [5,'Qty',12,20]
print(df)
# Add columns here
df["Sold in Bulk?"] = ['Yes','Yes','No','No']
print(df)

# Adding a column that is true for all rows
df['Is taxed?'] = "Yes"
#This will create a new column with True. The one above,a column with yes
df['In Stock?'] = True
print(df)

# You can add a column by performing an operation on existing column
df['Sales Tax'] = df.Price * 0.075
df["Revenue"] = df["Price"] -  df["Cost to Manufacture"]
print(df)

#Performing Column Operations with apply,upper,lower
#remember to import from string upper or lower
from string import lower
import pandas as pd
from string import upper

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
  columns=['Name', 'Email']
)
# This creates a new column Lowercase Name with all the names in lower case
df['Lowercase Name'] = df['Name'].apply(lower)

# This creates a new column Uppercase Name with all the names in Upper case
df['Uppercase Name'] = df['Name'].apply(upper)
# The column remains the same but the names are changed to lower case. same can also be done for upper case
df['Name'] = df['Name'].apply(lower)
print(df)

# Renaming Columns 
# You can change column names using df.columns[list of new column names]
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']
# The line above changes the name and age to First Name and Age
df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID','Title','Category','Year Released','Rating']
print(df)

# You can also rename the individual columns by the .rename() method, Passin the columns as dictionary
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
#Using .rename() with only the columns keyword will create a new DataFrame, leaving your original DataFrame unchanged. 
#That’s why we also passed in the keyword argument inplace=True. Using inplace=True lets us edit the original DataFrame.
df.rename(columns={
    'name': 'movie_title'},
    inplace=True)
print(df)




