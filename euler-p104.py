# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:27:59 2026

@author: phoeb
"""

'''
It is easy to determine the rightmost 9 digits of the nth Fibonacci number by 
simply storing the number mod 10^9. The difficulty comes in investigating the 
leftmost 9 digits. To do this, I arbitrarily stored the leftmost 15 digits and 
recursively updated them to get approximate leftmost 15 digits for each Fibonacci 
number. My hope is that the leftmost 9 digits of this recursive result will 
have the correct leftmost 9 digits for successive Fibonacci numbers. By checking 
the leftmost and rightmost 9 digits for the pandigital property, it is possible 
to find the first index with the given property. 
'''

import time

def isPandigital(x):
    return sorted(x) == ["1","2","3","4","5","6","7","8","9"]

def projectEulerProblemOneHundredFour(n):
    firstL = 1
    secondL = 1
    firstF = 1
    secondF = 1
    i = 3
    while(True):
        temp = firstL+secondL
        secondL = firstL
        firstL = temp%(10**9)
        temp = firstF + secondF
        secondF = firstF
        if(temp>10**n):
            temp = int(str(temp)[0:n])
            secondF/=10
        firstF = temp
        if isPandigital(str(firstL)):
            if isPandigital(str(firstF)[0:9]):
                return i
        i+=1

start = time.time()
print(projectEulerProblemOneHundredFour(15))
print("--- %s seconds ---" % (time.time()-start))