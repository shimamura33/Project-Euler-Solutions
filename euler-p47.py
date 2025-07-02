# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 11:29:57 2025

@author: phoeb
"""

def p47():
	C = 10**6  # it's enough
	s = 0
	p = [0 for m in range(C)]
	for n in range(2, C):
		if p[n] == 4:
			s += 1
			if s == 4:
				return n-3
		else:
			s = 0
		if p[n] == 0:
			for m in range(n, C, n):
				p[m] += 1
                
p47()
