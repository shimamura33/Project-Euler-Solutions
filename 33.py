from __future__ import division
import numbers

g = []
for a in range(1,10):
	for c in range(1,10):
		b = (9*a*c)/(10*a-c)
		if b%1 == 0 and b > 0 and a!=c and b < 10:
			g.append((a,b,c))


print g

g = []
for b in range(1,10):
	for c in range(1,10):
		a = (9*b*c)/(10*c-b)
		if a%1 == 0 and a > 0 and b!=c and a < 10:
			g.append((a,b,c))


print g
