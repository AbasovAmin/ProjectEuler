#Problem 96
#Check projecteuler.net

import copy

sudoku_file = open('sudoku.txt').read()

nums = set(['1','2','3','4','5','6','7','8','9'])

lines = [line for line in sudoku_file.strip().split('\n')]

grids = {lines[i]: [[j for j in line] for line in lines[i+1:i+10]] for i in range(0, 491, 10)}
    
def solve(grid):
    dct_of_possibilities = {}
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '0':
                nums_ex = set()
                for row_o in range(9): #Check the numbers in the same column
                    nums_ex.add(grid[row_o][col])
                    
                for col_o in range(9): #Check the numbers in the same row
                    nums_ex.add(grid[row][col_o])

                #Check the numbers in the same 3x3 box
                row_b_start = (row//3)*3
                col_b_start = (col//3)*3
                for row_b in range(row_b_start, row_b_start + 3): 
                    for col_b in range(col_b_start, col_b_start + 3):
                        nums_ex.add(grid[row_b][col_b])
                        
                dct_of_possibilities[(row, col)] = nums.difference(nums_ex)
                #In the past loops, we did not exile the cell itself since it is already 0 and 0 will be
                #overlooked in the difference of the sets since it is in nums_ex and not in nums
            else:
                dct_of_possibilities[(row, col)] = set(grid[row][col])

    return int(''.join(list(new_branch(dct_of_possibilities)[(0, col)])[0] for col in range(3)))

#Now we continue with the actual solving part
def new_branch(dct):

    propagated = set()
    
    while True:
        made_changes = False
        for row in range(9):
            for col in range(9):
                set_of_values = dct[(row, col)]
                
                if len(set_of_values) == 0:
                    return False
                
                if len(set_of_values) == 1 and (row, col) not in propagated:
                    propagated.add((row, col))
                    
                    dct = update(dct, row, col, set_of_values) 
                    made_changes = True
        
        if not made_changes:
            break

    if len(propagated) == 81:
        return dct
    
    size = 2
    while True:
        for row in range(9):
            for col in range(9):
                set_of_values = dct[(row, col)]
                if len(set_of_values) == size:
                    for value in set_of_values:
                        dct_new = update(copy.deepcopy(dct), row, col, value)
                        finished_dct = new_branch(dct_new)
                        if finished_dct != False:
                            return finished_dct
                    return False

        size += 1

def update(dct, row, col, value):
    set_value = set(value)
    dct[(row, col)] = set_value
    for row_o in range(9): #Remove the value from the number's possibilities in the same column
        if row_o == row:
            continue
        dct[(row_o, col)] = dct[(row_o, col)].difference(set_value)
        
    for col_o in range(9): #Remove the value from the number's possibilities in the same row
        if col_o == col:
            continue
        dct[(row, col_o)] = dct[(row, col_o)].difference(set_value)

    #Remove the value from the number's possibilities in the same 3x3 box
    row_b_start = (row//3)*3
    col_b_start = (col//3)*3
    for row_b in range(row_b_start, row_b_start + 3): 
        for col_b in range(col_b_start, col_b_start + 3):
            if row_b == row and col_b == col:
                continue
            dct[(row_b, col_b)] = dct[(row_b, col_b)].difference(set_value)
            
    return dct
                 
count = 0

for grid in grids:
    count += solve(grids[grid])

print(count)
