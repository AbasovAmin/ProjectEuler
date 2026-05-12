triangle_file = open('triangle.txt')

list_of_rows = []

for row in triangle_file.read().split('\n'):
    row_list = [int(x) for x in row.split()]
    list_of_rows.append(row_list)

for i in range(len(list_of_rows) - 2, -1, -1):
    for k in range(len(list_of_rows[i])):
        list_of_rows[i][k] += max(list_of_rows[i+1][k], list_of_rows[i+1][k+1])

print(list_of_rows[0][0])
