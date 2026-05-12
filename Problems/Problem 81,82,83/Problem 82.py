#Problem 82
#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and
#finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
#131	673	'234'	'103'	'18'
#'201'	'96'	'342'	965	150
#630	803	746	422	111
#537	699	497	121	956
#805	732	524	37	331
#Find the minimal path sum from the left column to the right column in matrix.txt
#(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

matrix_file = open('matrix.txt').read()

matrix = [[int(element) for element in row.split(',')] for row in matrix_file.split('\n') if row]

def right_and_up(grid, a, n): #Calculation of column a based on column a - 1 with only right and up movements
    prev = [grid[i][a-1] for i in range(n)]
    col  = [grid[i][a]   for i in range(n)]
    new  = [0] * n

    new[0] = col[0] + prev[0]

    for i in range(1, n):
        new[i] = col[i] + min(prev[i], new[i-1])

    return new

def right_and_down(grid, a, n): #Calculation of column a based on column a - 1 with only right and down movements
    prev = [grid[i][a-1] for i in range(n)] 
    col  = [grid[i][a]   for i in range(n)] 
    new  = [0] * n

    new[n-1] = col[n-1] + prev[n-1]

    for i in range(n-2, -1, -1):
        new[i] = col[i] + min(prev[i], new[i+1])

    return new


def column_by_column_calculation(grid):
    n = len(grid)
    m = len(grid[0])

    for j in range(1,m):
        up = right_and_up(grid, j, n)
        down = right_and_down(grid, j, n)
        for i in range(n):
            grid[i][j] = min(up[i], down[i])

    return min(grid[i][m-1] for i in range(n)), [grid[i][m-1] for i in range(n)]

print(column_by_column_calculation(matrix))
            

    

    

    

    
