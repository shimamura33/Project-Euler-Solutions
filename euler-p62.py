# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 14:51:09 2025

@author: phoeb
"""

### https://github.com/TheAlgorithms/Python/blob/master/project_euler/problem_062/sol1.py

from collections import defaultdict


def solution(max_base: int = 5) -> int:
    """
    Iterate through every possible cube and sort the cube's digits in
    ascending order. Sorting maintains an ordering of the digits that allows
    you to compare permutations. Store each sorted sequence of digits in a
    dictionary, whose key is the sequence of digits and value is a list of
    numbers that are the base of the cube.

    Once you find 5 numbers that produce the same sequence of digits, return
    the smallest one, which is at index 0 since we insert each base number in
    ascending order.

    >>> solution(2)
    125
    >>> solution(3)
    41063625
    """
    freqs = defaultdict(list)
    num = 0

    while True:
        digits = get_digits(num)
        freqs[digits].append(num)

        if len(freqs[digits]) == max_base:
            base = freqs[digits][0] ** 3
            return base

        num += 1


def get_digits(num: int) -> str:
    """
    Computes the sorted sequence of digits of the cube of num.

    >>> get_digits(3)
    '27'
    >>> get_digits(99)
    '027999'
    >>> get_digits(123)
    '0166788'
    """
    return "".join(sorted(str(num**3)))


if __name__ == "__main__":

    print(f"{solution() = }")
