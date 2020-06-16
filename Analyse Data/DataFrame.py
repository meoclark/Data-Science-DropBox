# MODIFYING DATAFRAMES

# Adding a Column I
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)


# Adding a Column II
df['In Stock?'] = True
#Now all of the rows have a column called In Stock? with value True.

df['Is taxed?'] = 'Yes'
# all rows will now have a column yes

# Adding a Column III
df['Sales Tax'] = df.Price * 0.075

df['Margin'] = df['Price'] - df['Cost to Manufacture']

# Performing Column Operations 

df['Lowercase Name'] = df.Name.apply(lower)

# Reviewing Lambda Function
# Create a lambda function mylambda that returns the first and last letters of a string
mylambda = lambda x: x[0] + x[-1]

print(mylambda('This is a string'))

# Reviewing Lambda Function: If Statements

#In general, the syntax for an if function in a lambda function is:

lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else "You must be over 13"

print(mylambda(13))


# Applying a Lambda to a Column
# We could use the following code with a lambda function and the string method .split():

df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1])

# Add columns here
get_last_name = lambda x: x.split(" ")[-1]

df['last_name'] = df.name.apply(lambda x: x.split(" ")[-1])

print(df)


# Applying a Lambda to a Row


# We can create this column using a lambda function and the keyword axis=1:

df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.075
     if row['Is taxed?'] == 'Yes'
     else row['Price'],
     axis=1)

import pandas as pd

df = pd.read_csv('employees.csv')

total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)

# Renaming Columns

df.columns = ["ID","Title","Category","Year Released","Rating"]
print(df)


# Renaming Columns II

# Rename columns here
df.rename(columns={
    'name': 'movie_title'
    },
    inplace=True)
print(df)


# Review
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)



# Project Petal

import pandas as pd

inventory = pd.read_csv("inventory.csv")
#print(inventory.head(10))

staten_island = inventory.head(10)
product_request = staten_island["product_description"]

seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
inventory["in_stock"] = inventory.apply(lambda row: True if row.quantity > 0 else False , axis = 1)

inventory["total_value"] = inventory.apply(lambda row: row.price * row.quantity,axis = 1)


combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory["full_description"] = inventory.apply(lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description))
print(inventory.head(10))











