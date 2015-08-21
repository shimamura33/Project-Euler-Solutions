a = 60085
k = range(2,a**0.5+1)
p = 2
n1 = 0
n2 = 1
i = k[n1]
k2 = []

# implement Sieve of Eratosthenes
#while n1 < len(k)-1:
#	while n2 < len(k):
#		g = k[n2]
#		if g % i == 0:
#			k.remove(g)
#		n2+=1
#	n1+=1
#	i = k[n1]
#	n2 = 1+n1


# find the largest prime factor
while n1 < len(k)-1:
	if a % i == 0:
		a = a / i
		sqrt_a = a**0.5+1
		k = [x for x in k if x <= sqrt_a and x%i != 0]
		k2 = k2.append(i)
	else:
		while n2 < len(k):
			g = k[n2]
			k = [x for x in k if x % g != 0]
	n1 += 1
	if n1 < len(k) - 1:
		i = k[n1]
		n2 = 1+n1
	else:
		print k2
		print k
