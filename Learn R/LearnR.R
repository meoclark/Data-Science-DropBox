---
title: "Introduction to R Syntax"
output: html_notebook
---
```{r}
#Calculation 
25 * 4 + 9 / 3
```

```{r}
#Datatypes :Numeric,character,Vectors,NA,Logical[TRUE>FALSE]
print("Moses Egbo")
print(24)

print('24')
```

```{r}
#Variables note you can also assign with =
name <- "Meo Clark"
age <- 24
```

```{r}
# Vectors :this works like a list. The indexing starts at 1 not 0 e.g phone[1] will grab 234
#typeof(vector_name) checks the type, length(vector_name) checks the length of the vector
#vectors can only hold items of the same data-type
phone <- c(234,042,3454)
```

```{r}
# Conditionals

message <- "I change based on a condition."
if (TRUE){
  message = "I execute this when true!"
  print(message)
} else {
  print("I execute this when false!")
}

age = 19
if (age >= 18 & registered == TRUE) {
  can_vote <- TRUE
} else {
  can_vote <- FALSE
}
```

```{r}
#Comparism operators
56 >= 129
56 !=129
```

```{r}
# Logical operators & | !
message <- 'Should I pack an umbrella?'
weather <- 'cloudy'
high_chance_of_rain <- TRUE


if (weather == 'cloudy' & high_chance_of_rain) {
  message <- "Pack umbrella!"
} else {
  message <- "No need for umbrella!"
}

print(message)

```

```{r}
#Calling Function
#unique() prints out only the unique values in the vector

data <- c(120,22,22,31,15,120)
unique_vals = unique(data)
print(unique_vals)

solution =sqrt(49)
print(solution)

#rounds a decimal down to the next integer
round_down = floor(3.14)
print(round_down)

#rounds a decimal up to the next integer
round_up = ceiling(3.14)
print(round_up)

sort(c(2,4,10,5,1)); # Outputs c(1,2,4,5,10)
length(c(2,4,10,5,1)); # Outputs 5
sum(5,15,10) #outputs 30

```

```{r}
#To install a package use install.packages('package-name')

#To import
# load libraries
library(dplyr)
library(readr)
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
artists %>%
  select(-country,-year_founded,-albums) %>%
  filter(spotify_monthly_listeners > 20000000, genre != 'Hip Hop') %>%
  arrange(desc(youtube_subscribers))
```

# First project

```{r error=TRUE}
calculate_annual_growth <- function(year_one,year_two,pop_y1, pop_y2,city) {
  annual_growth <- (((pop_y2 - pop_y1) / pop_y1) * 100) / (year_two-year_one)
  message <- paste("From", year_one, "to", year_two, "the population of", city, "grew by approximately", annual_growth, "% each year.")
  print(message)
  return(annual_growth)
}
 # Project calculating population change over time with R

# Write your code starting here:
city_name <- "Istanbul, Turkey"
pop_year_one <- 691000
pop_year_two <- 15029231

pop_change <- pop_year_two - pop_year_one
print(pop_change)

percentage_gr <- ((pop_change/pop_year_one) * 100)

annual_gr <- percentage_gr / (2017-1927)
print(annual_gr)

calculate_annual_growth(1950,2000,983000,15029231,"Istanbul, Turkey")

```

