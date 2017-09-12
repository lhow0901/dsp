# Think Stats Exercise 3.1
# Use the NSFG respondent variable numkdhh to construct the actual distribution
# for the number of children under 18 in the respondents' households. Now compute
# the biased distribution we would see if we surveyed the children and asked
# them how many children under 18 (including themselves) are in their household.
# Plot the actual and biased distributions, and compute their means.


from __future__ import print_function, division

import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

# Use Think Stats code to load data from respondent file into DataFrame, clean,
# and create BiasePmf function.
resp = nsfg.ReadFemResp()

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

# Plot histogram of PMF
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of Children in Household', ylabel='Pmf')
thinkplot.Save(root='PMF_numkdhh')

# Define biased PMF, plot histogram comparing to actual distribution, and calulate
# respective means
biased_numkdhh = BiasPmf(pmf, label = 'biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_numkdhh])
thinkplot.Config(xlabel='Number of Children in Household', ylabel='PMF')
thinkplot.Save(root='PMF_biased_numkdhh')

mean_unbiased = pmf.Mean()
print(mean_unbiased)

mean_biased = biased_numkdhh.Mean()
print(mean_biased)
