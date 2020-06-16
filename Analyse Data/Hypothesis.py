# Introduction: Hypothesis Testing with SciPy

# 1 Sample T-Testing

# SciPy has a function called ttest_1samp, which performs a 1 Sample T-Test for you.

# ttest_1samp requires two inputs, a distribution of values and an expected mean:

tstat, pval = ttest_1samp(example_distribution, expected_mean)
print pval

from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("ages.csv")

print(ages)

ages_mean = np.mean(ages)
tset, pval = ttest_1samp(ages, 30)

print pval

# One Sample T-Test II

from scipy.stats import ttest_1samp
import numpy as np

correct_results = 1 # Start the counter at 0

daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")

for i in range(1000): # 1000 experiments
   #your ttest here:
   t, pval = ttest_1samp(daily_visitors[i], 30) # perform t-test
   if pval < 0.05: # check our p-value
       correct_results += 1
    #print the pvalue here:
   print pval
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
  

# 2 Sample T-Test


from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")


week1_mean = np.mean(week1)
print(week1_mean)
week2_mean = np.mean(week2)
print(week2_mean)

week1_std = np.std(week1)
print(week1_std)

week2_std = np.std(week2)
print(week2_std)

tstatstic, pval = ttest_ind(week1, week2)

print(pval)



# Dangers of Multiple T-Tests
# The bigger the test the lesser the efficiency
# probability of making a Type I error got dangerously high as we performed more t-tests.

# ANOVA 

from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b_new.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

stat, pval = f_oneway(a, b, c)
print pval


# Assumptions of Numerical Hypothesis Tests




# Tukey's Range Test

# The function to perform Tukey’s Range Test is pairwise_tukeyhsd, which is found in statsmodel, not scipy.

tukey_results = pairwise_tukeyhsd(movie_scores, labels, 0.05)

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

stat, pval = f_oneway(a, b, c)
print pval

# Using our data from ANOVA, we create v and l
v = np.concatenate([a, b, c])
labels = ['a'] * len(a) + ['b'] * len(b) + ['c'] * len(c)

tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print tukey_results


# Binomial Test


# SciPy has a function called binom_test, which performs a Binomial Test for you.

pval = binom_test(525, n=1000, p=0.5)

from scipy.stats import binom_test

pval = binom_test(510, n=10000, p=0.06)
print pval

pval2 = binom_test(590, n=10000, p=0.06)
print pval2



# Chi Square Test

from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12
# 4th gr | 20 .     |  20

X = [[30, 10],
     [35, 5],
     [28, 12],
     [20, 20]]
chi2, pval, dof, expected = chi2_contingency(X)
print pval




# Project Familiar

import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency



vein_pack_lifespans = familiar.lifespans(package='vein')

tstat, vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test)
#for stat,pvalue in vein_pack_test:
if vein_pack_test < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package='artery')

tstat,package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)
if package_comparison_results < 0.05:
  print("the Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")

iron_contingency_table = familiar.iron_counts_for_package()

tstat, iron_pvalue, dof,ef  = chi2_contingency(iron_contingency_table)
print(iron_pvalue)
if iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("It is nice")







# Project Fetchmaker
import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency



rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

whippet_rescue = fetchmaker.get_is_rescue("whippet")

num_whippet_rescues = np.count_nonzero(whippet_rescue)
print(num_whippet_rescues)

num_whippets = np.size(whippet_rescue)
print(num_whippets)

pval = binom_test(num_whippet_rescues, n = num_whippets, p = 0.08)
print(pval)

a = fetchmaker.get_weight("whippet")
b = fetchmaker.get_weight("terrier")
c = fetchmaker.get_weight("pitbull")
stat, pval = f_oneway(a, b, c)
print(pval)

v = np.concatenate([a, b, c])
labels = ['a'] * len(a) + ['b'] * len(b) + ['c'] * len(c)

tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print tukey_results

poodle_colors = fetchmaker.get_color("poodle")

shihtzu_colors = fetchmaker.get_color("shihtzu")

color_table = [[np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")], [np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")], [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")], [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")], [np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]]

chi2, pval, dof, expected = chi2_contingency(color_table)
print pval
