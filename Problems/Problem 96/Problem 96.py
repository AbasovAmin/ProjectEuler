#Problem 96
#Check projecteuler.net

sudoku_file = open('sudoku.txt').read()

lines = [line for line in sudoku_file.strip().split('\n')]

grids = {lines[i]: [[j for j in line] for line in lines[i+1:i+10]] for i in range(0, 491, 10)}

def solve(grid):
    
        

count = 0

for grid in grids:
    count += solve(grids[grid])
