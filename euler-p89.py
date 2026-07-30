# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:49:47 2026

@author: phoeb
"""

def subtractive(roman):
    result = roman
    replacements = [
        ("VIIII", "IX"), 
        ("IIII", "IV"), 
        ("LXXXX", "XC"), 
        ("XXXX", "XL"),
        ("DCCCC", "CM"), 
        ("CCCC", "CD"),
    ]
    for old, new in replacements:
        result = result.replace(old, new)
    return result

current = 0
improved = 0
for line in open('E:\\Downloads\\0089_roman.txt'):
    roman = line.strip()
    current += len(roman)
    improved += len(subtractive(roman))
print(current - improved)