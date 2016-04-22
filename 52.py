l = []
for k in range(10000,166666):
	k1 = map(int, str(k))
	if len(set(k1)) == 6:
		g = [k,2*k,3*k,4*k,5*k,6*k]
		g2 = [map(int, str(a)) for a in g]
		g2 = [val for sublist in g2 for val in sublist]
		if len(set(g2)) == 6:
			l.append(k)

print l
