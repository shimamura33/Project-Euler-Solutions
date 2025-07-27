#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 19:03:00 2025

@author: phoebeliu
"""

## https://math.berkeley.edu/~elafandi/euler/p51/

'''
<p>From this point onward, the problems start to get a bit harder.</p>

<p>As mentioned in <a href="../p41">my writeup of Problem 41</a>, a number is divisible 
by 3 if and only if the sum of its digits is divisible by 3. Thus, if the fixed 
digits of a number family sum to \(x\) modulo 3, the variable digits must never 
sum to \(-x\) modulo 3. That is, if there are \(k\) variable digits which take 
on values \(t\), then \(kt\) can take on at most two values modulo \(3\). There 
are four digits that are equivalent to 0 mod 3; three digits that are equivalent 
to 1 mod 3; and three digits that are equivalent to 2 mod 3 (in order: 0, 3, 6, 
                                                             and 9; 1, 4, and 7; 2, 5, and 8). 
Any set of eight \(t\) will have at least one element in all three sets. 
Therefore, in order to restrict the values of \(kt\) modulo 3, \(k\) must be divisible by 3.</p>

<p>The assumption that \(k = 3\) is reasonable and ultimately correct, as is the 
assuption that there are three fixed digits. We are thus looking for a family 
of six-digit numbers. Note that the last digit must be fixed, because odd primes 
only end in the digits 1, 3, 7, and 9. There are therefore ten possible patterns f
or a family: AB***C, A*B**C, A**B*C, A***BC, *AB**C, *A*B*C, *A**BC, **AB*C, **A*BC, and ***ABC, w
here "*" represents a variable digit and "A," "B," and "C" represent fixed digits.</p>

'''

from sympy import isprime

def p51():
	patterns = ['{0}{1}{3}{3}{3}{2}', '{0}{3}{1}{3}{3}{2}',
				'{0}{3}{3}{1}{3}{2}', '{0}{3}{3}{3}{1}{2}',
				'{3}{0}{1}{3}{3}{2}', '{3}{0}{3}{1}{3}{2}',
				'{3}{0}{3}{3}{1}{2}', '{3}{3}{0}{1}{3}{2}',
				'{3}{3}{0}{3}{1}{2}', '{3}{3}{3}{0}{1}{2}']
	res = 10 ** 6  # Just in case there were multiple families (there aren't)
	for pattern in patterns:
		for A in range(10):
			if pattern[1] == '0' and A == 0:
				continue
			for B in range(10):
				for C in [1, 3, 7, 9]:
					tmin = 1 if pattern[1] == '3' else 0
					non_primes = tmin
					pmin = int(pattern.format(A, B, C, tmin))
					for t in range(tmin, 10):
						p = int(pattern.format(A, B, C, t))
						if not isprime(p):
							non_primes += 1
							if non_primes > 2:
								break
					if non_primes == 2:
						res = min(res, pmin)
	return res