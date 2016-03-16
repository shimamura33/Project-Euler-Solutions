file = open('p067_triangle.txt','r')
grid = file.readlines()

for i in range(len(grid)):
	grid[i] = grid[i].split(' ')
	grid[i] = [int(grid[i][j]) for j in range(len(grid[i]))]

grid = grid[::-1]

j = 1
k1 = grid[j]
print k1
k2 = grid[j-1]
print k2
while j < len(grid)-1:
	for i in range(len(k1)):
		k1[i] = max(k2[i],k2[i+1]) + k1[i]
	
	print k1
	j+=1
	k2 = k1
	k1 = grid[j]

print k1
