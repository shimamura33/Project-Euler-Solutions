# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:18:44 2026

@author: phoeb
"""
import itertools

'''
Project Euler Problem 77: Prime summations continues with number partitions, though we now all summands have to be primes.

We have essentially the same problem as in Solution 76: Counting summations. We are to partition integers into sums of primes. The thing to find out is the smallest number which has over 5,000 partitions in this way.

Using our beloved prime generator from Solution 3: Largest prime factor, we can write an iterator for primes up to that number:
'''

def prime_generator() -> int:
    primes = []
    for candidate in itertools.count(2):
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            yield candidate
            primes.append(candidate)

def primes_up_to(number: int) -> int:
    for prime in prime_generator():
        if prime > number:
            break
        yield prime

'''
Then we adapt the partition function from the previous problem such that it only takes the primes into account. Otherwise it has the same structure. We also need to make sure that we only allow taking just the number when it is a prime itself. For that we use the accelerated prime test from Solution 58: Spiral primes.
'''

def is_prime_accelerated(number: int) -> bool:
    for divisor in prime_generator():
        if number % divisor == 0:
            return False
        if divisor * divisor > number:
            return True


def partitions(number: int, top: int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        result = sum(
            partitions(number - x, min(number - x, x)) for x in primes_up_to(top)
        )
        if number <= top and is_prime_accelerated(number):
            result += 1
        return result

'''
The solution then seeds the prime generator with a sufficient number of primes. I’ve lowered the ceiling after learning what the result is. And then just iterate the numbers until it exceeds the threshold.

Euler problem 7: the Sieve of Eratosthenes which lets you find prime numbers up to a ceiling pretty efficiently. Since I already know the solution I can just use that as the ceiling. Otherwise we would have to run the sieve a few times until we get to the 10001st prime.
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
    prime_generator.__defaults__ = (prime_sieve(72),)
    for i in itertools.count(10):
        if partitions(i, i) > 5_000:
            return i
