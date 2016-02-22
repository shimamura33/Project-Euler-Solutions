a = 1000
k = range(2,a)
prime = []

# generate primes
while len(k)>0:
	i = k[0]
	k = [g for g in k if g%k[0] != 0]
	print k
	prime.append(i)
	if i**2 > a:
		break
		
prime = prime.remove(2)
prime = prime.remove(3)
prime = prime.remove(5)
prime = prime.remove(7)
prime = prime.remove(23)

print prime

# test if prime
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# test if truncatable
def is_trun(n):
	n = map(int, str(n))
	n2 = [g for g in n if g%2 == 0 and g != 1]
	if len(n2) == len(n):
		for i in range(1,len(n2)):
			g = int(''.join(map(str, map(int, n))[i:]))
			if is_prime(g) is False:
				return False
				break
			g = int(''.join(map(str, map(int, n))[:i]))
			if is_prime(g) is False:
				return False
				break
		return True
	return False

g = [g in prime if is_trun(g) is True]
print g
