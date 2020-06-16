# WORKING WITH MULTIPLE DATAFRAMES

# Introduction: Multiple DataFrames

# We can call the pd.merge method with two tables like this:

new_df = pd.merge(orders, customers)

import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)

print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# The following command would merge orders to customers, and then the resulting DataFrame to products:

big_df = orders.merge(customers)\
    .merge(products)


import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)
print(all_data)


results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

# Merge on Specific Columns


orders_products = pd.merge(orders,products.rename(columns={'id':'customer_id'}))

print(orders_products)

# Merge on Specific Columns II


orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

# Use left_on and right_on to merge orders and products
orders_products = pd.merge(
	orders,
	products,
	left_on = 'product_id',
	right_on = 'id',
	suffixes = ['_orders', '_products']
)

print(orders_products)


# Outer Merge
store_a_b_outer = pd.merge(store_a,store_b,how = 'outer')

print(store_a_b_outer)


# Left and Right Merge

store_a_b_left = pd.merge(store_a,store_b,how = 'left')
store_b_a_left = pd.merge(store_a,store_b,how = 'right')

print(store_a_b_left)
print(store_b_a_left)


# Concatenate DataFrames

menu = pd.concat([bakery,ice_cream])
print(menu)


# REVIEW


import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits)
print(checkouts)

v_to_c =  pd.merge(visits,checkouts)


v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time

print(v_to_c)

print(v_to_c.time.mean())


# Project Page Funnel Visit

import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())


visits_cart = pd.merge(visits,cart, how = 'left')
print(visits_cart)

nat = visits_cart[visits_cart.cart_time.isnull()]
allva = visits_cart['cart_time']

percentage = (len(nat) / float(len(allva)) ) * 100

print(percentage)
# 80.5%


cart_checkout =pd.merge(cart,checkout, how = 'left')
#print(cart_checkout)

cat_null = cart_checkout[cart_checkout.checkout_time.isnull()]
all_cat = cart_checkout['checkout_time']

percent = (len(cat_null) / float(len(all_cat))) * 100
print(percent)
# 20.93%
all_data = visits.merge(cart).merge(checkout).merge(purchase)
print(all_data.head())

shirt_null = all_data[all_data.checkout_time.isnull()]
shirt_all = all_data['checkout_time']

percenta = (len(shirt_null) / float(len(shirt_all))) * 100
print(percenta)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time


print(all_data.time_to_purchase)


print(all_data.time_to_purchase.mean())

