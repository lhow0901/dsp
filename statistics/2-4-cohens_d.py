# Think Stats Exercise 2.4
# Using the variable `totalwgt_lb`, investigate whether first babies
# are lighter or heavier than others. Compute Cohen’s effect size to
# quantify the difference between the groups. How does it compare to the
# difference in pregnancy length?


from __future__ import print_function, division

import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

# Use Think Stats code to load data from pregnancy file into DataFrame, clean,
# select only live births, and separte into two groups: first births and others
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.

    group1: Series or DataFrame
    group2: Series or DataFrame

    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

# My investigation of total birth weight by birth order

# Histogram of total birth weight in lbs by birth order
preg['totalwgt_lb'] = preg.birthwgt_lb + preg.birthwgt_oz/16
totalwgt_round = np.round(live.totalwgt_lb)

first_hist = thinkstats2.Hist(totalwgt_round, label='first')
other_hist = thinkstats2.Hist(totalwgt_round, label='other')

width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
thinkplot.Config(xlabel='lbs', ylabel='Count', xlim=[0, 13])

thinkplot.Save(root='first_others_totalwgt_live')

# Descriptive statistics for first births versus others
mean_firsts = firsts.totalwgt_lb.mean()
var_firsts = firsts.totalwgt_lb.var()
std_firsts = firsts.totalwgt_lb.std()

mean_others = others.totalwgt_lb.mean()
var_others = others.totalwgt_lb.var()
std_others = others.totalwgt_lb.std()

print("Firsts n = ", len(firsts))
print("Others n = ", len(others))

print("Firsts mean = ", np.round(mean_firsts, 2), " lbs")
print("Others mean = ", np.round(mean_others, 2), " lbs")

print("Firsts sd = ",  np.round(std_firsts, 2))
print("Others sd = ",  np.round(std_others, 2))

# Calculating Cohen's d for firsts versus others
print("Cohen's d for firsts vs others = ", np.round(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb), 2))
