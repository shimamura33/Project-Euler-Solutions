# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:55:07 2026

@author: phoeb
"""

"""
Number of numbers between 1 and n that are coprime to n is given by the Euler's Totient
function, phi(n). So, the answer is simply the sum of phi(n) for 2 <= n <= 1,000,000
Sum of phi(d), for all d|n = n. This result can be used to find phi(n) using a sieve.

Totient Function Sieve (Function ET(L))

    We create a list phi[] of size L+1 such that phi[i] = i.
    We iterate over n from 2 to L. If phi[n] == n, then n is prime.
    For each prime n, we update its multiples:
    φ[k]=φ[k]−φ[k]n for each multiple k of n
    φ[k]=φ[k]−nφ[k]​ for each multiple k of n
    This is a standard sieve method for computing totient values in O(Llog⁡log⁡L)O(LloglogL) time. 

Next, we compute the partial sums of the values in the phi[] list. As a result, phi[x] stores the sum of φ(i)φ(i) for ii ranging from 00 to xx.

Finally, we handle user queries by reading an integer input and outputting cumulative sum minus 1. The subtraction of 1 excludes the fraction 1/11/1.

By precomputing the totient function values and their cumulative sums, we can answer each query in constant time. 
"""

L = 1_000_000
phi = list(range(L + 1))

for n in range(2, L + 1):
    if phi[n] == n:  # n is prime
        for k in range(n, L + 1, n):
            phi[k] -= phi[k] // n

for i in range(1, L + 1):
    phi[i] += phi[i - 1]


#似乎不对
for _ in range(int(input())):
    print(phi[int(input())] - 1)	
    
#现在对了
print(phi[int(L)] - 1)
    


#第二种方法    
import numpy as np


def solution(limit: int = 1_000_000) -> int:
    """
    Returns an integer, the solution to the problem
    >>> solution(10)
    31
    >>> solution(100)
    3043
    >>> solution(1_000)
    304191
    """

    # generating an array from -1 to limit
    phi = np.arange(-1, limit)

    for i in range(2, limit + 1):
        if phi[i] == i - 1:
            ind = np.arange(2 * i, limit + 1, i)  # indexes for selection
            phi[ind] -= phi[ind] // i

    return int(np.sum(phi[2 : limit + 1]))


if __name__ == "__main__":
    print(solution())   