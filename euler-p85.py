# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 13:24:21 2025

@author: phoeb

https://ramonsmathsblog.wordpress.com/2020/11/26/project-euler-problem-85-python-solution/
"""

def A(n,k):
    t = 0
    for a in range(1,n+1):
        for b in range(1,k+1):
            t = t+ (n-a+1)*(k-b+1)
    return t


L =[]
B=[]
for k in range(1,201):
    for n in range(1,201):
        L.append(A(n,k))
        B.append(n*k)
dist=2000000
ind = 0
for i in range(0,len(L)):
    d=(abs(L[i]-2000000))
    if d<dist:
        dist = d
        ind = i
print(B[ind])