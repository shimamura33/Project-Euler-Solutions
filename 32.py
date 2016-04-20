import itertools

# 1-digit number multiplies 4-digit number
g = []
for k in range(2,10):
	iterable = range(1,10)
	iterable.remove(k)
	iterable = [a for a in itertools.permutations(iterable,4)]
	iterable2 = [reduce(lambda rst, d: rst * 10 + d, a) for a in iterable]

	for b in iterable2:
		c = k*b
		c2 = map(int, str(c))
		if len(set(c2)) == 4 and 0 not in c2:

			s = map(int, str(c)) + map(int, str(b)) + map(int, str(k))
			if len(set(s)) == 9 and len(s)==9:
				g.append((k,b,c))

print g

# 2-digit number multiplies 3-digit number
g = []
for k in range(12,100):
	k1 = map(int, str(k))
	if len(set(k1)) == 2 and 0 not in k1:

		iterable = range(1,10)
		iterable = [x for x in iterable if x not in k1]

		iterable = [a for a in itertools.permutations(iterable,3)]
		iterable2 = [reduce(lambda rst, d: rst * 10 + d, a) for a in iterable]	

		for b in iterable2:
			c = k*b
			c2 = map(int, str(c))
			if len(set(c2)) == 4 and 0 not in c2:
	
				s = map(int, str(c)) + map(int, str(b)) + map(int, str(k))
				if len(set(s)) == 9 and len(s) == 9:
					g.append((k,b,c))

print g
