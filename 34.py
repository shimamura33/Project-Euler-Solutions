import math as m
list1 = []
for i in range(10,2217600):
	k = [int(char) for char in str(i)]
	g = sum([m.factorial(i2) for i2 in k])
	if g == i:
		list1.append(g)
		
print list1
