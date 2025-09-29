# -*- coding: utf-8 -*-
"""
Solution found

Primes: 13, 5197, 5701, 6733, 8389
Sum: 26,033
Run time reduced to ~10 seconds vs. 1-2 hours reported by OP solution.

Approach

Backtracking algorithm based upon extending path containing list of primes
A prime can be added to the path if its pairwise prime with all primes already in path
Use Sieve of Eratosthenes to precompute primes up to max we expect to need
For each prime, precompute which other primes it is pairwise prime with
"""

import functools
import time

# Decorator for function timing
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

#*************************************************************
# Prime number algorithms
#-------------------------------------------------------------
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16, _known_primes = set([2, 3, 5, 7])):
    if n in _known_primes:
        return True

    if n > 6 and not (n % 6) in (1, 5):
        # Check of form 6*q +/- 1
        return False

    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

def primes235(limit):
    ' Prime generator using Sieve of Eratosthenes with factorization wheel of 2, 3, 5 '
    # Source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes#Python
    yield 2; yield 3; yield 5
    if limit < 7: return
    modPrms = [7,11,13,17,19,23,29,31]
    gaps = [4,2,4,2,4,6,2,6,4,2,4,2,4,6,2,6] # 2 loops for overflow
    ndxs = [0,0,0,0,1,1,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,7]
    lmtbf = (limit + 23) // 30 * 8 - 1 # integral number of wheels rounded up
    lmtsqrt = (int(limit ** 0.5) - 7)
    lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30] # round down on the wheel
    buf = [True] * (lmtbf + 1)
    for i in range(lmtsqrt + 1):
        if buf[i]:
            ci = i & 7; p = 30 * (i >> 3) + modPrms[ci]
            s = p * p - 7; p8 = p << 3
            for j in range(8):
                c = s // 30 * 8 + ndxs[s % 30]
                buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]; ci += 1
    for i in range(lmtbf - 6 + (ndxs[(limit - 7) % 30])): # adjust for extras
        if buf[i]: yield (30 * (i >> 3) + modPrms[i & 7])
            
def prime_pair(x, y):
    ' Checks if two primes are prime pair (i.e. concatenation of two in either order is also a prime)'
    return is_prime(int(str(x)+str(y)))  and is_prime(int(str(y)+str(x)))


def find_pairs(primes):
    ' Creates dictionary of what primes can go with others as a pair'
    prime_pairs = {}
    for i, p in enumerate(primes):
        pairs = set()
        for j in range(i+1, len(primes)):
            if prime_pair(p, primes[j]):
                pairs.add(primes[j])
        prime_pairs[p] = pairs
    return prime_pairs

#*************************************************************
# Main functionality
#-------------------------------------------------------------   
@timer
def find_groups(max_prime = 9000, n = 5):
    '''
       Find group smallest sum of primes that are pairwise prime
       
       max_prime       - max prime to consider
       n                - the size of the group
    '''
    def fully_connected(p, path):
        '''
           checks if p is connected to all elements of the path 
           (i.e. group of primes)
        '''
        return all(p in prime_pairs.get(path_item, set()) for path_item in path)
    
    def backtracking(prime_pairs, n, path = None):
        if path is None:
            path = []
            
        if len(path) == n:
            yield path[:]
        else:
            if not path:
                for p, v in prime_pairs.items():
                    if v:
                        yield from backtracking(prime_pairs, n, path + [p])
            else:
                p = path[-1]
                for t in sorted(prime_pairs[p]):
                    if t > p and fully_connected(t, path):
                        yield from backtracking(prime_pairs, n, path + [t])
      
    primes = list(primes235(max_prime))     # Sieve for list of primes up to max_pair
    set_primes = set(primes)                # set of primes (for easy test if number is prime)
    prime_pairs = find_pairs(primes)        # Table of primes and set of other primes they can pair with
    
    return next(backtracking(prime_pairs, n), None)


for n, max_prime in [(2, 1000), (3, 1000), (4, 1000), (5, 9000)]:
    print(find_groups(max_prime = max_prime, n = n))