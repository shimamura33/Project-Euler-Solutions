import itertools
import math
from collections import deque
def isPrime(k):
	if k < 2: return False
	elif k == 2: return True
	elif k % 2 == 0: return False
	else:
		for x in range(3,int(math.sqrt(k)+1),2):
			if k % x == 0: return False
		return True

#print isPrime(197)

def is_circular_prime(k):
	if isPrime(k):
		l2 = list(str(k))
		l = [[l2[i-j] for i in range(len(l2))] for j in range(len(l2))]
		#print l
		p = [map(int,x) for x in l]
		#print p
		g = [int(''.join(map(str,x))) for x in p]
		#print g
		return all(isPrime(x) for x in g)
g = []
for i in range(100,1000000):
	if is_circular_prime(i):
		g.append(i)

print len(g) + 13
