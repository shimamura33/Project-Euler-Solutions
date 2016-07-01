my_list = []
for i in range(80,100):
	for j in range(80,100):
		g = i**j
		my_list.append(sum_of_digits(g))

import operator
index, value = max(enumerate(my_list), key=operator.itemgetter(1))

print my_list
print index
