# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:22:05 2014

@author: Max
"""

from math import sqrt
# The following function will yield the number of seconds in flight given an initial height in meters.
def falling(x):
    duration= sqrt(x/(2*9.81))
    print("The number of seconds in flight is %.3f seconds." % duration)