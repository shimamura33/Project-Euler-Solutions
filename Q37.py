import numpy
a = 1000000

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

# test if prime
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# test if truncatable
def is_trun(n):
	n = map(int, str(n))
	n2 = [g for g in n if g != 4 and g != 6 and g != 8]
	if len(n2) == len(n) and len(n2) > 1 and n2[0] != 1 and n2[len(n2)-1] != 1 and n2[0] != 9 and n2[len(n2)-1] != 9:
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

k = [g for g in prime if is_trun(g)]
print k
