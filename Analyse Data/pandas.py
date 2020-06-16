# Calculating Column Statistics

# The general syntax for these calculations is:

df.column_name.command()

print(orders.head(10))
most_expensive = orders.price.mnum_colors = orders.shoe_color.nunique()

# Calculating Aggregate Functions I

# For this example, we’d use the following command:

grades = df.groupby('student').grade.mean()

# General synthax for using groupby
df.groupby('column1').column2.operation()

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)

# Calculating Aggregate Functions II

# Generally, you’ll always see a groupby statement followed by reset_index: reset_index converts it to a data frame


df.groupby('column1').column2.operation()
    .reset_index()

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))


# Calculating Aggregate Functions III
# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()


cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x:np.percentile(x,25)).reset_index()
print(cheap_shoes)


# Calculating Aggregate Functions IV

# we could calculate the average sales for each store on each day of the week across multiple months. The code would look like this:

df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

print(shoe_counts)


# Pivot Tables

#In Pandas, the command for pivot is:

df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
#For our specific example, we would write the command like this:

# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')


shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id').reset_index()

print(shoe_counts_pivot)


# REVIEW
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

# Part 1.
print(user_visits.head(10))

# Part 2.
click_source = user_visits.groupby('utm_source').id.count().reset_index()

#Part 3.
print(click_source)

#Part 4.
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

#print(click_source_by_month)

#Part 5.
click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

#Part 6.
print(click_source_by_month_pivot)


# A/B Testing Project
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())
print(ad_clicks.groupby('utm_source')
    .user_id.count()
    .reset_index())

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

print(ad_clicks.head())

clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()


clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()


clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])


a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']


