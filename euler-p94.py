# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:20:07 2026

Solution #1: Pell Equation Approach

We have two cases to consider. In the first, the triangle has sides x, x, and 
x+1. We can show that the area of this triangle is (x+1)*sqrt(3*x^2-2x-1)/4. 
Thus, it suffices to determine when 3*x^2-2x-1 = y^2 for some integer y. Treating 
this as a quadratic for x and solving, we get x = (2+2*sqrt(4+3y^2))/6. It is 
easy to show that y is not odd, so we can write y = 2*z. Thus, sqrt(4+12z^2) 
= 2*sqrt(1+3z^2) is an integer. It follows that a^2-3z^2 = 1 for some integer a. 
Thus, determining solutions for x is equivalent to determining solutions for z 
in this Pell Equation. We can observe that the first 3 solutions are (a,z) = 
(1,0), (2,1), (7,4). It follows that if (a,z) is a solution, (2*a+3*z, a+2*z) 
is the next solution. We can write x = (1+2*a)/3. We can observe that every 
other solution satisfies a%3 = 1, so it suffices to recursively generate every 
other solution. Doing so, we can find all almost equilateral triangles of the 
form x, x, x+1.

The other case is triangles of the form x, x, x-1. We can find that the area of 
this triangle is (x-1)*sqrt(3*x^2+2x-1)/4. Thus, 3x^2+2x-1 = y^2 for some value 
of y. Solving for x, we get x = (-2+sqrt(16+12y^2))/6. We can observe that 
this will result in the same Pell Equation, but this time the other half of 
the solutions will be acceptable, and we can get the value of x from x = (2a-1)/3. 
From this, we can recursively generate every solution. 
"""

import time

def projectEulerProblemNinetyFour(n):
    # l, l, l+1 Triangles
    y = 14
    x = 8
    pTotal = 0
    while(y<=n-2):
        pTotal+=(y+2)
        yTemp = 7*y+12*x
        xTemp = 4*y+7*x
        y = yTemp
        x = xTemp
    y = 52
    x = 30
    while(y<=n+2):
        pTotal+=(y-2)
        yTemp = 7*y+12*x
        xTemp = 4*y+7*x
        y = yTemp
        x = xTemp
    return pTotal

start = time.time()
print (projectEulerProblemNinetyFour(10**9))
print ("--- %s seconds ---" % (time.time()-start))