a = 10000
k = range(2,a)
m = []

# generate primes
while len(k)>0:
	i = k[0]
	k = [g for g in k if g%k[0] != 0]
	m.append(i)
	if i**2 > a:
		break
	
factor1 =[]
factor2 = []
Sum = 0
for i in range(1,10000) :
	j = 0
	while j < len(m):
		g = m[j]
		if g <= i**0.5 and i%g == 0:
			factor1.append(g)
			factor2.append(i/g)
			l=0
			while l < len(factor1):
				k = g * factor1[l]
				if i%k == 0 and k <= i**0.5:
					factor1.append(k)
					factor2.append(i/k)
				l += 1
		j += 1
	factor = factor1 + list(set(factor2) - set(factor1))
	i1 = sum(factor) + 1

	factor1 = []
	factor2 = []
	j = 0
	while j < len(m):
		g = m[j]
		if g <= i1**0.5 and i1%g == 0:
			factor1.append(g)
			factor2.append(i1/g)
			l=0
			while l < len(factor1):
				k = g * factor1[l]
				if i1%k == 0 and k <= i1**0.5:
					factor1.append(k)
					factor2.append(i1/k)
				l += 1
		j += 1
	factor = factor1 + list(set(factor2) - set(factor1))
	apple = sum(factor) + 1

	if i == apple and i != 1 and i != i1:
		summation = i + i1
		Sum+= summation	
	factor1 = []
	factor2 = []

print Sum/2
