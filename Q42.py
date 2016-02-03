# This question has roughly the same solution as Q22
file = open('p042_words.txt','r')
grid = file.readline().split(',')
grid = [ a.replace('"', '') for a in grid ]

for i in range(len(grid)):
	grid[i] = [str(grid[i][j]) for j in range(len(grid[i]))]

grid2 = []
for i in range(len(grid)):
	grid2.append(sum(ord(char.lower())-96 for char in grid[i]))

# generate triangle numbers
triangle = [x*(x+1)/2 for x in range(1,20)]

triangle2 = [val for val in grid2 if val in triangle]
print len(triangle2)
