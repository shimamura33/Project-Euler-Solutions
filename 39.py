def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

p = []
for i in range(1,500):
	for j in range(1,500):
		if is_square(i**2 + j**2) and (i**2 + j**2)**(0.5) > 250:
			p.append(i + j + (i**2 + j**2)**(0.5))
			print p

from collections import defaultdict

d = defaultdict(int)
for i in p:
  d[i] += 1
most_frequent = sorted(d.iteritems(), key=lambda x: x[1], reverse=True)[0]

print most_frequent
