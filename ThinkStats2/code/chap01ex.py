"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

preg = nsfg.ReadFemPreg()
resp = nsfg.ReadFemResp()


print(resp.pregnum.value_counts().sort_index())
