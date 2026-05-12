#Problem 83
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
#by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

#'131'	 673	'234'	'103'	'18'
#'201'	'96'	'342'	 965	'150'
# 630	 803	 746	'422'	'111'
# 537	 699	 497	'121'	 956
# 805	 732	 524	'37'	'331'

#Find the minimal path sum from the top left to the bottom right by moving left, right, up,
#and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

import heapq

matrix_file = open('C:\\Users\\PC\\Desktop\\Project Euler\\Problem 81,82,83\\matrix.txt').read()

matrix = [[int(element) for element in row.split(',')] for row in matrix_file.split('\n') if row]

def shortest_from_tl_to_br(grid, n, m): #n rows, m columns, m x n grid
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    dist[0][0] = matrix[0][0]
    pq = []        
    heapq.heappush(pq, (dist[0][0], 0, 0))
    while pq:
        d, i, j = heapq.heappop(pq)
        A_ij = dist[i][j]
        if d > A_ij:
            continue
        if d < A_ij:
            dist[i][j] = d
            A_ij = dist[i][j]
        if i == n - 1 and j == m - 1:
            return d
        if i < n - 1:
            heapq.heappush(pq, (matrix[i+1][j] + A_ij, i+1, j))
        if j < m - 1:
            heapq.heappush(pq, (matrix[i][j+1] + A_ij, i, j+1))
        if i > 0:
            heapq.heappush(pq, (matrix[i-1][j] + A_ij, i-1, j))
        if j > 0:
            heapq.heappush(pq, (matrix[i][j-1] + A_ij, i, j-1))

print(shortest_from_tl_to_br(matrix, 80, 80))

'''
def shortest_from_tl_to_br(grid):
    n = len(grid)
    m = len(grid[0])

    INF = float('inf')
    dist = [[INF for _ in range(m)] for _ in range(n)]

    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]  # (distance, row, col)

    while pq:
        d, i, j = heapq.heappop(pq)

        # Skip stale entries
        if d > dist[i][j]:
            continue

        # Final answer when target is finalized
        if i == n - 1 and j == m - 1:
            return d

        # Relax neighbors
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                new_cost = d + grid[ni][nj]
                if new_cost < dist[ni][nj]:
                    dist[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))

    return None'''
    
    
