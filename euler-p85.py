# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:49:12 2026

Solution #1: Brute Force Approach

Let F(M) be the number of cuboids with this property ignoring rotations with 
dimensions less than or equal to M. We can observe that F(M) – F(M-1) is the 
number of cuboids with this property with at least one side length equal to M. 
Thus, it suffices to count for each possible value of M the number of triples 
(a,b,M) with a<=b<=M such that a cuboid with sides a, b, M has this property.

It is well known that by looking at the net of a rectangular prism, the surface 
area diagonal of the prism can have one of the lengths sqrt((a+b)^2+M^2), 
sqrt((a+M)^2+b^2), or sqrt((b+M)^2+a^2). To minimize the surface area diagonal, 
it is clear that the value sqrt((a+b)^2+M^2) will be the smallest, because the 
rate of change of x^2 increases as x increases. We can observe that 
sqrt((a+b)^2+M^2) <= sqrt(5*M^2). Thus, it suffices to list all square numbers 
up to 5*M^2 and then binary search the list for each value of (a+b)^2+M^2 to 
check whether the cuboid with sides a, b, M satisfies the condition.

Binary Search continues to be very useful for improving the efficiency of code.
"""

import time
from math import sqrt

def projectEulerProblemEightySix(n):
    m = 0
    squares = [0]
    t = 1
    upper = 2*int(sqrt(5*n))+1
    while(t<upper):
        squares.append(t*t)
        t+=1
    current = 0
    while(current<n):
        m+=1
        cFactor = squares[m]
        for abSum in range(2,2*m+1):
            v = squares[abSum]+cFactor
            value = binarySearch(squares, v)
            if value>-1:
                for a in range(max(abSum-m,1),abSum//2+1):
                    b = abSum - a
                    if(a<=b):
                        if b<=m:
                            current+=1
                    else:
                        break
    return m

def binarySearch(myList, n):
    lower = 0
    upper = len(myList)-1
    while(lower<upper-1):
        middle = (lower+upper)//2
        v = myList[middle]
        if v>n:
            upper = middle
        elif v<n:
            lower = middle
        else:
            return middle
    if(myList[lower]==n):
        return lower
    if(myList[upper]==n):
        return upper
    return -1

start = time.time()
print(projectEulerProblemEightySix(1000000))
print("--- %s seconds ---" % (time.time()-start))