## ------------------------------------------------------------------------------------------------- ##
## Call functions (could be found in shimamura33/Functions/Python)                                   ##
## ------------------------------------------------------------------------------------------------- ##

import numpy
import math
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def is_prime(n):
    for i in range(2, int(math.floor(n**0.5))):
        if n % i == 0:
            return False
    return True
	
## ------------------------------------------------------------------------------------------------- ##
## Get results using the called functions above                                                      ##
## ------------------------------------------------------------------------------------------------- ##

l = []
g = primes(10000) 
print g
for i in range(0,len(g)):
	k = sum(g[3:i+1])
	if is_prime(k) and k < 1000000:
		l.append(k)
		
print l
