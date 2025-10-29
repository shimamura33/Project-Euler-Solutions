# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 17:07:59 2025

@author: phoeb
"""

'''
This can be solved straightforwardly. First we need to have a factorial function 
for the digits. We expect it to be called with the values from 0 to 9, so we 
can happily cache all of them.
'''
def factorial(number: int) -> int:
    result = 1
    for k in range(2, number + 1):
        result *= k
    return result


'''
The next numbers are likely going to occur again and again. Therefore we also 
cache them. In order not to overwhelm the memory, I set a limit for it.
'''
def factorial_digit_sum(number: int) -> int:
    return sum(factorial(int(digit)) for digit in str(number))


'''
And then we just have to iterate through all numbers. We can already stop after 
more than 60 iterations because we only care for the numbers where the length 
is exactly 60 elements.
'''
def solution() -> int:
    result = 0
    for number in range(1_000_000):
        steps = [number]
        for iteration in range(60):
            new_number = factorial_digit_sum(steps[-1])
            if new_number in steps:
                if iteration == 59:
                    result += 1
                break
            steps.append(new_number)
    return result