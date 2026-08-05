# -*- coding: utf-8 -*-
"""
Solution: Pell Equation Approach

Let the number of blue disks be b and let the total number of disks be t. We 
want to search for integer pairs (b,t) such that 2*b*(b-1) = t*(t-1). Writing 
this as 2b^2-2b+t-t^2 = 0 and solving for b, we get 
b = (2+sqrt(4+8t^2-8t))/4 = (1+sqrt(1+2t^2-2t))/2. Thus, it suffices to find 
values of t such that 2t^2-2t+1 = c^2 for some integer c. Solving for t, we get 
t = (2+sqrt(8c^2-4))/4 = (1+sqrt(2c^2-1))/2. Thus, it suffices to find values 
of c such that d^2-2c^2 = -1 for some integer d. The first three solutions to 
this are (1,1), (7,5), It follows that if (d,c) is a solution, (3*d+4*c,2*d+3*c) 
is the next solution. Thus, the integer solutions for c can be recursively 
generated, and each one can be translated to a distinct solution for the value 
of b. 
"""

import time

def projectEulerProblemOneHundred(n):
    y = 7
    x = 5
    maxY = 2*n-1
    while(y<=maxY):
        tempX = 2*y+3*x
        tempY = 3*y+4*x
        y = tempY
        x = tempX
    return (x+1)/2

start = time.time()
print(projectEulerProblemOneHundred(10**12))
print("--- %s seconds ---" % (time.time()-start))

'''
And with that, we’re done. This is yet another example of the powers of Pell 
Equations. We wanted to find all solutions up to 1 trillion, and yet the program 
only took a hundredth of a millisecond to run.
'''