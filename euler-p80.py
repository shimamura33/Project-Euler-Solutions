# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:52:13 2026

@author: phoeb
"""

import math

'''
Most square roots are irrational numbers, for instance $\sqrt 2 = 1.4142135623730951\ldots$. We are asked to give the sum of the first 100 digits of the irrational square roots of the first 100 natural numbers.
This means that we have to compute a handful of square roots to 100 digits. The FP64 data type that we have in Python has only around 18 decimal digits of precision, so that is not sufficient here. We would need around 300 bits, and there is no native type for that. We therefore need to have a more clever way to compute the square roots. Perhaps we can make use of the arbitrary size integers in Python for this.
One way could be to compute $10^{100} \cdot \sqrt{2}$ as an integer. This way we would have just shifted the comma enough to do it with integers.
In order to compute $x = \sqrt{a}$ we just use Heron&rsquo;s method and iterate the solution candidate $x$ like so:
$$ x := \frac 12 \left( x + \frac ax \right) ,. $$
And we do this until $x$ doesn&rsquo;t change between iterations. $x$ and $a$ are both integers, so we will have some rounding issues here. To compensate for this, we will try to compute a couple of additional digits.
We can take the example from the problem statement and turn that into a test case:
'''

'''
We have used the digit_sum function from Solution 56: Powerful digit sum.

Then we implement this using Heron’s method:
'''
def digit_sum(number: int) -> int:
    return sum(map(int, str(number)))

def test_sqrt_digits() -> None:
    sqrt_2 = sqrt_digits(2)
    assert digit_sum(sqrt_2[:100]) == 475


def sqrt_digits(number: int) -> str:
    number *= 10**250
    root = number
    for i in range(100000):
        old = root
        root = (root + number // root) // 2
        if old == root:
            break
    return str(root)

'''
The ceiling of 100,000 is just there to prevent an endless loop. It takes around 500 iterations to compute $\sqrt 2$ to the precision that we want.
And then the solution is just adding up all the digits from the first 100 numbers.
'''

def solution() -> int:
    result = 0
    for i in range(100):
        if math.floor(math.sqrt(i)) ** 2 != i:
            result += digit_sum(sqrt_digits(i)[:100])
    return result

