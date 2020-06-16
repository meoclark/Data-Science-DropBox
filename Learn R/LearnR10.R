# HYPOTHESIS TESTING WITH R

# Statistical hypothesis testing is a process that allows you to evaluate if a change or difference
# seen in a dataset is “real”, or if it’s just a result of random fluctuation in the data.

---
title: "Hypothesis Testing in R"
output: html_notebook
---

```{r message = FALSE}
# load data
load("week_1.Rda")
load("week_2.Rda")
```

```{r}
# calculate week_1_mean and week_2_mean:
week_1_mean <- mean(week_1)
week_1_mean
week_2_mean <- mean(week_2)
week_2_mean
```

```{r}
# calculate week_1_sd and week_2_sd:
week_1_sd <- sd(week_1)
week_1_sd
week_2_sd <- sd(week_2)
week_2_sd
```

```{r}
# run two sample t-test:
results <- t.test(week_1,week_2)
results
```


# Sample Mean and Population Mean - I


```{r}
# generate random population
population <- rnorm(300, mean=65, sd=3.5)

# calculate population mean here:
population_mean <- mean(population)
population_mean
```

```{r}
# generate sample 1
sample_1 <- sample(population, size=30)
sample_1

# calculate sample 1 mean
sample_1_mean <- mean(sample_1)
sample_1_mean
```

```{r}
# generate samples 2,3,4 and 5
sample_2 <- sample(population, size=30)
sample_3 <- sample(population, size=30)
sample_4 <- sample(population, size=30)
sample_5 <- sample(population, size=30)
```

```{r}
# calculate sample means here:
sample_2_mean <- mean(sample_2)
sample_2_mean
sample_3_mean <-mean(sample_3)
sample_3_mean
sample_4_mean <-mean(sample_4)
sample_4_mean
sample_5_mean <- mean(sample_5)
sample_5_mean
```


# Sample Mean and Population Mean - II

# Sampling error,occurs when a sample is not representative of the population it comes from. 

# There is one surefire way to mitigate the risk of having a skewed sample mean — take a larger set of samples!
# The sample mean of a larger sample set will more closely approximate the population mean, and reduce the chance of a sampling error.



# Hypothesis Formulation


# a hypothesis, or an assumption about your population that you want to test. A hypothesis can be written in words,
# but can also be explained in terms of the sample and population means you just learned about.

#  when constructing hypotheses for a hypothesis test, you want to formulate a null hypothesis. 
# A null hypothesis states that there is no difference between the populations you are comparing,
# and it implies that any difference seen in the sample data is due to sampling error. 

# Null hypothesis statements

```{r}
# experiment 1
hypo_a <- "DeePressurize lowers blood pressure in patients."
hypo_b <- "DeePressurize has no effect on blood pressure in patients."
null_hypo_1 <- "hypo_b"
```

```{r}
# experiment 2
hypo_c <- "The new profile layout has no effect on number of matches with other users."
hypo_d <- "The new profile layout results in more matches with other users than the original layout."
null_hypo_2 <- "hypo_c"
```



# Designing an Experiment

```{r}
# load data
load("retriever_lengths.Rda")
load("doodle_lengths.Rda")
```

```{r}
# calculate mean_retriever_l and mean_doodle_l here:
mean_retriever_l <- mean(retriever_lengths)
mean_retriever_l

mean_doodle_l <-  mean(doodle_lengths)
mean_doodle_l
```

```{r}
# calculate mean_difference here:
mean_difference <- mean_retriever_l -  mean_doodle_l
mean_difference
```

```{r}
# statements:
st_1 <- "The average length of Golden Retrievers is 2.5 inches longer than the average length of Goldendoodles."
st_2 <- "The average length of Golden Retrievers is the same as the average length of Goldendoodles."

# update null_hypo here:
null_hypo <- "st_2"
```

# Type I and Type II Errors

# A Type I error occurs when a hypothesis test finds a correlation between things that are not related. This error is sometimes called a “false positive”
# and occurs when the null hypothesis is rejected even though it is true.

# The second kind of error, a Type II error, is failing to find a correlation between things that are actually related. This error is referred to as a “false negative”
# and occurs when the null hypothesis is not rejected even though it is false.

# The base R intersect() function can take two vectors as arguments and returns a vector containing the common elements.

```{r}
# the true positives and negatives:
actual_positive <- c(2, 5, 6, 7, 8, 10, 18, 21, 24, 25, 29, 30, 32, 33, 38, 39, 42, 44, 45, 47)
actual_negative <- c(1, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 26, 27, 28, 31, 34, 35, 36, 37, 40, 41, 43, 46, 48, 49)

# the positives and negatives we determine by running the experiment:
experimental_positive <- c(2, 4, 5, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 32, 35, 36, 38, 39, 40, 45, 46, 49)
experimental_negative <- c(1, 3, 6, 12, 14, 23, 25, 29, 30, 31, 33, 34, 37, 41, 42, 43, 44, 47, 48)
```

