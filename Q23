a = 20000
k = range(2,a)
m = []
while len(k)>0:
	i = k[0]
	k = [g for g in k if g%k[0] != 0]
	m.append(i)
	if i**2 > a:
		break
	
factor1 =[]
factor2 = []
Sum = 0
list2 = []
for i in range(1,28124) :
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
	if i1 > i:
		list2.append(i)
	factor1 = []
	factor2 = []	
		
list2 = list(set(list2))
list3 = list(set([i+j for i in list2 for j in list2]))
list4 = [i for i in list3 if i < 28124]
print sum(list(set(range(1,28124)) - set(list4)))
