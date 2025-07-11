# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 13:19:30 2025

@author: phoeb
"""

#### https://raw.org/puzzle/project-euler/problem-55/

def reverse(x):
  n = 0
  while x > 0:
    n = n * 10 + x % 10
    x = x // 10
  return n

def isPalindrome(n):
  return reverse(n) == n

def isLychrel(n):
  for i in range(50):
    n+= reverse(n)
    if isPalindrome(n):
      return False
  return True


cnt = 0
for i in range(10000):
  if isLychrel(i):
    cnt+= 1

print(cnt)