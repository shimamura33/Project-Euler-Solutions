# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 11:31:24 2025

@author: phoeb
"""
####https://github.com/TheAlgorithms/Python/blob/master/project_euler/problem_043/sol1.py

from itertools import permutations


def is_substring_divisible(num: tuple) -> bool:
    """
    Returns True if the pandigital number passes
    all the divisibility tests.
    >>> is_substring_divisible((0, 1, 2, 4, 6, 5, 7, 3, 8, 9))
    False
    >>> is_substring_divisible((5, 1, 2, 4, 6, 0, 7, 8, 3, 9))
    False
    >>> is_substring_divisible((1, 4, 0, 6, 3, 5, 7, 2, 8, 9))
    True
    """
    if num[3] % 2 != 0:
        return False

    if (num[2] + num[3] + num[4]) % 3 != 0:
        return False

    if num[5] % 5 != 0:
        return False

    tests = [7, 11, 13, 17]
    for i, test in enumerate(tests):
        if (num[i + 4] * 100 + num[i + 5] * 10 + num[i + 6]) % test != 0:
            return False
    return True


def solution(n: int = 10) -> int:
    """
    Returns the sum of all pandigital numbers which pass the
    divisibility tests.
    >>> solution(10)
    16695334890
    """
    return sum(
        int("".join(map(str, num)))
        for num in permutations(range(n))
        if is_substring_divisible(num)
    )


if __name__ == "__main__":
    print(f"{solution() = }")