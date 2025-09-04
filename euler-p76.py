# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:14:50 2025

You may notice that this solution is very similar to Project Euler Problem #31 
which involved determining the number of ways certain amounts of currency could 
be represented with coins. The only difference is that in this question, the 
possible values of the coins include every positive integer. You may also recall 
that the more efficient solution I presented in Problem #31 came from Project 
Euler’s documentation. Thus, I will reuse their solution to solve this problem 
and give credit appropriately. Here is Project Euler’s Solution:

Solution #1: Dynamic Approach (Project Euler’s Approach)

As in Project Euler Problem #31, we can observe that adding larger types of 
currency can be thought of as adding to the same problem with only the smaller 
amounts of currency. Thus, we dynamically count the number of ways each total 
can be summed for each new currency. In this case, the currencies range in value
from 1 to n-1. Once all of the currencies have been iterated through, we are 
done. Here is an implementation of this approach in Python 2.7. As listed above, 
this is very similar to Project Euler’s solution for Problem #31.
"""

import time
 
def projectEulerProblemSeventySix(n):
    numbers = []
    for x in range(1,n):
        numbers.append(x)
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(len(numbers)):
        for j in range(numbers[i], n+1):
            ways[j] = ways[j] + ways[j-numbers[i]]
    return ways[n]
 
start = time.time()
print(projectEulerProblemSeventySix(100))
print("--- %s seconds ---" % (time.time()-start))
