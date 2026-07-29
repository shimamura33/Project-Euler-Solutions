# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:56:16 2026

@author: phoeb
"""

from fractions import Fraction

def main():
    three_sevenths = 3.0 / 7
    closest = Fraction(three_sevenths).limit_denominator(1000000)
    while closest == Fraction(3, 7):
        three_sevenths -= 1e-6
        closest = Fraction(three_sevenths).limit_denominator(1000000)
    print(closest.numerator)

if __name__ == "__main__": main()