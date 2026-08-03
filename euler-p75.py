# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:49:10 2026

@author: phoeb
"""

'''
- 求解分析

我们知道Project Euler Problem 39整数边直角三角形也有判断一个给定的周长p，最多有多少整数边直角三角形。

但是 p ≤ 1000, 现在 L≤1500000, 我们需要找到其他方法或规律来解决这道题。

请参考 Pythagorean triple - Wikipedia来生成毕达哥拉斯三元组。

- C++/Python 代码实现

我们根据求解分析的方法，使用下面的方法，产生a, b,c， 然后判断(a, b, c)是否是最简三角形，然后找到周长为p的k倍的三角形，最后统计只有单个整数边的直角三角形个数。

    a = k*(m2 - n2), b = k*(2mn), c = k*(m2 + n2)
    where m, n, and k are positive integers with m > n, (m − n) odd, and with m
    and n coprime.
'''


import time
import math

def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def findIntegerSidedRightAngleTriangles(max_length):
    numOfTriangles, rightTriangles = 0,  [0] * (max_length+1)
    
    # p = 2*m*m + 2*m*n <= max_length, n >= 1, m > n so m>=2 and
    for m in range(2, int(math.sqrt((max_length-4)//2))):
        for n in range (1, m):       # m > n
            # check whether (m − n) is odd and  m & n are co-prime
            if (m - n) % 2 == 1 and 1 == gcd(m, n):             
                a, b, c = m*m-n*n, 2*m*n, m*m+n*n
                p = a+b+c  # the perimeter of a right angle triangle
         
                if p <= max_length and 1 == gcd(c, gcd(b, a)):
                    #for k in range (1, (max_length+1)//p+1):   ## working
                    #    rightTriangles[p*k] += 1
                    for s in range(p, max_length+1, p):            ## faster 
                        rightTriangles[s] += 1
    
    numOfTriangles = len([s for s in range(1, max_length+1) if 1 == rightTriangles[s]])
    return numOfTriangles

def main():
    start = time.process_time()
    
    assert(13 == findIntegerSidedRightAngleTriangles(120));

    L = 1500000
    print("For L <= %d," % L, findIntegerSidedRightAngleTriangles(L), end='')
    print(" exactly one integer sided right angle triangles can be formed.")

    end = time.process_time()
    print('CPU processing time :', end-start)

if  __name__ == '__main__':
    main()
