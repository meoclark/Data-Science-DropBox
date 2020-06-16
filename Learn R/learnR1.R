# Introduction to Data Frames
---
title: "Introduction to Data Frames"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)

```

```{r}
# load data frame
artists <- read_csv('artists.csv')
```

```{r}
# inspect data frame
artists
head(artists)
summary(artists)
```

```{r}
# select columns, filter and arrange rows of artists
artists_manipulated <- artists %>% 
  select(-country,-year_founded,-albums) %>% 
  filter(spotify_monthly_listeners > 20000000, genre != 'Hip Hop') %>% 
  arrange(desc(youtube_subscribers))
artists_manipulated
```

# Tibbles are modern versions of data frames in R,
# and they operate in essentially the same way. The terms tibble and data frame are often used interchangeably.

# To Load a data Frame
```{r}
# load libraries
library(readr)
library(dplyr)
```

```{r}
# load data frame
songs <- read_csv('songs.csv')
```

```{r}
songs
```

```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
```

```{r}
# load data frame
artists <- read_csv('artists.csv')

#You can also save data from a data frame to a CSV using readr‘s write_csv() function
# it takes two argument, 1 the data frame df, 2 the name of the csv file
write_csv(df,'new_csv_file.csv')
```

# Inspecting Data Frames
```{r}
# The head() function returns the first 6 rows of a data frame.
#you can pass an additional argument n to head(). For example, head(df,8) will show the first 8 rows.
# The function summary() will return summary statistics such as mean, median, minimum and maximum 
#for each numeric column while providing class and length information for non-numeric columns.

# inspect data frame
artists
head(artists)
summary(artists)

```
# Piping

```{r message=FALSE}
# load data frame
artists <- read_csv('artists.csv')
```

```{r}
#The pipe operator, or %>%, helps increase the readability of data frame code by piping the value on
# its left into the first argument of the function that follows it. For example:

df %>%
  head()
#pipes the data frame df into the first argument of head(), becoming

head(df)

# inspect data frame with pipe

artists %>% head()
```

# Selecting Data frames

```{r}
#You can select the appropriate columns for your analysis using dplyr‘s select() function:

select(customers,age,gender)
#select() takes a data frame as its first argument
#all additional arguments are the desired columns to select
#select() returns a new data frame containing only the desired columns

#You can simplify the readability of your code by using the pipe:

customers %>%
  select(age,gender)


# select one column
artist_groups <- artists %>% select(group)
artist_groups

```

```{r}
# select multiple columns
group_info <- artists%>%select(group,spotify_monthly_listeners,year_founded)
group_info


```
# Excluding Columns

```{r}
#To exclude the columns you do not need:

customers %>%
  select(-name,-phone)
#the data frame customers is piped into select()
#the columns to remove, prepended with a -, are given as arguments



# select all columns except one
no_albums <- artists %>% 
        select(-albums)
no_albums

```

```{r}
# select all columns except a set
df_cols_removed <- artists %>% 
select(-genre, -spotify_monthly_listeners, -year_founded)
df_cols_removed 
```


# Filtering Rows with Logic I
```{r}
#you can also subset a data frame by rows using dplyr’s filter() function and comparison operators!

#Let’s say you want to find all orders made by customers with the first name 'Joyce'.

orders %>%
  filter(first_name == 'Joyce')
#What if you have multiple conditions you want to be met? Not a problem
orders %>%
  filter(shoe_material == 'faux-leather',price > 25)
#You can provide any number of conditions that you please, as long as you separate each condition 
#by a comma as its own argument. Note: each condition that you list must be met for a row to be returned!

# filter rows one condition
rock_groups <- artists %>% filter(genre == 'Rock')
rock_groups

```

```{r}
# filter rows multiple conditions
popular_rock_groups <- artists %>% filter(genre == 'Rock',spotify_monthly_listeners > 20000000 )
popular_rock_groups


```

# Filtering Rows with Logic II

```{r}
# filter rows with or
korea_or_before_2000 <- artists %>% 
  filter(country == 'South Korea' | year_founded < 2000)
korea_or_before_2000
```

```{r}
# filter rows with not !
#This will print only rows that are not rock music
not_rock_groups <- artists %>% 
  filter(!(genre == 'Rock'))
not_rock_groups
```


# Arranging Rows
```{r}
#arrange() will sort the rows of a data frame in ascending order by the column provided as an argument

# arrange rows in ascending order
group_asc <- artists %>% arrange(group)
group_asc

```

```{r}
#arrange() can also order rows by descending order! arrange(desc(age))

# arrange rows in descending order

youtube_desc <- artists %>% arrange(desc(youtube_subscribers))
youtube_desc


#If multiple arguments are provided to arrange(), it will order the rows by the column 
#given as the first argument and use the additional columns 
#to break ties in the values of preceding columns.
```

# REVIEW

---
title: "Introduction to Data Frames in R"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
```

```{r message=FALSE}
# load data frame
artists <- read_csv('artists.csv')
```

```{r}
# select columns
chosen_cols <- artists %>% 
  select(-country,-year_founded,-albums)
head(chosen_cols)
```

```{r}
# filter rows
popular_not_hip_hop <- chosen_cols %>% 
  filter(spotify_monthly_listeners > 20000000, genre != 'Hip Hop') 
head(popular_not_hip_hop)
```

```{r}
# arrange rows
youtube_desc <- popular_not_hip_hop %>% 
  arrange(desc(youtube_subscribers))
head(youtube_desc)
```

# The code below does exactly what the above one does but in one line and using one data fame.

```{r}
# select columns, filter and arrange rows
artists <- artists %>% select(-country,-year_founded,-albums)%>%filter(spotify_monthly_listeners > 20000000, genre != 'Hip Hop')%>%arrange(desc(youtube_subscribers))

head(artists)




```




