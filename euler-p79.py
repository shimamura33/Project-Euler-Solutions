#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 19:04:31 2025

@author: phoebeliu
"""

### brute force
### https://walkerdoescode.home.blog/2019/11/07/project-euler-problem-79/

'''
Solution #1: Greedy Algorithm Approach

We simply iterate through the different substrings and store all the minimum 
length strings at each step. For each new substring, we do casework based on 
hich characters in the substring are present in each minimum length string. 
A list of all concatenated strings is generated and only the shortest strings
 are kept for the next substring. Finally, once all substrings have been 
 concatenated, the shortest possible string is generated. 
'''

import time
f = open("/Users/phoebeliu/Downloads/0079_keylog.txt","r")

if f.mode=="r":
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(str(x))
else:
    raise ValueError("Cannot read from file")

finalContents = []
for x in realContents:
    finalContents.append(x[0:3])

def concatenateStrings(a,b):
    c = b[0]
    d = b[1]
    e = b[2]
    try:
        f = a.index(c)
    except:
        f = -1
    try:
        g = a.index(d,f+1)
    except:
        g = -1
    try:
        h = a.index(e,max(g+1,f+1))
    except:
        h = -1
    possible = []
    l = len(a)
    if(f==-1 and g == -1 and h == -1):
        for i1 in range(l+1):
            for i2 in range(i1,l+1):
                for i3 in range(i2,l+1):
                    s = a[0:i1]+c
                    s+=(a[i1:i2]+d)
                    s+=(a[i2:i3]+e+a[i3:])
                    possible.append(s)
        return possible
    if(g==-1 and h == -1):
        for i1 in range(f+1,l+1):
            for i2 in range(i1,l+1):
                s = a[0:i1]+d
                s+=a[i1:i2]+e+a[i2:]
                possible.append(s)
        return possible
    if(f==-1 and h==-1):
        for i1 in range(g+1,l+1):
            for i2 in range(i1,l+1):
                s = a[0:i1]+c
                s+=a[i1:i2]+e+a[i2:]
                possible.append(s)
        return possible
    if(f==-1 and g==-1):
        for i1 in range(g+1,l+1):
            for i2 in range(i1,l+1):
                s = a[0:i1]+c
                s+=a[i1:i2]+d+a[i2:]
                possible.append(s)
        return possible
    if(f==-1):
        for i1 in range(g):
            s = a[0:i1]+c+a[i1:]
            possible.append(s)
        return possible
    if(g==-1):
        for i1 in range(f+1,h):
            s = a[0:i1]+d+a[i1:]
            possible.append(s)
        return possible
    if(h==-1):
        for i1 in range(g+1,l+1):
            s = a[0:i1]+c+a[i1:]
            possible.append(s)
        return possible
    return [a]

def projectEulerProblemSeventyNine(myList):
    if(len(myList)==1):
        return myList[0]
    if(len(myList) == 2):
        a = concatenateStrings(myList[0], myList[1])
        minFound = len(a[0])
        for x in a:
            if(len(x)<minFound):
                minFound = len(x)
        return minFound
    allMini = [myList[0]]
    l = len(myList)
    for x in range(1,l):
        newMini = []
        minLength = -1
        curValue = myList[x]
        for y in allMini:
            z = concatenateStrings(y, curValue)
            for b in z:
                if(minLength==-1 or len(b)<minLength):
                    minLength = len(b)
                    newMini = [b]
                elif(len(b)==minLength):
                    if b not in newMini:
                        newMini.append(b)
        allMini = newMini
    return allMini[0]

start = time.time()
print(projectEulerProblemSeventyNine(finalContents))
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

73162890
--- 0.000269889831543 seconds ---

for input = given list of password attempts.
''' 