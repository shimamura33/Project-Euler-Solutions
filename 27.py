import math

def longestPrimeQuadratic(alim,blim):
	def isPrime(k):
		if k < 2: return False
		elif k == 2: return True
		elif k % 2 == 0: return False
		else:
			for x in range(3,int(math.sqrt(k)+1),2):
				if k % x == 0: return False
			return True
	longest = [0,0,0]
	for a in range((alim*-1+1),alim):
		for b in range(2,blim):
			if isPrime(b):
				count = 1
				while isPrime(count**2+a*count+b):
					count += 1
				if count > longest[0]:
					longest = [count,a,b]
					
	return longest

print longestPrimeQuadratic(1000,1000)
