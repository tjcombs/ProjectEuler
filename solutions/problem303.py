# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:10:56 2020

@author: tjcombs

https://projecteuler.net/problem=303
"""

import pandas as pd

def check_number(x):
    '''
    Checks if the digits of a number is only made
    up of 0, 1, and 2.
    '''
    answer = True
    while x > 0:
        residue = x % 10
        x = (x - residue)/10
        answer = answer & ((residue == 0) | (residue == 1) | (residue == 2))
    return answer

def check_number_ser(x):
    '''
    Checks if the digits of a number is only made
    up of 0, 1, and 2.
    '''
    answer = True
    while (x > 0).any():
        residue = x % 10
        x = (x - residue)/10
        answer = answer & ((residue == 0) | (residue == 1) | (residue == 2))
    return answer
    
assert(check_number(123)==False)
assert(check_number(102)==True)


numberstemp = pd.DataFrame({'X': [0.0, 1.0, 2.0]})

def extend(df, number):
    data = df.copy()
    data['X'] = number + 10*data['X']
    return data

def f(n):
    return numbers['X'][numbers['X'] % n == 0].min()

data = pd.DataFrame({'n': range(1, 10001)})
data['f(n)'] = None

for i in range(15):
    numberstemp = pd.concat((extend(numberstemp, 0), extend(numberstemp, 1), extend(numberstemp, 2)))
    numbers = numberstemp.copy()
    numbers = numbers[numbers['X']>=10**i]
    data.loc[data['f(n)'].isnull(), 'f(n)'] = data.loc[data['f(n)'].isnull(), 'n'].apply(f)

assert(data['f(n)'].isnull().sum()<=1)
data[data['f(n)'].isnull()]
SUM = (data['f(n)']/data['n']).sum()