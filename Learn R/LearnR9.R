# QUARTILES


# Q2
---
title: "Quartiles"
output: html_notebook
---

```{r}
#  second quartile (Q2). Q2 happens to be exactly the median. Make sure you sort the data.

dataset_one <- c(50, 10, 4, -3, 4, -20, 2)
# sorted dataset_one: c(-20, -3, 2, 4, 4, 10, 50)

dataset_two <- c(24, 20, 1, 45, -15, 40)

# define the second quartile of both datasets here:
dataset_one_q2 <-  4 
dataset_two_q2 <- 22
```

# Q1 and Q3
# from the Q2 take median to the left to find the Quartile 1 and to the Right to find the Quartile 2

# define the first and third quartile of both datasets here:
dataset_one_q1 <- -3
dataset_one_q3 <- 10

dataset_two_q1 <- 1
dataset_two_q3 <- 40


```

# Method Two: Including Q2

# Note that there is no universally agreed upon method of calculating quartiles,
# and as a result, two different tools might report different results.
#  Using this second method, we include Q2 in each half.

```{r}
dataset_one <- c(50, 10, 4, -3, 4, -20, 2)
# sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]

dataset_two <- c(24, 20, 1, 45, -15, 40)
# sorted [-15,1,20,24,40,45]
dataset_one_q2 <- 4
dataset_two_q2 <- 22

# define the first and third quartile of both datasets here:

dataset_one_q1 <- -0.5
dataset_one_q3 <- 7

dataset_two_q1 <- 1
dataset_two_q3 <- 40

```

```{r}


# Quartiles in R


# The quantile() function takes two parameters.
# The first is the dataset you’re interested in. The second is a number between 0 and 1.

```{r}
# create the variables songs_q1, songs_q2, and songs_q3 here:
songs_q1 <- quantile(songs,0.25)
songs_q2 <- quantile(songs,0.50)
songs_q3 <- quantile(songs,0.75)
```

```{r}

# REVIEW
# plot histogram
hist <- qplot(songs,
              geom="histogram",
              main = 'Histogram of Song Lengths',
              xlab = 'Song Length (Seconds)',
              ylab = 'Count',
              fill=I("blue"),
              col=I("red"),
              alpha=I(.2)) +
        geom_vline(aes(xintercept=quantile(songs,0.25),
                       color=I("blue")),
                   linetype="solid",
                   size=1,
                   show.legend=T) +
				geom_vline(aes(xintercept=quantile(songs,0.5),
                       color=I("purple")),
                   linetype="solid",
                   size=1,
                   show.legend=T) +
  			geom_vline(aes(xintercept=quantile(songs,0.75),
                       color=I("yellow")),
                   linetype="solid",
                   size=1,
                   show.legend=T) + 
				scale_colour_manual(name = "",
                            labels =c("Q1","Q2","Q3"),
                            values=c("blue","purple","yellow"))

hist





# Quantiles in R


```{r}
# define twenty_third_percentile here:
twenty_third_percentile <- quantile(songs,0.23)
```

```{r}

```{r}
# define quartiles and deciles here:
quartiles <- quantile(songs,c(0.25, 0.5, 0.75))

```

```{r}
# define tenth here:
deciles <- quantile(songs,c(0.1, 0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9))

tenth <- 3


```
```{r}
# load song data
load("songs.Rda")
```

```{r}
# define percentile and answer here:
percentile <- quantile(songs,0.32)
answer = "below"
```


# INTERQUARTILE RANGE

# The interquartile range (IQR) is a descriptive statistic that tries to solve this problem. 
# The IQR ignores the tails of the dataset, so you know the range around-which your data is centered
# Interquartile is the difference btw first quartile and third quartile

```{r}
# find the first quartile
q1 <- quantile(songs,0.25)
```

```{r}
# calculate the third quartile here:
q3 <- quantile(songs,0.75)
```

```{r}
# calculate the interquartile range here:
interquartile_range <- q3 - q1
```

```{r}

# IQR in R

# The IQR() function takes a dataset as a parameter and returns the Interquartile Range.

```{r}
# create the variable interquartile_range here
interquartile_range <- IQR(songs)
```

```{r}

# REVIEW
```{r}
# small dataset
dataset = c(-50, -24, -13, -2, 0, 12, 15, 18, 73, 90, 100)

# calculate range and IQR
dataset_range = max(dataset) - min(dataset)
dataset_iqr = IQR(dataset)

# print range and IQR
print(paste("The range of the dataset is ",dataset_range))
print(paste("The IQR of the dataset is ",dataset_iqr))
```

