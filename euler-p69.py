# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 10:51:29 2025

@author: phoeb
"""

### solution of problem 69 + 3
### https://martin-ueding.de/posts/project-euler-solution-69-totient-maximum/
### https://martin-ueding.de/posts/project-euler-solution-3-largest-prime-factor/

import itertools

def prime_generator() -> int:
    primes = []
    for candidate in itertools.count(2):
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            yield candidate
            primes.append(candidate)
            
def solution() -> int:
    ceiling = 1000000
    result = 1
    for prime in prime_generator():
        if result * prime > ceiling:
            return result
        result *= prime