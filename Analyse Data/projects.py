# PROJECT: BOARD SLIDES FOR FOODWHEEL
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

print(restaurants.head())

cuisine_options_count = restaurants.cuisine.nunique()

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)

cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values


plt.pie(counts,
        labels=cuisines,
       autopct='%d%%')
plt.title('FoodWheel')
plt.axis('equal')
plt.show()


# Orders Over Time

from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

ax = plt.subplot()

bar_heights = avg_order.price
bar_errors = std_order.price

plt.bar(range(len(bar_heights)),
  			bar_heights,
        yerr=bar_errors,
       capsize=5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Amount')
plt.title('Order Amount over Time')
plt.show()



from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print customer_amount.head()

plt.hist(customer_amount.price.values,
        range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel("Number of Customers")
plt.title('Customer Expenditure Over 6 Months')

plt.show()




# ANALYZE FARMBURG'S A/B TEST

import pandas as pd

df = pd.read_csv('clicks.csv')

df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

purchase_counts = df.groupby(['group', 'is_purchase'])\
	.user_id.count().reset_index()

print purchase_counts


# Performing a Significance Test

from scipy.stats import chi2_contingency

contingency = [[316, 1350],
           [183, 1483],
           [83, 1583]]

chi2_stat, pvalue, dof, t = chi2_contingency(contingency)

print pvalue


# Calculating Necessary Purchase Rates

import pandas as pd

df = pd.read_csv('clicks.csv')

df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

purchase_counts = df.groupby(['group', 'is_purchase'])\
	.user_id.count().reset_index()

print purchase_counts

num_visits = len(df)

p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits

from scipy.stats import binom_test

pvalueA = binom_test(316, 1666, p_clicks_099)
pvalueB = binom_test(183, 1666, p_clicks_199)
pvalueC = binom_test(83, 1666, p_clicks_499)

final_answer = 4.99










is_significant = True