```{r}
# define type_i_errors and type_ii_errors here:
type_i_errors <- intersect(experimental_positive,actual_negative) 

type_i_errors


type_ii_errors <- intersect(experimental_negative,actual_positive)

type_ii_errors
```


# P-Values

#  P-values help determine how confident you can be in validating the null hypothesis. In this context, a p-value is the probability that, assuming the null hypothesis is true,
# you would see at least such a difference in the sample means of your data.

```{r}
# possible interpretations
st_1 <- "There is a 20% chance that the difference in average weight of green and red apples is due to random sampling."
st_2 <- "There is a 20% chance that green and red apples have the same average weight."
st_3 <- "There is a 20% chance red apples weigh more than green apples."
st_4 <- "There is a 20% chance green apples weigh more than green apples."

# update the value of interpretation here:
interpretation <- "st_1"
```

# Significance Level 

# It is an industry standard to set a significance level of 0.05 or less,
# meaning that there is a 5% or less chance that your result is due to sampling error.


# One Sample T-Test


#  A One Sample T-Test compares a sample mean to a hypothetical population mean. It answers the question
# “What is the probability that the sample came from a distribution with the desired mean?”

# R has a function called t.test() in the stats package which can perform a One Sample T-Test for you.

#t.test() requires two arguments, a distribution of values and an expected mean:

results <- t.test(sample_distribution, mu = expected_mean)

``{r}
# calculate ages_mean here:
ages_mean <- mean(ages)
ages_mean
```

```{r}
# perform t-test here:

results <- t.test(ages,mu = 30)
```


# Two Sample T-Test


#  A Two Sample T-Test compares two sets of data, which are both approximately normally distributed.

# You can use R’s t.test() function to perform a Two Sample T-Test, as shown below:

results <- t.test(distribution_1, distribution_2)

```{r}
# calculate week_1_mean and week_2_mean here:
week_1_mean <- mean(week_1)

week_1_mean

week_2_mean <- mean(week_2)

week_2_mean

```

```{r}
# calculate week_1_sd and week_2_sd here:
week_1_sd <- sd(week_1)
week_1_sd

week_2_sd <- sd(week_2)
week_2_sd

```

```{r}
# run two sample t-test here:
results <- t.test(week_1,week_2)
results
```

# Dangers of Multiple T-Tests

# Multiple T test leads to multiple errors
# probability of making a Type I error got dangerously high as you performed more t-tests.

```{r}
# calculate means here:
store_a_mean <- mean(store_a)
store_a_mean
store_b_mean <- mean(store_b)
store_b_mean
store_c_mean <- mean(store_c)
store_c_mean
```

```{r}
# calculate standard deviations here:
store_a_sd <- sd(store_a)
store_a_sd


# ANOVA

# ANOVA (Analysis of Variance) tests the null hypothesis that all of the datasets you are considering have the same mean. If you reject the null hypothesis with ANOVA, you’re saying that at least one of the sets has a different mean;
# however, it does not tell you which datasets are different.

#ou can then run an ANOVA test with this line:

results <- aov(score ~ group, data = df_scores)

# score ~ group indicates the relationship you want to analyze

#To retrieve the p-value from the results of calling aov(), use the summary() function:

summary(results)


```{r}
# inspect stores here:
stores
```

```{r}
# perform anova on stores here:
results <- aov(sales ~ store, data = stores)
summary(results)

```

```{r}
# perform anova on stores_new here:
results_new <- aov(sales ~ store,data = stores_new)
summary(results_new)

# Assumptions of Numerical Hypothesis Tests

#1. The samples should each be normally distributed…ish
#2. The population standard deviations of the groups should be equal
#3. The samples must be independent

```{r}
# plot histograms and define not_normal here:
hist(dist_one)
hist(dist_two)
hist(dist_three)
hist(dist_four)

not_normal <- 4
```

```{r}
# define ratio here:
ratio <- sd(dist_two) / sd(dist_three)
ratio
```
```


# Review

#Phew! Nobody said hypothesis testing is easy, but you made it to the end of the lesson. Congratulations! The world of hypothesis testing is vast. There is much more you can learn, and so many applications where you can use them.

#Let’s review what you’ve learned in this lesson:

#Samples are subsets of an entire population, and the sample mean can be used to approximate the population mean

#The null hypothesis is an assumption that there is no difference between the populations you are comparing in a hypothesis test

#Type I Errors occur when a hypothesis test finds a correlation between things that are not related, and Type II Errors occur when a hypothesis test fails to find a correlation between things that are actually related

#P-Values indicate the probability that, assuming the null hypothesis is true, such differences in the samples you are comparing would exist

#The Significance Level is a threshold p-value for which all p-values below it will result in rejecting the null hypothesis

#One Sample T-Tests indicate whether a dataset belongs to a distribution with a given mean

#Two Sample T-Tests indicate whether there is a significant difference between two datasets

#ANOVA (Analysis of Variance) allows you to detect if there is a significant difference between one of multiple datasets

