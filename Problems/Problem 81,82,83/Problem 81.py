#Problem 81
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#'131'	673	234	103	18
#'201'	'96'	'342'	965	150
#630	803	'746'	'422'	111
#537	699	497	'121'	956
#805	732	524	'37'	'331'

#Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."),
#a 31K text file containing an 80 by 80 matrix.


matrix_file = open('C:\\Users\\PC\\Desktop\\Project Euler\\Problem 81,82,83\\matrix.txt').read()

rows = [row for row in matrix_file.split('\n') if row]
matrix = [[int(element) for element in row.split(',')] for row in rows]

for j in range(1, 80):
    matrix[0][j] += matrix[0][j-1]
for i in range(1, 80):
    matrix[i][0] += matrix[i-1][0]


for i in range(1,80):
    for j in range(1,80):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

print(matrix[79][79])
