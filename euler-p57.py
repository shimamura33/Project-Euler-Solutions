#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 18:33:15 2025

@author: phoebeliu
"""
##https://raw.org/puzzle/project-euler/problem-57/

## sol 1
import math

def solution(N=1000):
  c = 0
  n = d = 1
  for k in range(N):
    n, d = 2 * d + n, d + n
    if int(math.log10(n)) > int(math.log10(d)):
      c+= 1
  return c

## sol 2
def solution2(N=1000):
  c = 0
  n = d = 1
  np = dp = 10
  for k in range(N):
    n, d = 2 * d + n, d + n
    if n >= np:
      np*= 10
    if d >= dp:
      dp*= 10
    if np > dp:
      c+= 1
  return c