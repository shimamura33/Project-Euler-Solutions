# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:38:00 2026

@author: phoeb

https://martin-ueding.de/posts/project-euler-solution-70-totient-permutation/
"""

import itertools


"""
分解质数，做表格，找规律

We are interested in the other thing now. We want to have the fewest factors 
and with the largest primes. Sorting the table the other way around shows that 
indeed the largest primes have the smallest n/phi(n):

There is another insight that we can use. Although the ceiling is 10,000,000, 
we don’t need prime numbers that high. Since we want both prime numbers of the 
same order of magnitude, it is sufficient to only look at primes that are up to 
10,000. This means that we just need to add a factor of 10 to the primes and 
this increases computation cost only a bit.

We can filter the table to only include numbers such that the number and its 
totient are digit permutations. We also increase the ceiling to 100,000 such 
that we get more interesting results. These are the minimum numbers that we get:
"""


# So what is left in the code is just a function that 
# checks for permutations using sort_digits from Solution 62: Cubic permutations
def sort_digits(number: int) -> list[int]:
    return sorted(str(number))

def are_permutations(left: int, right: int) -> bool:
    return sort_digits(left) == sort_digits(right)

# And then the main function goes through the primes which are generated with 
# the prime sieve from Solution 7: 10001st prime:
def prime_sieve(end: int) -> list[int]:
    sieve = [True] * end
    sieve[0] = False
    sieve[1] = False
    for i in range(end):
        if sieve[i]:
            for factor in itertools.count(2):
                number = factor * i
                if number >= len(sieve):
                    break
                sieve[number] = False
    primes = [number for number, state in enumerate(sieve) if state]
    return primes

def solution() -> int:
    primes = prime_sieve(10**5)
    values = []
    for p1 in primes:
        for p2 in primes:
            if p1 == p2:
                break
            number = p1 * p2
            if number > 10**7:
                break
            t = (p1 - 1) * (p2 - 1)
            if are_permutations(t, number):
                values.append((number / t, number))
    return min(values)[1]