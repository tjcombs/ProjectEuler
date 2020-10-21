# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:07:51 2020

@author: tjcombs

Problem 99: Largest exponential

Problem statement can be found here:
    
    https://projecteuler.net/problem=99

"""

import requests
import numpy as np
import pandas as pd

# Get the data
req = requests.get('https://projecteuler.net/project/resources/p099_base_exp.txt')

data = pd.DataFrame({'PAIR': req.text.split('\n')})
data['ROW'] = data.index + 1
data[['X', 'Y']] = data['PAIR'].str.split(',', expand=True).astype(int)
data['LOG(X^Y)'] = data['Y']*np.log(data['X'])
# X^Y is largest when LOG(X^Y) is large
max_row = data.loc[data['LOG(X^Y)']==data['LOG(X^Y)'].max()]
answer = max_row.iloc[0]['ROW']

# Answer is 709
assert(answer == 709)