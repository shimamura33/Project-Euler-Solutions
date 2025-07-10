# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 15:22:33 2025

@author: phoeb
"""

## https://ramonsmathsblog.wordpress.com/2020/08/27/project-euler-problem-49-python-solution/

from sympy import *
primes=[]
for i in range(1000,10000):
    if isprime(i):
        primes.append(i)
        
from itertools import permutations 
def permute(n):
    return list(set([int(''.join(p)) for p in permutations(str(n))]))
def prime_permute(n):
    perms = permute(n)
    prime_perms =[]
    for p in perms:
        if p in primes:
            prime_perms.append(p)
    prime_perms.remove(n)
    return sorted(prime_perms)


def sequence_gen(n):
    seq_bool=False
    global seq
    seq=[]
    fin =[]
    perms = prime_permute(n)
    for q in perms:
        if (q+(q-n)) in perms:
            seq =[n,q,2*q-n]
            seq_bool=True
    return seq_bool

for p in primes:
    if sequence_gen(p):
        print(seq)