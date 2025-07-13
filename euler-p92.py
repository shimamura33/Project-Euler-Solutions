#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 18:41:44 2025

@author: phoebeliu
"""

## https://thecprojectt.blogspot.com/2014/10/square-digit-chains-problem-92-project.html
## brute force sol, very slow
def squareDigitChains():
    squareDigitCount = 0
    for i in range(1,10000000):
        strnumber = ""
        strnumber = str(i)
        sqnumber = 0
        temp = strnumber
        while True:
            sqnumber = 0
            for j in range(len(strnumber)):
                sqnumber = sqnumber + int(strnumber[j])**2
            strnumber = str(sqnumber)   
            if sqnumber == 1 or sqnumber == 89:
                break
        if sqnumber == 89:
            print(temp)
            squareDigitCount = squareDigitCount + 1
    print("Required Counter is:",squareDigitCount)            
squareDigitChains()
