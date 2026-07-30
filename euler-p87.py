# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:23:49 2026

@author: phoeb
"""

'''
My approach here is to just iterate through all numbers and see when we reach 
the ceiling.

First we write a helper function which yields all numbers raised to a fixed 
exponent:
'''

import math
import itertools

def powers(primes: list[int], exponent: int) -> iter(list([int])):
    for base in primes:
        yield base**exponent

'''
Then we use the prime sieve from solution 7. With that we go through all the 
squares of prime numbers until we hit the ceiling. Then we add all the cubes, 
again watching the ceiling. Also with the fourth powers. If the sum of these 
four summands is above the ceiling, we stop there. Otherwise we just add the 
number to the set of numbers which can be represented like this.

A more clever way to do this is called the Sieve of Eratosthenes which lets you 
find prime numbers up to a ceiling pretty efficiently. Since I already know the solution I can 
just use that as the ceiling. Otherwise we would have to run the sieve a 
few times until we get to the 10001st prime.
'''


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
    ceiling = 50_000_000
    primes = prime_sieve(int(math.sqrt(ceiling)))
    numbers = set()
    for square in powers(primes, 2):
        if square > ceiling:
            break
        for cube in powers(primes, 3):
            if square + cube > ceiling:
                break
            for quadruple in powers(primes, 4):
                number = square + cube + quadruple
                if number >= ceiling:
                    break
                numbers.add(number)
    return len(numbers)


'''
This way we don’t have to go through all numbers up to 50 million and try to 
decompose them. Rather we can just construct all the numbers that can be written 
like this.

This runs in 481 ms, so it’s not instant. But it should be good enough.
'''