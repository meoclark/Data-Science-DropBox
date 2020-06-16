---
title: "Standard Deviation"
output: html_notebook
---
```{r message=FALSE, warning=FALSE, error=TRUE}
library(readr)
library(dplyr)
```

```{r error=TRUE}
load("project.Rda")
```

```{r error=TRUE}
# Change these variables to be the standard deviation of each dataset.
# Inspect Data

#head(london_data)
print(nrow(london_data))

# To get a single column from a DataFrame, you can use this syntax:
temp <- london_data$TemperatureC
# Average temperature
average_temp <- mean(temp)
average_temp

temperature_var <- variance(temp)
print(temperature_var)
# Variance and SD for the year
temperature_standard_deviation <- sd(temp)
print(temperature_standard_deviation)



#Inspect once again
head(london_data)

# Get monthly temperature average
june <- london_data %>%
  filter(month == "06")

july <- london_data %>%
  filter(month == "07")
# Analyze by month
print(mean(june$TemperatureC))
print(mean(july$TemperatureC))

print(sd(june$TemperatureC))
print(sd(july$TemperatureC))

# Analyze by month
monthly_stats <- london_data %>%
    group_by(month) %>%
    summarize(mean = mean(TemperatureC),
              standard_deviation = sd(TemperatureC))

monthly_stats
```