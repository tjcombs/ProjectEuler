# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:44:15 2020

@author: tjcombs

Problem 92: Square digit chains

The problem statement can be found here:
    
    https://projecteuler.net/problem=92
"""

import pandas as pd

def sum_of_square_digits(x):
    out = 0
    while x >= 10:
        residual = x % 10
        out = out + residual**2
        x = (x-residual)/10
    out = out + x**2
    return out

# Check that the function is behaving correctly
assert(sum_of_square_digits(44) == 32)
assert(sum_of_square_digits(1234) == 30)

data = pd.DataFrame({'X': range(1, 10000000)})

# Create a CLASSIFICATION column which will eventually say if the sequence
# ends up at 1 or 89
data['CLASSIFICATION'] = data['X'].apply(sum_of_square_digits)
data.loc[data['X'].isin([1, 89]), 'CLASSIFICATION'] = data.loc[data['X'].isin([1, 89]), 'X']

while len(data['CLASSIFICATION'].unique()) > 2:
    next_step = data[['X', 'CLASSIFICATION']].copy()
    next_step.columns = ['CLASSIFICATION', 'NEXT']
    data = pd.merge(left=data, right=next_step, on='CLASSIFICATION')
    data = data.drop(columns = ['CLASSIFICATION'])
    data = data.rename(columns = {'NEXT': 'CLASSIFICATION'})

answer = (data['CLASSIFICATION'] == 89).sum()
# Check that the answer is correct
assert(answer == 8581146)
