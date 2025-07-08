# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 14:46:35 2025

@author: phoeb
"""

##### https://stackoverflow.com/questions/54385550/code-on-pentagonal-numbers-takes-too-long-to-execute

from bisect import bisect_left

pentagonal = []
for n in range(1, 10000):
    p = int((n*(3*n - 1))/2)
    pentagonal.append(p)


def bisect_search(lst, item):
    ''' it is used for sorted lists'''
    return (item <= lst[-1]) and (lst[bisect_left(lst, item)] == item)


for i in pentagonal:
    for j in pentagonal:
        diff = abs(i - j)
        sam = i + j
        if bisect_search(pentagonal, sam) and bisect_search(pentagonal, diff):
            print("(", i, ":", j, ")")