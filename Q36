def dec_to_bin(x):
    return int(bin(x)[2:])

def ispalindrome(i):
	return str(i) == str(i)[::-1]

k = []
for i in range(1,1000001):
	if ispalindrome(i) and ispalindrome(dec_to_bin(i)):
		k.append(i)

print sum(k)
