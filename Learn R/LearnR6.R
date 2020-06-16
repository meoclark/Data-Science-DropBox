# JOINING TABLES IN R


# Joining
# Was about locating each id using its number in another data frame

# Inner Join I
# The inner_join() method looks for columns that are common between two data frames and then looks for rows where those columns’ values are the same. It then combines the matching rows into a single row in a new table.

joined_df <- orders %>%
  inner_join(customers)

---
title: "Joining Tables in R"
output: html_notebook
---

```{r message = FALSE}
# load packages
library(readr)
library(dplyr)
```

```{r message = FALSE}
# load sales and targets data
sales <- read_csv("sales.csv")
targets <- read_csv("targets.csv")
```

```{r}
# inspect orders, customers and products
head(sales)
head(targets)
```

```{r}
# define sales_vs_targets here:
sales_vs_targets <- sales %>% inner_join(targets)

```

```{r}
# define crushing_it here: where revenue is greater than targets
crushing_it <- sales_vs_targets %>%
  filter(revenue > target)

```


# Inner Join II

# In addition to using inner_join() to join two data frames together, we can use the pipe %>% to join multiple data frames together at once.
big_df <- orders %>%
  inner_join(customers) %>%
  inner_join(products)

```{r message = FALSE}
# load and inspect sales and targets data
sales <- read_csv("sales.csv")
targets <- read_csv("targets.csv")
head(sales)
head(targets)
```

```{r}
# load men_women data here:
men_women <- read_csv('men_women_sales.csv')

# inspect men_women here:
head(men_women)
```

```{r}
# define all_data here:
all_data <- sales %>% inner_join(targets) %>% inner_join(men_women)

head(all_data)

```

```{r}
# define results here:
results <- all_data  %>% filter(revenue > target, women > men)

head(results)
```

# Join on Specific Columns I

# You must ensure their column names are well named to avoid getting confused

```{r}
# rename the id column of products here:
products <- products %>% rename(product_id = id)


```

```{r}
# define orders_products here:
orders_products <- orders %>% inner_join(products)

head(orders_products)


# Join on Specific Columns II

#We can add the "by" argument when calling inner_join() to specify which columns we want to join on.

orders %>% 
  inner_join(customers,
             by = c('customer_id' = 'id'),
             suffix = c('_order','_customer'))

# The above will match the id from orders to customer_id
# Two id columns will be formed id_x and id_y so we use the suffix() to add a more clear column name


```{r}
# inspect orders and products
head(orders)
head(products)
```

```{r}
# define orders_products here:
orders_products <- orders %>% inner_join(products,by = c('product_id' = 'id'))

orders_products

```

```{r}
# define products_orders here:
products_orders <- products %>% inner_join(orders,by = c('id' = 'product_id'), suffix = c('_product','_order'))


products_orders

```

# Mismatched Joins

```{r}
# define orders_products here:
orders_products <- orders %>% inner_join(products)

orders_products

# The new product disappeared oo! we lost it
```

# Full Join
# To account for the above mismatched rows we use full_join 
# we could use a Full Join. A Full Join would include all rows from both tables, even if they don’t match. Any missing values are filled in with NA.

full_joined_dfs <- company_a %>%
  full_join(company_b)


```{r}
# inspect store_a and store_b
head(store_a)
head(store_b)
```

```{r}
# define store_a_b_full here:
store_a_b_full <- store_a %>% full_join(store_b)

store_a_b_full
```

# Left and Right Joins

# Left join
left_joined_df <- company_a %>%
  left_join(company_b)
#By listing company_a first, we get all customers from Company A, and only customers from Company B who are also customers of Company A.

# Right join
right_joined_df <- company_a %>%
  right_join(company_b)
# By listing company_a first and company_b second, we get all customers from Company B, and only customers from Company A who are also customers of Company B.


```{r}
# define left_a_b here:
left_a_b <- store_a %>% left_join(store_b)

left_a_b 
```

```{r}
# define left_b_a here:
left_b_a <- store_a %>% right_join(store_b)

left_b_a
```

# Concatenate Data Frames

# When we need to reconstruct a single data frame from multiple smaller data frames, we can use the dplyr bind_rows() method.
# This method only works if all of the columns are the same in all of the data frames.
concatenated_dfs <- df1 %>%
  bind_rows(df_2)

```{r}
# inspect bakery and ice_cream
head(bakery)
head(ice_cream)
```

```{r}
# define menu here:
menu <- bakery %>% bind_rows(ice_cream)

menu
```

# REVIEW

```{r}
# define v_to_c here:
v_to_c <- visits %>% inner_join(checkouts)

v_to_c
```

```{r}
# define avg_time_to_check here:
v_to_c <- v_to_c %>% 
  mutate(time = checkout_time - visit_time)
v_to_c

# To get the average time to checkout

avg_time_to_check <- v_to_c %>% 
  summarize(mean_time = mean(time))
avg_time_to_check

```


