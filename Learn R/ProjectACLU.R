---
title: "ACLU Child Separations"
output: html_notebook
---

```{r message=FALSE, warning=FALSE, error=TRUE}
# load libraries
library(dplyr)
library(readr)

```

```{r error=TRUE}
# load data
aclu <- read_csv('aclu_separations.csv')
```

```{r error=TRUE}
# inspect data
head(aclu)
summary(aclu)

```

```{r error=TRUE}
# select columns
aclu <- aclu %>% select(-addr)


```

```{r error=TRUE}
# view columns
print(colnames(aclu))
```

```{r error=TRUE}
# rename columns
aclu <- aclu %>% rename(city = program_city, state = program_state,number_children = n,longitude = lon, latitude = lat)
print(colnames(aclu))





```

```{r error=TRUE}
# add column
border_latitude = 25.83
aclu <- aclu %>% mutate(lat_change_border =  latitude - border_latitude)
head(aclu)


```

```{r error=TRUE}
# latitude change
further_away <- aclu %>% filter(lat_change_border > 15)
head(further_away)%>%arrange(desc(lat_change_border))


```

```{r error=TRUE}
# number of children
ordered_by_children <- aclu %>% arrange(desc(number_children))
head(ordered_by_children)


```

```{r error=TRUE}
# state analysis
chosen_state = "NY"
chosen_state_separations <- aclu %>% filter(state == chosen_state)%>%arrange(desc(number_children))
head(chosen_state_separations)



```