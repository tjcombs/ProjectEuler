# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:52:36 2020

@author: tjcombs

https://projecteuler.net/problem=297

"""
import pandas as pd

fibonacci = pd.Series(index=[1, 2], data=[1.0, 2.0])
for k in range(3, 40):
    fibonacci[k] = fibonacci[k-1] + fibonacci[k-2]

data = pd.DataFrame({'n': range(0, 10**6)})
data.loc[data['n']==0, 'RESIDUE'] = 0
data.loc[data['n']==0, 'z'] = 0
data.loc[data['n'].isin(fibonacci), ['RESIDUE', 'z']]= [0, 1]
data['RESIDUE'] = data['RESIDUE'].fillna(data['n'])
data['z'] = data['z'].fillna(0)

while (data['RESIDUE']>0).any():
    # Find the largest fibonicci number below the residue
    data['LARGEST_FIB'] = 0
    for fib in fibonacci:
        data.loc[fib<=data['RESIDUE'], 'LARGEST_FIB'] = fib
    
    data.loc[data['LARGEST_FIB']>0, 'z'] = data.loc[data['LARGEST_FIB']>0, 'z'] + 1
    data['RESIDUE'] = data['RESIDUE'] - data['LARGEST_FIB']

assert(data['z'][data['n']<10**6].sum() == 7894453)

