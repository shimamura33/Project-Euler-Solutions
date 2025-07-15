# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 18:04:39 2025

@author: phoeb
"""

## https://math.berkeley.edu/~elafandi/euler/p58/

'''
Let n be the (odd) length of the square just after completing one full layer; then 
the new entries on the diagonals are in the four corners. The bottom-right corner 
has value n^2, the bottom-left has value n^2-n+1
, the top-left has valuen n^2-2n+2, and the top-right has value  n^2-3n+3
. As a square, the first of these values cannot be prime, but the other 
three might be. My code keeps running tallies of how many diagonal entries 
have been seen and how many are prime, and breaks out when the ratio falls 
below 10%.
'''

from itertools import count
from sympy import isprime

def p58(target = 1/10):
	a, b = 3, 5
	for n in count(5, 2):
		for p in [n**2-n+1, n**2-2*n+2, n**2-3*n+3]:
			if isprime(p):
				a += 1
		b += 4
		if a/b < target:
			return n