# AGGREGATES IN R

---
title: "Aggregates in R"
output: html_notebook
---

```{r message = FALSE}
# load packages
library(readr)
library(dplyr)
```

```{r message = FALSE}
# load data
orders <- read_csv("orders.csv")
page_visits <- read_csv("page_visits.csv")
```

```{r}
# inspect data frames
head(orders)
head(page_visits)
```

```{r}
# average price of order
average_price <- orders %>% 
  summarize(mean_price = mean(price, na.rm = TRUE))
average_price
```

```{r}
# page visits by UTM source
click_source <- page_visits %>%
  group_by(utm_source) %>%
  summarize(count = n())
click_source
```

```{r}
# page visits by UTM source and month
click_source_by_month <- page_visits %>%
  group_by(utm_source,month) %>%
  summarize(count = n())
click_source_by_month
```

# Calculating Column Statistics

# This can be done with the help of the dplyr function summarize(),which returns a new data frame containing the desired calculation.

#The general syntax for these calculations is:

df %>%
  summarize(var_name = command(column_name))
#df is the data frame you are working with
#summarize is a dplyr function that reduces multiple values to a single value
#var_name is the name you assign to the column that stores the results of the summary function in the returned data frame
#command is the summary function that is applied to the column by summarize()
#column_name is the name of the column of df that is being summarized

# The following table includes common summary functions that can be given as an argument to summarize():

mean()	Average of all values in column
median()	Median value of column
sd()	Standard deviation of column
var()	Variance of column
min()	Minimum value in column
max()	Maximum value in column
IQR()	Interquartile range of column
n_distinct()	Number of unique values in column
sum()	Sum values of column


```{r message = FALSE}
# load order data
orders <- read_csv("orders.csv")

# inspect orders here:
head(orders,10)
```

```{r}
# define most_expensive here:

# na.rm = TRUE
# Add the following as an additional argument to max() so that it removes all missing values before computing the maximum value.

most_expensive <- orders %>% summarize(most_expensive = max(price,na.rm = TRUE))
print(most_expensive)
```

```{r}
# define num_colors here:
num_colors <- orders %>% summarize(num_colors = n_distinct(shoe_color))
print(num_colors)

```


# Calculating Aggregate Functions I

# To find the aggregates pertaining to  group we use the groupby() function

grades <- df %>%
  group_by(student) %>%
  summarize(mean_grade = mean(grade))

# In general, we use the following syntax to calculate aggregates:

df %>%
  group_by(column_1) %>%
  summarize(aggregate_name = command(column_2))

#column_1 (student in our example) is the column that we want to group_by()
#column_2 (grade in our example) is the column that we want to apply command(), a summary function, to using summarize()
#aggregate_name is the name assigned to the calculated aggregate

# n() will return the count of the rows within a group, and does not require a column as an argument
 # To get the count of the rows in each group of students from our example:


```{r}
# define pricey_shoes here:
pricey_shoes <- orders %>%
  group_by(shoe_type) %>%
  summarize(max_price = max(price, na.rm = TRUE))
pricey_shoes
```

```{r}
# The inventory team wants to know how many of each shoe_type has been sold so they can forecast inventory for the future.

# define shoes_sold here:for n()

# You must specify the argument count as count 
shoes_sold <- orders %>%
  group_by(shoe_type) %>%
  summarize(count = n())
shoes_sold
```


# Calculating Aggregate Functions II


# Sometimes, we want to group by more than one column. We can do this by passing multiple column names as arguments to the group_by function.

df %>%
  group_by(location,day_of_week) %>%
  summarize(mean_total_sales = mean(total_sales))

 ```{r}
# define shoe_counts here:

shoe_counts <- orders %>%
  group_by(shoe_type,shoe_color) %>%
  summarize(count = n())

shoe_counts



```

```{r}
# define shoe_prices here:
shoe_prices <- orders %>%
  group_by(shoe_type,shoe_material) %>%
  summarize(mean_price = mean(price,na.rm = TRUE))



shoe_prices



```

# Combining Grouping with Filter


enrollments %>%
  group_by(course) %>%

  filter(mean(quiz_score) < 80)


group_by() groups the data frame by course into two groups: learn-r and learn-python
filter() will keep all the rows of the data frame whose per-group (per-course) average quiz_score is less than 80

```{r}
# define most_pop_orders here:
most_pop_orders <- orders %>%
group_by(shoe_type)%>%
filter( n() > 16)


most_pop_orders

```


# Combining Grouping with Mutate

```{r}
# define diff_from_mean here:
diff_from_mean = orders %>% group_by(shoe_type) %>%
mutate(diff_from_shoe_type_mean = price - mean(price,na.rm = TRUE))

diff_from_mean


```

 # REVIEW


---
title: "Aggregates in R"
output: html_notebook
---

```{r message = FALSE}
# load packages
library(readr)
library(dplyr)
```

```{r message = FALSE}
# load data
orders <- read_csv("orders.csv")
page_visits <- read_csv("page_visits.csv")
```

```{r}
# inspect data frames
head(orders)
head(page_visits)
```

```{r}
# define average_price here:
average_price <- orders %>% summarize(avg_price = mean(price,na.rm = TRUE))

average_price
```

```{r}
# define click_source here:
click_source <- page_visits %>% group_by(utm_source) %>% summarize(count = n())


click_source
```

```{r}
# define click_source_by_month here:
click_source_by_month <- page_visits %>% group_by(utm_source,month) %>% summarize(count = n())


click_source_by_month

```