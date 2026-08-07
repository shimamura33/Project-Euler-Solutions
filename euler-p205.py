# -*- coding: utf-8 -*-
"""
http://projecteuler.net/problem=205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The
result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer
rounded to seven decimal places in the form 0.abcdefg

算法1：蒙特卡罗
First I coded a Monte Carlo simulation to approximate my result, got to the sixth decimal place after ~10 mins of waiting.
After that I had to start thinking smart, my code has 3 functions
    
1、colindice()

Initialise and array = [0]*37 (This is for 1-36 indexing)
Do a 6 times nested loop through the list [1,2,3,4,5,6] each time, at the end you will have the sum of 6 numbers, say sum, between 6-36
array[sum] += 1/(6^6), essentially what this is doing is creating an array which stores the probability of colin rolling a number, after everything is done for example array[18] = 0.07353823

2、peterdice()

I believe you can figure out what I did here from above

3、compute()

Goes through a double nested loop with variables x, y, where x goes from 6-37 (Cubic Colin), y goes from 9-37 (Pyramidal Pete), these represent the sum of the dice rolls for each player
First we create a temp variable say, temptotal. Now we want to find the probability that Pyramidal Pete beats Cubic Colin, therefore if y > x, that is Pyramidal Pete rolls higher than Cubic Colin, then we add the probability of Pyramidal Pete getting that roll, y, which we can find from function peterdice(). After we've done that for every number we multiply temptotal by the probability of Cubic Colin getting the roll x
"""

from itertools import product
from collections import Counter

# 1. Generate all possible outcomes for Peter (9 four-sided dice)
peter_counts = Counter()
for roll in product(range(1, 5), repeat=9):
    peter_counts[sum(roll)] += 1

# 2. Generate all possible outcomes for Colin (6 six-sided dice)
colin_counts = Counter()
for roll in product(range(1, 7), repeat=6):
    colin_counts[sum(roll)] += 1

# 3. Calculate total possible outcome spaces
total_peter_outcomes = 4**9
total_colin_outcomes = 6**6
total_combinations = total_peter_outcomes * total_colin_outcomes

# 4. Count the number of times Peter beats Colin
peter_wins = 0
for p_score, p_count in peter_counts.items():
    for c_score, c_count in colin_counts.items():
        if p_score > c_score:
            peter_wins += p_count * c_count

# 5. Calculate and format the final probability
probability = peter_wins / total_combinations
print(f"Probability: {probability:.7f}")


"""
暴力求解2
"""

# since number of all combinations not so high, just counted all
import itertools

pyramidal_counts = {}
cubic_counts = {}

# pyramidal
for i in itertools.product(range(1, 5), repeat=9):
    s = sum(i)
    pyramidal_counts[s] = pyramidal_counts.get(s, 0) + 1

# cubic
for i in itertools.product(range(1, 7), repeat=6):
    s = sum(i)
    cubic_counts[s] = cubic_counts.get(s, 0) + 1

pyramid_wins = 0
cubic_wins = 0
tie = 0
for i in pyramidal_counts:
    for j in cubic_counts:
        c = pyramidal_counts[i] * cubic_counts[j]
        if i > j:
            pyramid_wins += c
        elif i < j:
            cubic_wins +=c
        else:
            tie +=c

print('%.7f' % (float(pyramid_wins) / (pyramid_wins + cubic_wins + tie)))

print((float(pyramid_wins) / (pyramid_wins + cubic_wins + tie)))