# MEAN IN R

title: "Mean in R"
output: html_notebook
---
```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
library(ggplot2)

# load data frame
greatest_books <- read_csv('top-hundred-books.csv')

#plot data
hist <- qplot(greatest_books$Ages,
      geom='histogram',
      binwidth = 3,  
      main = 'Age of Top 100 Novel Authors at Publication', 
      xlab = 'Publication Age',
      ylab = 'Count',
      fill=I("blue"), 
      col=I("red"), 
      alpha=I(.2)) 

hist
```

```{r}
total <- 29 + 49 + 42 + 43
print(total)

mean_value <- total / 4
print(mean_value)
```

# Set author ages to a vector
author_ages <- greatest_books$Ages

# Use R to calculate mean
average_age <- mean(author_ages)
print(average_age)


# Review
#plot data
hist <- qplot(greatest_books$Ages,
      geom='histogram',
      binwidth = 3,  
      main = 'Age of Top 100 Novel Authors at Publication', 
      xlab = 'Publication Age',
      ylab = 'Count',
      fill=I("blue"), 
      col=I("red"), 
      alpha=I(.2)) +
  geom_vline(aes(xintercept=mean(greatest_books$Ages),
                 color="mean"), linetype="solid",
             size=1) +
  scale_color_manual(name = "statistics", values = c(mean = "red"))

hist


# MEDIAN IN R


# There are always two steps to finding the median of a dataset:

# 1. Order the values in the dataset from smallest to largest
# 2. Identify the number(s) that fall(s) in the middle


# Array of the first five author ages
five_author_ages <- c(29, 49, 42, 43, 32)

# Fill in the empty array with the values sorted
sorted_author_ages <- c(29, 32, 42, 43, 49)

# Save the median value to median_value
median_value <- 42

# Print the sorted array and median value
cat("The sorted array is:", sorted_author_ages)
cat(paste("The median of the array is: ", median_value))

# Save author ages to author_ages
author_ages <- greatest_books$Ages

# Use R to calculate the median age of the top 100 authors
median_age <- median(author_ages)

print(median_age)

print(paste("The median age of the 100 greatest authors, according to a survey by Le Monde is: " , median_age))

# Review
#plot data
hist <- qplot(greatest_books$Ages,
      geom='histogram',
      binwidth = 3,  
      main = 'Age of Top 100 Novel Authors at Publication', 
      xlab = 'Publication Age',
      ylab = 'Count',
      fill=I("blue"), 
      col=I("red"), 
      alpha=I(.2)) +
  geom_vline(aes(xintercept=median(greatest_books$Ages),
                 color="median"), linetype="dashed",
             size=1) +
  geom_vline(aes(xintercept=mean(greatest_books$Ages),
                 color="mean"), linetype="solid",
             size=1) +
  scale_color_manual(name = "statistics", values = c(median = "blue", mean = "red"))

hist


# MODE IN R

# The most frequently occurring observation in the dataset. 
# A dataset can have multiple modes if there is more than one value with the same maximum frequency.

# The R package DescTools includes a handy Mode() function which can do the work of finding the mode for us.

# Set author ages to 
author_ages <- greatest_books$Ages

mode_age <- Mode(author_ages)

print(paste("The mode age of authors from Le Monde's 100 greatest books is: ", mode_age[1]))


