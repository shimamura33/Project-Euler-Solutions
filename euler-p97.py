# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:15:39 2025

@author: phoeb
"""

##https://martin-ueding.de/posts/project-euler-solution-97-large-non-mersenne-prime/
############ solution 1
def solution_naive() -> int:
    return (28433 * 2**7830457 + 1) % 10**10

solution_naive() 


############ solution 2
def solution_modulus() -> int:
    divisor = 10**10
    number = 28433
    for i in range(7830457):
        number *= 2
        number %= divisor
    number += 1
    number %= divisor
    return number

solution_modulus()