file = open('p022_names.txt','r')
grid = file.readline().split(',')
grid = [ a.replace('"', '') for a in grid ]
grid.sort()

for i in range(len(grid)):
	grid[i] = [str(grid[i][j]) for j in range(len(grid[i]))]

grid2 = []
for i in range(len(grid)):
	grid2.append(sum(ord(char.lower())-96 for char in grid[i]))

print grid2

grid3 = range(1,len(grid2)+1)

print sum([i*j for (i, j) in zip(grid2, grid3)])
