for k in range(100000000,138902663):
	m = k**2
	g = [int(i) for i in str(m)]
	if g[0] == 1 and g[2] == 2 and g[4] == 3 and g[6] == 4 and g[8] == 5 and g[10] == 6 and g[12] == 7 and g[14] == 8 and g[16] == 9:
		print k*10
