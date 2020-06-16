# Introduction to Sample Size and A/B Testing

# An A/B Test is a scientific method of choosing between two options (Option A and Option B)

# In order to determine the sample size necessary for an A/B test, a sample size calculator requires three numbers:

#The Baseline conversion rate
#The Minimum detectable effect
#The Statistical significance

# A/B Testing: Determining Lift



# Lift is generally expressed as a percent of the baseline conversion rate
#To calculate lift:

100 * (new - old) / old
100 * (8 - 6) / 6
33%



# A/B Testing: Don't Interfere With Your Tests

# Here are two important rules for making sure that A/B tests remain unbiased:

# Don’t continue to run the test after the predetermined sample size, until “significant” results are found.
# Don’t stop a test before reaching the predetermined sample size, just because your results reach significance early
# (unless there are ethical reasons that require you to stop, like a prescription drug trial).

# Test data is sensitive to changes in sample size, which is why it is important to calculate beforehand.



# A/B Testing: Splitting a Test

910 / (350 * 20)


# Sample Size Calculator for Margin of Error


# It is easy to find a sample size calculator online, but it is difficult to determine what parameters to input. Generally, sample size calculators use 4 parameters:

#Margin of error
#Confidence level
#Population size
#Expected proportion

# Margin of Error

# The margin of error is the furthest we expect the true value to be from what we measure in our survey. 

# the smaller we make the margin of error, the more certainty we have in the results
# In order to make our margin of error smaller, we will need a larger sample size.

# Population Size

# Normally, 100,000 will suffice, as changes become negligible beyond that.
# Generally, we use this larger population size of 100,000 or greater instead of focusing on the amount of current customers.
# But when you are working with a known sample size. like the num of employees in a company. Use the population of the employees.


# Likely Sample Proportion

# Confidence Level

# The confidence level is the probability that the margin of error contains the true proportion.

# Sample Size of a Survey

margin_of_error = 4

confidence_level = 95

likely_proportion = 40

population_size = 100000


sample_size = 573

weeks_of_survey = 600 / 120



#Project A/B Testing at Nosh Mish Mosh

import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits

paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)

paying_visitor_count = len(paying_visitors)

baseline_percent = (paying_visitor_count * 100.0) / total_visitor_count


print(baseline_percent)

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)

new_customers_needed = np.ceil(1240 / average_payment)

percentage_point_increase = (new_customers_needed * 100.0) / total_visitor_count
print(percentage_point_increase)

minimum_detectable_effect = 100.0 * percentage_point_increase / baseline_percent

print(minimum_detectable_effect)

ab_sample_size = 290
