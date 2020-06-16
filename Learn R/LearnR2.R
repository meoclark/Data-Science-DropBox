 # MODIFYING DATA FRAMES IN R

 ---
title: "Modifying Data Frames in R"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
```

```{r}
# load data frame
dogs <- read_csv('dogs.csv')
```

```{r}
# inspect data frame
head(dogs)
```

```{r}
# rename columns
dogs <- dogs %>%
  rename(popularity_2016 = rank_2016,
        popularity_2015 = rank_2015,
        popularity_2014 = rank_2014,
        popularity_2013 = rank_2013)
colnames(dogs)
```

```{r}
# calculate average height, average weight, and change in popularity from 2013 to 2016
dogs <- dogs %>%
  transmute(breed = breed,
            avg_height = (height_low_inches + height_high_inches)/2,
            avg_weight = (weight_low_lbs + weight_high_lbs)/2,
            pop_change_13_to_16 = popularity_2016 - popularity_2013)
head(dogs)
```

# Adding a Column

```{r}
#You can add a new column to the data frame using the mutate() function.
#The following code multiplies each price by 0.075, the sales tax in your state:
df %>%
  mutate(sales_tax = price * 0.075)
#a new Column with name sales_tax is added with the tax showing in each row

# inspect data frame
head(dogs)
```

```{r}
# add average height column
dogs <- dogs %>% 
mutate(avg_height = (height_low_inches + height_high_inches) / 2)
head(dogs)


```

# Adding Multiple Columns
```{r}
# add average height, average weight and rank change columns
dogs <- dogs %>%
  mutate(avg_height = (height_low_inches + height_high_inches)/2, avg_weight = (weight_low_lbs + weight_high_lbs) / 2 ,rank_change_13_to_16 = (rank_2016 - rank_2013) )

head(dogs )

```

# Transmute Columns
# This will create new columns and remove all the existing ones
```{r}
# update the function call to drop all existing columns
dogs <- dogs %>%
  transmute(breed = breed,avg_height = (height_low_inches + height_high_inches)/2,
         avg_weight = (weight_low_lbs + weight_high_lbs)/2,
        rank_change_13_to_16 = rank_2016 - rank_2013)
head(dogs)

# breed = breed makes sure the breed column is not dropped.
```

# Rename Columns
```{r}
#To get the column names of a data frame, use colnames() or names() with the data frame as an argument.
# check column names
original_col_names <- colnames(dogs)
original_col_names
```

```{r}
# rename data frame columns
dogs <- dogs %>%
  rename(avg_height_inches = avg_height,
         avg_weight_lbs = avg_weight,
         popularity_change_13_to_16 = rank_change_13_to_16)
```

```{r}
# check column names
new_col_names <- colnames(dogs)
new_col_names
```

# REVIEW

```{r}
# add new columns, drop existing columns and arrange
dogs <- dogs %>% transmute(breed = breed,height_average_feet = ((height_low_inches + height_high_inches)/2)/12, popularity_change_15_to_16 = (rank_2016 - rank_2015) )%>%arrange(desc(popularity_change_15_to_16))
head(dogs)

```
