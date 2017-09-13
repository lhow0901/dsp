# Think Stats Exercise 5.1
# In the BRFSS (see Section 5.4), the distribution of heights is roughly normal
# with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and
# σ = 7.3 cm for women. In order to join Blue Man Group, you have to be male
# between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the
# U.S. male population is in this range?

import numpy as np
import thinkstats2
import scipy.stats

# Finds the percentile of men with a height of 6'1" (185.4cm) and subtracts it from the
# percitile of men with a height of 5'10" (177.8cm) to get the percent of men
# whose heights fall in that range.
low = scipy.stats.norm.cdf(177.8, loc=178, scale=7.7)
high = scipy.stats.norm.cdf(185.4, loc=178, scale=7.7)
print(np.round(high-low, 3)*100, " percent")
