# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:45:45 2026

@author: phoeb
"""

'''
暴力求解
First, we determine the sum of the proper factors of every number less than 
1,000,000 by iterating through the possible divisors less than 500,000 and 
adding each divisor to every proper multiple of it. Next, we start from 1,000,000 
and work down, checking each number for periodic behavior of amicable chains. 
We can perform this task dynamically, so numbers that are part of larger chains 
do not need to be checked multiple times. 
'''

import time

def projectEulerProblemNinetyFive(n):
    properSums = [0]*(n+1)
    for c in range(1,int(n/2+1)):
        for d in range(2*c,n+1,c):
            properSums[d]+=c
    maxLoop = 5
    minNumber = 12496
    loopLengths = [-1]*(n+1)
    for e in range(n,0,-1):
        if loopLengths[e]==-1:
            t = 0
            f = properSums[e]
            loops = True
            found = [e]
            if(f!=e):
                while(f!=e):
                    t+=1
                    if(f>n):
                        for x in found:
                            loopLengths[x] = 0
                        loops = False
                        break
                    if loopLengths[f]!=-1:
                        for x in found:
                            loopLengths[x] = loopLengths[f]
                            loops = False
                            break
                    if f in found:
                        a = found.index(f)
                        for x in found:
                            loopLengths[x] = len(found)-a
                        found = found[a:]
                        break
                    found.append(f)
                    v = properSums[f]
                    if(v==f or v==0):
                        for x in found:
                            loopLengths[x] = 0
                        loops = False
                        break
                    f = v
                if loops:
                    for x in found:
                        loopLengths[x] = t
                    if t>maxLoop:
                        maxLoop = t
                        minNumber = found[0]
                        for x in found:
                            if x<minNumber:
                                minNumber = x
                    elif t==maxLoop:
                        for x in found:
                            if x<minNumber:
                                minNumber = x
                else:
                    for x in found:
                        loopLengths[x] = 0
    return minNumber

start = time.time()
print (projectEulerProblemNinetyFive(1000000))
print ("--- %s seconds ---" % (time.time()-start))