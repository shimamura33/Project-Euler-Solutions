# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:20:16 2026

@author: phoeb
"""
# http://radiusofcircle.blogspot.com

#import time
import time

# square root function
from math import sqrt

# time at the start of program execution
start = time.time()

'''
If you have already solved Problem 64 on Project euler, then assume that this 
one is an extension to Problem 64.

The solution is based on two approaches: Chakravala method(Page No:3) 
http://www.isibang.ac.in/~sury/chakravala.pdf

and 
Continued Fraction method(Page No: 18). 
https://ir.canterbury.ac.nz/server/api/core/bitstreams/7f14fb64-bc37-46b8-9d2d-0d705cab0319/content

And to find continued fractions 
I have used this source: Wikipedia - Methods of Computing square roots.

There are four things that we will have to understand from the sources:
If the period of the continued fraction is even then we are finding the solution for the positive pells equation - $ x^{2} - Dy^{2} = 1 $
If the period of the continued fraction is odd then we are finding the solution for the negative pells equation - $ x^{2} - Dy^{2} = -1 $
What ever might be the case, we don't need the last value of the convergent list. i.e. in our case $ \sqrt{19} = [4;2,1,3,1,2] $ instead of $ [4;2,1,3,1,2,8] $
If we are solving the negative pells equation, then we will use Baskara's Lemma to get the required answer.
'''

# function to calculate the continued fraction
def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    convergents = [a0]
    period = 0
    if a0 != sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

def cf_inv(cf):
    """
    function to calculate the
    simple fraction from the continued
    fraction.
    """
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator, numerator = denominator*cf.pop() + numerator, denominator
    return denominator, numerator

# variable to store the largest value 
# and the place it occurs
largest = 0, 0

# for loop less than 1000
for i in range(1, 1001):
    if i%sqrt(i) != 0:
        continued_fraction = cf(i)
        if len(continued_fraction) % 2 != 0:
            u, v = cf_inv(continued_fraction)
            u, v = 2*u**2+1, 2*u*v
        else:
            u, v = cf_inv(continued_fraction)
        if u > largest[1]:
            largest = i, u

# print the largest value
print(largest[0])

# time at the end of program execution
end = time.time()

# total time taken to run the program
print(end - start)



'''
I have tried to name the variables as meaningful as possible. But a brief explanation is as follows:
The function <code>cf</code> will take a number($ n $) as input and calculate the continued fraction for square root of the number($ \sqrt{n} $).
So the expected output will be <code>[a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, .........., a<sub>n</sub>]</code>. Also from the reference, we know that <code>a<sub>n</sub> = 2a<sub>0</sub></code>. We also know that, to solve pell's equation we don't need the last value(a<sub>n</sub>) and so <code>cf</code> will return a list with values excluding the last number.
The function <code>cf_inv</code> will take a list(List of continued fraction values) as input and will return the numerator and the denominator if the list is written as a simple fraction.
For example, consider the list: [2, 3, 4, 5]. This list when written as a continued fraction will be as follows:
    \begin{equation}
  x = 2 + \cfrac{1}{3 
          + \cfrac{1}{4 
          + \cfrac{1}{5} } }
\\
\implies
  x = 2 + \cfrac{1}{3 
          + \cfrac{5}{21} }
  \\
  \implies
  x = 2 + \cfrac{21}{68}
  \\
  \implies
  x = \cfrac{157}{68}
\end{equation}


Now that you have understood how the function works in the background, we will 
use tweak the function so that it will print the numerator and denominator for 
each and every iteration.
'''
def cf_inv(cf):
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator, numerator = denominator*cf.pop() + numerator, denominator
        print(numerator, denominator)
    return denominator, numerator

print(cf_inv([2, 3, 5, 7]))
