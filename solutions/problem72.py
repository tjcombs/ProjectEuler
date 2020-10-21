# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:56:35 2020

@author: tjcombs

Problem 72: Counting fractions

Problem statement can be found here:
    
    https://projecteuler.net/problem=72

"""

import numpy as np
import pandas as pd
from sympy import factorint

def phi(x):
    '''
    Euler's totient function
    Returns the number of numbers 1<=y<x such that y and x are reletively prime.
    The fraction y/x with 1<=y<x is a proper fracton if and only if y and x 
    are reletively prime.
    '''
    factors = factorint(x)
    components = [p**factors[p] - p**(factors[p]-1) for p in factors] + [1]
    return np.product(components)

data = pd.DataFrame({'d': range(2, 1000001)})
data['PROPER_FRACTIONS'] = data['d'].apply(phi)
answer = data['PROPER_FRACTIONS'].sum()
assert(answer == 303963552391)