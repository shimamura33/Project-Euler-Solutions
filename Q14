m = []
k = range(10000,1000000)
for n in k:
	l = 0
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n+1
		l+=1
	m.append(l)

	
print m
import numpy as np
ind = np.argmax(m)
print k[ind]
