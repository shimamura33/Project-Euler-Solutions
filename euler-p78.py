# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:05:44 2026

@author: phoeb
"""

import time

'''
 We will proceed with the same dynamic approach that was used in Problem #31, 
 Problem #76, and Problem #77. As noted in my posts for each of those problems, 
 my solution is heavily inspired by Project Euler’s documentation for Problem #31.
That being said, my solution is still far too inefficient for this version of 
the partition problem as it takes over 6 minutes to run. 

Solution #1: Brute Force Dynamic Approach

As in the other questions that involve partitions, we add recursive layers 
representing larger summands after counting the partitions of every number 
with the smaller summands. In this variant of the problem, we have to guess 
and check what the smallest number with a multiple of 1,000,000 partitions is. 
Because it is not easy to recursively go from F(n) to F(n+1), we will guess and 
check by repeatedly multiplying the guess by 3. 
'''
 
def subProblem(n,x):
    numbers = []
    for y in range(1,n+1):
        numbers.append(y)
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(len(numbers)):
        for j in range(numbers[i], n+1):
            ways[j] = (ways[j] + ways[j-numbers[i]])%x
    for y in range(n+1):
        if (ways[y])%x == 0:
            return y
    return -1

def projectEulerProblemSeventyEight(n):
    c = 10
    while True:
        a = subProblem(c,n)
        if(a!=-1):
            return a
        c*=3
        
start = time.time()
print(projectEulerProblemSeventyEight(1000000))
print("--- %s seconds ---" % (time.time()-start))

'''
I definitely need to look for a faster way to do this. The main problem is that 
because the recursive layers build off of each other as larger summands are 
added and a new summand is added for every new input, it is hard to do the 
entire problem recursively. We can store the remainder when every subproblem 
is computed mod 1,000,000 to make the solution more efficient, but this barely 
improved the efficiency. As of right now, I am unsure how to optimize this 
solution.
'''
 




