import itertools
import math
def is_prime(n):
    for i in range(2, int(math.floor(n**0.5))):
        if n % i == 0:
            return False
    return True

g = []

for k in range(4,8):
	iterable = range(1,k+1)
	iterable = [a for a in itertools.permutations(iterable,k)]
	iterable2 = [reduce(lambda rst, d: rst * 10 + d, a) for a in iterable]
	for b in iterable2:
		if is_prime(b):
			g.append(b)
			
print g
