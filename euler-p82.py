# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:09:31 2026

@author: phoeb
"""

'''
Problem #82 is a more complex version of Problem #81.

As mentioned above, this problem is very similar to Problem 81. The only 
difference is that in this case, the path can start anywhere on the left edge 
and it can move up. These changes do not require the solution to be significantly 
different, so my solution for this problem is similar to my solution for Problem 
81. Here’s my solution:

Solution #1: Dynamic Approach

We simply go from left to right across the grid, finding the minimum path sum 
to each cell one column at a time. The first column can be found by simply 
storing the first column of the given grid. Each successive column can be 
calculated by iterating through the previous column and finding the minimum 
path sum from each cell in the previous column to each cell in the next column. 
By this method, the minimum path to each column can be generated dynamically. 
Here is an implementation of this approach:
'''

import time
 
f = open("E:\\Downloads\\0082_matrix.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(list(map(int,x.split(","))))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemEightyTwo(myGrid):
    newGrid = []
    rows = len(myGrid)
    cols = len(myGrid[0])
    for x in range(rows):
        newGrid.append([myGrid[x][0]])
    for y in range(1,cols):
        theColumn = []
        for x in range(rows):
            theColumn.append(myGrid[x][y])
        forwardPartials = [0]
        t = 0
        for x in theColumn:
            t+=x
            forwardPartials.append(t)
        backwardPartials = [t]
        for x in range(rows-1,-1,-1):
            t-=theColumn[x]
            backwardPartials.append(t)
        newColumn = []
        for z in range(rows):
            minFound = newGrid[z][y-1]+myGrid[z][y]
            for a in range(rows):
                if(a<z):
                    total = myGrid[z][y] + forwardPartials[z]-forwardPartials[a] + newGrid[a][y-1]
                elif(a>z):
                    total = myGrid[z][y] + forwardPartials[a+1] - forwardPartials[z+1] + newGrid[a][y-1]
                else:
                    total = minFound
                if(total<minFound):
                    minFound = total
            newColumn.append(minFound)
        for x in range(rows):
            newGrid[x].append(newColumn[x])
    minFound = newGrid[0][cols-1]
    for a in range(1,rows):
        v = newGrid[a][cols-1]
        if(v<minFound):
            minFound = v
    return minFound

start = time.time()
print(projectEulerProblemEightyTwo(realContents))
print("--- %s seconds ---" % (time.time()-start))