# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:10:56 2020

@author: tjcombs

https://projecteuler.net/problem=303
"""

import pandas as pd

numberstemp = pd.DataFrame({'X': [0.0, 1.0, 2.0]})

def extend(df, number):
    data = df.copy()
    data['X'] = number + 10*data['X']
    return data

def f(n):
    return numbers['X'][numbers['X'] % n == 0].min()

data = pd.DataFrame({'n': range(1, 10001)})
data['f(n)'] = None
# Find f(9999) because it is taking too long
# From data
# f(9) = 12222
# f(99) = 1122222222
# f(999) = 111222222222222
# Looks like should be
# f(9999) = 11112222222222222222
data.loc[data['n']==9999, 'f(n)'] = 11112222222222222222

for i in range(15):
    numberstemp = pd.concat((extend(numberstemp, 0), extend(numberstemp, 1), extend(numberstemp, 2)))
    numbers = numberstemp.copy()
    numbers = numbers[numbers['X']>=10**i]
    data.loc[data['f(n)'].isnull(), 'f(n)'] = data.loc[data['f(n)'].isnull(), 'n'].apply(f)

assert(data['f(n)'].notnull().all())
SUM = (data['f(n)']/data['n']).sum()
# Check answer
assert(SUM == 1111981904675169)