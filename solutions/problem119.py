# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:07:46 2020

@author: tjcombs

https://projecteuler.net/problem=119

"""
import pandas as pd
import numpy as np

def sum_up_digits(ser):
    sum_digits = 0
    
    while((ser > 0).any()):
        digit = ser % 10
        sum_digits = sum_digits + digit
        ser = (ser-digit)/10
    
    return sum_digits

# Find every number that is of the form b^y where y!=1 and b^y <= threshhold
threshhold = 10**15

# Fix b, then b^y <= threshhold iff y*log(b) <= log(threshhold)
# iff y <= log(threshhold)/log(b) iff y <= floor(log(threshhold)/log(b))

data = pd.DataFrame({'B':range(2, int(np.sqrt(threshhold)))})
data['MAX_EXPONENT'] = np.floor(np.log(threshhold)/np.log(data['B']))
max_exponent = int(data['MAX_EXPONENT'].max())
# Remove b of the form u^v
for k in range(2, max_exponent+1):
    data = data[~np.isclose(np.round(data['B']**(1/k)), data['B']**(1/k))]
data['MAX_NUMBER'] = data['B']**data['MAX_EXPONENT']
# Drop some data that generate the same lists
# data = data.drop_duplicates('MAX_NUMBER', keep='first')
data = data.set_index('B')
# https://stackoverflow.com/questions/50257516/expand-pandas-dataframe-by-values-in-column
data = data.reindex(data.index.repeat(data['MAX_EXPONENT']-1))
data['EXPONENT'] = data.groupby(level=0).cumcount()+2
data['X'] = data.index**data['EXPONENT']
assert(not data['X'].duplicated().any())
data = data[['X']].sort_values(by='X').reset_index(drop=True)

# Find numbers x such that x = sum(x digits) ^ (some number)
# We want the the 30th such number
data = data[data['X'] > 9]
data['SUM_DIGITS'] = sum_up_digits(data['X'])

## X and SUM_DIGITS need to be divisible by the same prime numbers
for prime in [2, 3]:
    data = data[((data['X'] % prime == 0) & (data['SUM_DIGITS'] % prime == 0)) | ((data['X'] % prime != 0) & (data['SUM_DIGITS'] % prime != 0))]

# Check if X = SUM_DIGITS**Something
# Log(X) = Something*log(SUM_DIGITS)
# Something = Log(X)/log(SUM_DIGITS)
# Check if this is an integer
data['EXPONENT'] = np.log(data['X']) / np.log(data['SUM_DIGITS'])
data = data[data['SUM_DIGITS']**np.round(data['EXPONENT']) == data['X']]

assert(data.iloc[1]['X'] == 512)
assert(data.iloc[9]['X'] == 614656)
answer = data.iloc[29]['X']
assert(answer == 248155780267521)
