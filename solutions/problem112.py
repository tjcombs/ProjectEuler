# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:25:48 2020

@author: TJ

Problem 112: Bouncy Numbers

This is where the problem is from:
    
    https://projecteuler.net/problem=112

Working from left-to-right if no digit is exceeded by the digit to its left it 
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a 
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a 
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over 
half of the numbers below one-thousand (525) are bouncy. In fact, the least 
number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we 
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

"""

import pandas as pd

data = pd.DataFrame({'X': range(1, 2000000)})
# Make the increasing version of the number
data['X_inc'] = data['X'].astype(str).astype(str).str.split('').apply(sorted).str.join('').astype(int)
# Make the decreasing version of the number
data['X_dec'] = data['X'].astype(str).astype(str).str.split('').apply(sorted, reverse = True).str.join('').astype(int)
# BOUNCY if not increasing and not decreasing
data['BOUNCY'] = (data['X'] != data['X_inc']) & (data['X'] != data['X_dec'])
data['PERCENT_BOUNCY'] = data['BOUNCY'].cumsum() / data['X']

answer = data[data['PERCENT_BOUNCY']>=0.99]['X'].min()
assert(answer == 1587000)