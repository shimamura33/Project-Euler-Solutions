# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:56:27 2026

@author: phoeb

Solution #1: SFFT Approach

We can rearrange the given equation to xy = nx+ny. By Simon’s Favorite Factoring Trick, 
this equation can be factored as (x-n)(y-n) = n^2. It follows that the number of 
ordered solutions (x,y) is the number of factors of n^2. Thus, it suffices to find 
the smallest value of n such that n^2 has at least 1999 factors. I did this by 
using the Sieve of Eratosthenes to find all primes less than an arbitrary upper 
bound and then using this list of primes to check each potential value of n until 
a sufficient value was found.
"""

 
import time

from math import sqrt

def countFactorSquare(n):
    a = n*n
    t = 0
    for x in range(1,n):
        if(a%x==0):
            t+=1
    return t+1

def sieveEratosthenes(n):
    myPrimes = []
    primePossible = [True]*(n+1)
    primePossible[0] = False
    primePossible[1] = False
    
    for (i,possible) in enumerate(primePossible):
        if possible:
            for x in range(i*i, (n+1), i):
                primePossible[x] = False
            myPrimes.append(i)
    return myPrimes

def projectEulerProblemOneHundredEight(n,m):
    myPrimes = sieveEratosthenes(n)
    primes = []
    exponents = []
    for a in range(n+1):
        primes.append([])
        exponents.append([])
    for x in myPrimes:
        for y in range(x,n+1,x):
            primes[y].append(x)
            exponents[y].append(1)
        power = x*x
        while(power<=n):
            for y in range(power,n+1,power):
                l = len(exponents[y])
                exponents[y][l-1]+=1
            power*=x
    totals = []
    for x in range(n+1):
        myProd = 1
        for a in exponents[x]:
            myProd*=(2*a+1)
        myProd = (myProd+1)/2
        totals.append(myProd)
    for x in range(n+1):
        if(totals[x]>m):
            return x
    return -1

start = time.time()
print(projectEulerProblemOneHundredEight(1000000,1000))
print("--- %s seconds ---" % (time.time()-start))