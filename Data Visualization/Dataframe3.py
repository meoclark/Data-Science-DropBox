import pandas as pd

#Inspect A DataFrame

df = pd.read_csv('imdb.csv')
#To vew
print(df.head())
#To get some statistics about the columns
print(df.info())

#Selecting columns
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df["clinic_north"]
clinic_south = df.clinic_south

print(type(clinic_north))
print(type(df))

#Selecting Multiple Columns
clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))

#Selecting Rows
#You can select the rows by using iloc and the index position of the row. row start from 0
march = df.iloc[2]

#Selecting Multiple Rows
april_may_june = df.iloc[3:6]
print(april_may_june)


# Selecting Row with logic you can use any operator u want(<, > , != , ==)
january = dataframe[dataframe.month == 'January' ]
print(january )

# Selecting Row with multiple logic
# In Python, | means “or” and & means “and”
march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)

# Selecting Row with isin
january_february_march = df[df.month.isin(['January','February','March'])]
print(january_february_march)


#Setting Indices
df2 = df.loc[[1, 3, 5]]
print(df2)

# We can set the indices or SN using indices.
# inplace= True will allow u modify your existing dataframe
# drop = 2 will make sure u dont retain the old dataframe column or have an extra column
df3 = df2.reset_index(inplace=True,drop=True)
print(df2)


#Exercise
#Part 1: reading the csv
orders = pd.read_csv('shoefly.csv')

#Part 2: inspecting the first five lines of data
print(orders.head(5))

#Part 3: selecting the column 'email'
emails = orders.email

#Part 4: the Frances Palmer incident
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

#Part 5: Comfy feet means more time on the street
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]



