import pandas as pd

#To create a data frame. use the method DataFrame(), it takes in a list. the keys are the column name and the values are the column values.

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
 'Product Name': ['t-shirt','t-shirt','skirt','skirt'],
 'Color' : ['blue','green','red','black']


})

print(df1)