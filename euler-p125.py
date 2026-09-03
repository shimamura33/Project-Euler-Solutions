# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:59:25 2026

@author: phoeb
"""

# 暴力解

import time
time1=time.time()
total,items=0,[]
Number=10**8
 
def Solve(i):
    global total,cnt,maxi
 
    m,sumi=i,0
 
     
    sumi=m**2
    keep=True
     
    while keep:
 
        m+=1
        sumi+=m**2
         
 
        if sumi>=Number:
            keep=False
            break
         
         
        ssumi=str(sumi)
        #print(i,ssumi,ssumi[::-1])
        if ssumi==ssumi[::-1] and sumi not in items:
                #print(i,ssumi,m,i)
                total+=sumi
                items.append(sumi)
 
     
 
for i in range(1,10000):
 
    Solve(i)
 
print("total=",total,sorted(items),len(items))
print(time.time()-time1)