---
title: "Page Visits Funnel"
output: html_notebook
---

```{r message = FALSE, error=TRUE}
# load packages
library(readr)
library(dplyr)
```

```{r message = FALSE, error=TRUE}
# load data
visits <- read_csv("visits.csv")
cart <- read_csv("cart.csv")
checkout <- read_csv("checkout.csv")
purchase <- read_csv("purchase.csv")
```

```{r error=TRUE}
# inspect data frames
head(visits)
head(cart)
head(checkout)
head(purchase)
```

```{r error=TRUE}
# define visits_cart here:
visits_cart <- visits %>% left_join(cart)

visits_cart

```

```{r error=TRUE}
# define total_visits here:
visits %>% nrow()

```

```{r error=TRUE}
# define visit_no_cart here:
visits_cart %>% filter(is.na(cart_time))


```

```{r error=TRUE}
# calculate visit_no_cart_percent here:
No_cart_percent = 1652/2000 * 100
No_cart_percent
# 82.6%
```

```{r error=TRUE}
# define cart_checkout here:
cart_checkout <- cart %>% left_join(checkout)

cart_checkout

cart_checkout %>% filter(is.na(checkout_time))

cart_but_no_checkout_percent = 122/348 * 100
cart_but_no_checkout_percent
#35.1%
```

```{r error=TRUE}
# define total_carts here:


```

```{r error=TRUE}
# define cart_no_checkout here:




```

```{r error=TRUE}
# calculate cart_no_checkout_percent here:


```

```{r error=TRUE}
# define all_data here:

all_data <- visits %>% left_join(cart) %>% left_join(checkout) %>% left_join(purchase)

all_data



```

```{r error=TRUE}
# define total_checkout here:
all_data %>% filter(is.na(checkout_time))

```

```{r error=TRUE}
# define checkout_no_purchase here:
didnt_purchase = 1774/2000 * 100

didnt_purchase
#88.7
```

```{r error=TRUE}
# calculate checkout_no_purchase_percent here:


```

```{r error=TRUE}
# update all_data with time_to_purchase column here:
all_data <- all_data %>%
  mutate(time_to_purchase = purchase_time - visit_time)

```

```{r error=TRUE}
# inspect the updated all_data data frame here:
head(all_data)
```

```{r error=TRUE}
# define time_to_purchase here:

time_to_purchase <- all_data %>%
  summarize(mean_time = mean(time_to_purchase, na.rm = TRUE))
time_to_purchase

```