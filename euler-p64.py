# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:58:53 2026

@author: phoeb
"""

import math

#We can use the given examples to write a test first:

def test_expansion() -> None:
    expand_root(2) == ([1], [2])
    expand_root(3) == ([1], [1, 2])
    expand_root(5) == ([2], [4])
    expand_root(6) == ([2], [2, 4])
    expand_root(7) == ([2], [1, 1, 1, 4])
    expand_root(8) == ([2], [1, 4])
    expand_root(10) == ([3], [6])
    expand_root(11) == ([3], [3, 6])
    expand_root(12) == ([3], [2, 6])
    expand_root(13) == ([3], [1, 1, 1, 1, 6])
    expand_root(23) == ([4], [1, 3, 1, 8])


"""
For the cancellation of the fraction we use greatest_common_denominator from 
Solution 33: Digit cancelling fractions.
"""

def greatest_common_denominator(a: int, b: int) -> int:
    while b != 0:
        b, a = a % b, b
    return a


"""
The first part are the coefficients before the periodic part, the second list is the periodic part.
Now we need to think of actually building this function. Looking at the example, we can see how to proceed. We start with a number $N$. The $\sqrt N$ usually isn&rsquo;t an integer. We define an integer number $f$ such that $f \leq \sqrt N &lt; f+1$ simply by using the floor function, $f := \lfloor \sqrt x \rfloor$. In the first step. The first step is writing $\sqrt N$ as $f + \sqrt N - f$. We know that $\sqrt N - f$ has to be smaller than 1 by definition. This way we can already split off $f$ and have the coefficient $a_0$ from the sequence already.
The next task is to further expand $\frac{1}{\sqrt N - f}$ into the a form $\frac{\sqrt N + f}{d}$. The denominator $d$ is easily found as $N - f^2$ using the third binomial equation. In general we will start from a form $\frac{b}{\sqrt N - c}$ and want to rewrite this as $b \frac{\sqrt N + c}{d}$.
The next step is the most difficult one. We need to pull out a full integer such that the fraction becomes smaller than one. For this we use that $f &lt; \sqrt N &lt; f + 1$ and therefore we can just see what we can do with the fraction $b \frac{f + c}{d}$. We first cancel $b$ and $d$ and then split the fraction into an integer $a_n$ and the new remaining part $\frac{\sqrt N - c&rsquo;}{d&rsquo;}$. In the next step we identify $c = - c&rsquo;$ and $b = d&rsquo;$ and do it again.
"""

def expand_root(number: int) -> tuple[list[int], list[int]]:
    floor = int(math.sqrt(number))
    if floor**2 == number:
        return [floor], []
    results = [floor]
    states = [(1, floor)]
    c = floor
    b = 1
    while True:
        # print()
        assert c > 0
        # print(f"{b}/(sqrt({number}) - {c})")
        d = number - c**2
        gcd = greatest_common_denominator(b, d)
        # print(f"{b} (sqrt({number}) + {c})/{d}")
        b //= gcd
        d //= gcd
        # print(f"{b} (sqrt({number}) + {c})/{d}")
        split = (floor + c) // d
        a = split * b
        c -= split * d
        # print(f"{a} + {b} (sqrt({number}) + {c})/{d}")
        c = -c
        b = d
        state = (b, c)
        results.append(a)
        if state in states:
            break
        states.append(state)
    i = states.index(state) + 1
    return results[:i], results[i:]


def solution() -> int:
    result = 0
    for number in range(2, 10_000):
        beginning, period = expand_root(number)
        if len(period) % 2 == 1:
            result += 1
    return result
