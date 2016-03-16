a = 10000000
k = range(2,a)
m = []

# generate primes
while len(k)>0:
	i = k[0]
	k = [g for g in k if g%k[0] != 0]
	m.append(i)
	if i**2 > a:
		break
print m		
# generate triangle numbers
x = range(1,40000)
triangle = []
for i in range(len(x)):
	triangle.append(sum(x[:i]))

triangle = triangle[800:]
print triangle

# divison
powerbig = []
factorbig = []
for i in triangle:
	j = 0
	factor = []
	power = []
	while j <len(m):
		g = m[j]
		if g<i and i%g == 0:
			k = 1
			factor.append(g)
			while i%g == 0:
				k += 1
				g = g**k
			power.append(k-1)
		j+=1
	powerbig.append(power)
	factorbig.append(factor)

for i in range(len(powerbig)):
	powerbig[i] = [j+1 for j in powerbig[i]]

from numpy import prod
k=list(map(prod,powerbig))
print k

g=min([i for i in range(len(k)) if k[i] > 500])
print triangle[g]
