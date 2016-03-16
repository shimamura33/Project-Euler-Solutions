triangle = [1,1]
triangle2 = []
for j in range(39):
	triangle2.append(1)
	for i in range(len(triangle)-1):
		triangle2.append(triangle[i]+triangle[i+1])
	triangle2.append(1)
	triangle = triangle2
	triangle2 = []
	j += 1


print triangle[20]
