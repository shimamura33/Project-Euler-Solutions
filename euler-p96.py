# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:09:28 2026

@author: phoeb
"""

from numpy import zeros
from urllib.request import urlopen

'''
Making the grid where every puzzle will be stored

Here is were I use the first library (numpy, zeros) that helps me to create a 
9*9 grid where every puzzle will be stored.
'''

grid = zeros(shape=(9, 9))

'''
How to find the next empty cell to fill

There are two loops that scan the grid start where the last cell was, if it’s 
the first time it starts from the first cell of the grid.

    Empty cells are marked with a 0.
'''

def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

'''
Finding which number is correct for the selected cell

First, I check if the selected n number is valid in the row its cell is placed, 
and then if it is true, we check the column. Finally if that is also true we 
check the number exist in another cell in its inner smaller box. I use the all() 
script because it returns a boolean result of (true/false).
'''

def isValid(grid, i, j, n):
    if all([n != grid[i][x] for x in range(9)]):
        if all([n != grid[x][j] for x in range(9)]):
            X0, Y0 = 3 * (i // 3), 3 * (j // 3)
            for x in range(X0, X0 + 3):
                for y in range(Y0, Y0 + 3):
                    if grid[x][y] == n:
                        return False
            return True
    return False

'''
Solving the Sudoku itself

In order to solve the puzzle, I use recursion by testing every number from [1/10] 
if it is valid in every empty cell.
'''

def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True # If there is no next cell.
    for n in range(1, 10):
        if isValid(grid, i, j, n):
            grid[i][j] = n
            if solveSudoku(grid):
                return True # If Su Doku is solved.
            grid[i][j] = 0
    return False # This is were recursion happens.

'''
Equipping solver to the problem

Finally, this is the last block of code, and it’s were I use the second library 
(urlopen), which gives me the ability to open the text file with the fifty 
puzzles without downloading it to my system, thus of course it works in any 
system. The only difference in Python 3 is that the lines of the file have to 
be decoded in order to use them properly. The idea behind this is that because 
every grid in the file is numbered (for example: Grid 01), Every time it passes 
one like that line (except the first time), it knows that the nine previous line 
make the previous grid, so then is solves it and then finds the result. 
Otherwise, when it encounters a “normal” grid line, it inserts it to the grid 
in order to be solved. With this method, the program is able to solve every Su 
Doku grid except the last one, cause there is no line “Grid 51” in order to be 
calculated. To solve this I thought that the simplest solution is to check every 
“normal” line if it equals with the last line of the file, and if it does it 
calculates the last Su Doku grid.
'''

file = urlopen("https://projecteuler.net/project/resources/p096_sudoku.txt")

count, result = 0, 0
for line in file:
    line = line.decode('utf-8')
    if line[0] == 'G':
        if count != 0: # It doesn't allow for line "Grid 01" to calculate a grid.
            count = 0 # It resets every time a grid is calculated.
            solveSudoku(grid)
            result += 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]
    else:
        for i in range(9):
            grid[count][i] = int(line[i]) # In order to solve the grid, it must contain integers and not characters.
        count += 1
        if line == "000008006": # The last line of the file.
            solveSudoku(grid)
            result += 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]
            break
file.close()
print(result)

'''
In the end, knowing the speed of Python and wanting to make a easy to understand 
by anyone program, and not the quickest possible, the program takes ~2 minutes 
to calculate the result.
'''