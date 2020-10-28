# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:45:06 2020

@author: tjcombs

https://projecteuler.net/problem=725

"""
import pandas as pd

def sum_up_digits(ser):
    sum_digits = 0
    
    while((ser > 0).any()):
        digit = ser % 10
        sum_digits = sum_digits + digit
        ser = (ser-digit)/10
    
    return sum_digits

data = pd.DataFrame({'X': range(1, 1000)})
data['X_str'] = data['X'].astype(str)
data['SUM_DIGITS'] = sum_up_digits(data['X'])

# X is a DS-Number if an only if when you sort the digits in decreasing order
# you still have a DS-Number

# X is a DS-Number if and only if when I add 0 to anywhere in the number I
# have a DS-Number


# X is a DS-Number if and only if SUM(X)/2 is a digit of X
# Proof: Write X = a_0a_1a_2...a_k...a_n.  Without loss of generality, assume
# the a_i are decreasing. Set S=SUM(X)=a_1+a_2+...+a_n.
# (<==) Suppose SUM(X)/2 is a digit of X.  Say a_k = SUM(X)/2.  Then the sum
# of all the other digits is SUM(X)/2, hence X is a DS-Number.
# (==>) Suppose X is a DS-Number.  Then, for some k a_k is the sum of the
# other digits.  So SUM(X) = a_k + (sum of other digits) = a_k + a_k = 2a_k,
# hence a_k = SUM(X)/2.
data = data[data['SUM_DIGITS'] % 2 == 0]
data['DIGIT'] = (data['SUM_DIGITS']/2).astype(int)
data = data[data['DIGIT'] <= 9]
# These are all DS-Numbers less than 1000
data = data[data.apply(lambda x: str(x['DIGIT']) in x['X_str'], axis=1)]


