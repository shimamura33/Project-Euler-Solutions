## ----------------- ##
## Idea: brute force ##
## ----------------- ##

T = [n*(n+1)/2 for n in range(1,100000)]
P = [n*(3*n-1)/2 for n in range(1, 100000)]
H = [n*(2*n-1) for n in range(1, 100000)]

s = set(T).intersection(P)
print s.intersection(H)
