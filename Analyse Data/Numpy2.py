# STATISTICAL DISTRIBUTIONS WITH NUMPY

# Histogram

import numpy as np
# Write matplotlib import
from matplotlib import pyplot as plt
commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, bins = 6 ,range = (20,51))
plt.show()


# Different Types of DISTRIBUTIONS
# Unimodal histogram | Bimodal histogram | Multimodal histogram 

# Skew - Right | Skew - left | Symmetric 


# Normal Distribution, Part II

import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(6.7,0.7,size= 1000)

# Fictionosaurus
f_data = np.random.normal(7.7,0.3,size = 1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

mystery_dino = "Brachiosaurus"
answer = False


# Standard Deviations and Normal Distribution


import numpy as np

one_above = 1000 + 100

one_below = 1000 - 100

print(one_above)

print(one_below)

one_std = 1360

print(one_std)

#  In any normal distribution, 68% of the total data is within one standard deviation.


# Binomial Distribution
import numpy as np
from matplotlib import pyplot as plt
# N is the number of trials, P is the probability of success, and size relates to the number of experiments.

emails = np.random.binomial(500 ,0.05, size = 10000)

plt.hist(emails)
plt.show()


# Binomial Distributions and Probability

import numpy as np

emails = np.random.binomial(500, 0.05, size=10000)

no_emails = np.mean(emails == 0)

b_test_emails = np.mean(emails == 8)

print(no_emails)
print(b_test_emails)


# Review

np.random.normal(
    loc=desired_mean,
    scale=desired_std,
    size=num_samples)




import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(
  loc=sunflowers_mean,
  scale=sunflowers_std,
  size=5000
)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='Observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='Normal', normed=True)
plt.legend()
plt.show()


# Calculate probabilities here:
experiments = np.random.binomial(200, 0.1, size=5000)
prob = np.mean(experiments < 20)
print(prob)


# Project Election Results
from matplotlib import pyplot as plt
import numpy as np
 
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)

percentage_ceballos = 100 * 33/len(survey_responses)
print(percentage_ceballos)

survey_length = float(len(survey_responses))

possible_surveys = np.random.binomial(survey_length, 0.54, size=10000) / survey_length

plt.hist(possible_surveys,range=(0,1),bins= 20)
plt.show()


ceballos_loss_surveys = np.mean(possible_surveys < 0.5 )

print(ceballos_loss_surveys)

large_survey_length = float(7000)

large_survey = np.random.binomial(large_survey_length, 0.54, size=10000) / large_survey_length

ceballos_loss_new = np.mean(large_survey < 0.5 )
print(ceballos_loss_new )



# Histogram, Mean and Median in NUMPY

minimum = np.amin()
maximun = np.amax()

times_hist = np.histogram(times, range = (0, 24), bins = 4)
plt.hist(times, range = (0, 24), bins = 4)
plt.show()
