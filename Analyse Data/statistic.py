# Statistical Concepts

import numpy as np

population = np.random.normal(loc=65, scale=3.5, size=300)
population_mean = np.mean(population)

print "Population Mean: {}".format(population_mean)

sample_1 = np.random.choice(population, size=30, replace=False)
sample_2 = np.random.choice(population, size=30, replace=False)
sample_3 = np.random.choice(population, size=30, replace=False)
sample_4 = np.random.choice(population, size=30, replace=False)
sample_5 = np.random.choice(population, size=30, replace=False)

sample_1_mean = np.mean(sample_1)
print "Sample 1 Mean: {}".format(sample_1_mean)

sample_2_mean = np.mean(sample_2)
sample_3_mean = np.mean(sample_3)
sample_4_mean = np.mean(sample_4)
sample_5_mean = np.mean(sample_5)

print "Sample 2 Mean: {}".format(sample_2_mean)
print "Sample 3 Mean: {}".format(sample_3_mean)
print "Sample 4 Mean: {}".format(sample_4_mean)
print "Sample 5 Mean: {}".format(sample_5_mean)



# Central Limit Theorem, states that if we have a large enough sample size, all of our sample means will be sufficiently close to the population mean.

import numpy as np

# Create population and find population mean
population = np.random.normal(loc=65, scale=100, size=3000)
population_mean = np.mean(population)

# Select increasingly larger samples
extra_small_sample = population[:10]
small_sample = population[:50]
medium_sample = population[:100]
large_sample = population[:500]
extra_large_sample = population[:1000]

# Calculate the mean of those samples
extra_small_sample_mean = np.mean(extra_small_sample)
small_sample_mean = np.mean(small_sample)
medium_sample_mean = np.mean(medium_sample)
large_sample_mean = np.mean(large_sample)
extra_large_sample_mean = np.mean(extra_large_sample)

# Print them all out!
print "Extra Small Sample Mean: {}".format(extra_small_sample_mean)
print "Small Sample Mean: {}".format(small_sample_mean)
print "Medium Sample Mean: {}".format(medium_sample_mean)
print "Large Sample Mean: {}".format(large_sample_mean)
print "Extra Large Sample Mean: {}".format(extra_large_sample_mean)

print "\nPopulation Mean: {}".format(population_mean)



# Hypothesis Tests

# A null hypothesis is a statement that the observed difference is the result of chance
# Hypothesis testing is a mathematical way of determining whether we can be confident that the null hypothesis is false.

# The first kind of error, known as a Type I error, is finding a correlation between things that are not related. This error is sometimes called a “false positive”
# and occurs when the null hypothesis is rejected even though it is true.

# Type II error, is failing to find a correlation between things that are actually related. This error is referred to as a “false negative”
# and occurs when the null hypothesis is accepted even though it is false.

import numpy as np

def intersect(list1, list2):
  return [sample for sample in list1 if sample in list2]

# the true positives and negatives:
actual_positive = [2, 5, 6, 7, 8, 10, 18, 21, 24, 25, 29, 30, 32, 33, 38, 39, 42, 44, 45, 47]
actual_negative = [1, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 26, 27, 28, 31, 34, 35, 36, 37, 40, 41, 43, 46, 48, 49]

# the positives and negatives we determine by running the experiment:
experimental_positive = [2, 4, 5, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 32, 35, 36, 38, 39, 40, 45, 46, 49]
experimental_negative = [1, 3, 6, 12, 14, 23, 25, 29, 30, 31, 33, 34, 37, 41, 42, 43, 44, 47, 48]

#define type_i_errors and type_ii_errors here
type_i_errors = intersect(experimental_positive, actual_negative)
type_ii_errors = intersect(experimental_negative, actual_positive)


# P-Values


# Generally, we want a p-value of less than 0.05, meaning that there is less than a 5% chance that our results are due to random chance.
def reject_null_hypothesis(p_value):
  """
  Returns the truthiness of whether the null hypothesis can be rejected

  Takes a p-value as its input and assumes p <= 0.05 is significant
  """
  return p_value <= .05

hypothesis_tests = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

for p_value in hypothesis_tests:
    reject_null_hypothesis(p_value)


 

