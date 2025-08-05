# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 17:15:43 2025

@author: phoeb
"""

### https://martin-ueding.de/posts/project-euler-solution-99-largest-exponential/

import math

def get_pairs() -> list[tuple[int, int]]:
    with open("D:/Downloads/0099_base_exp.txt") as f:
        return [tuple(map(int, line.split(","))) for line in f]
    
def solution_logarithm() -> int:
    pairs = get_pairs()
    numbers = [exponent * math.log(base) for base, exponent in pairs]
    argmax = sorted(enumerate(numbers, 1), key=lambda t: t[1])[-1][0]
    return argmax