# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:01:04 2016

@author: ericgrimson
"""

x = 0.2334
epsilon = 0.01
numGuesses = 0
low = x
high = 1.0
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
