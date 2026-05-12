#Problem 85
#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
#Although there exists no rectangular grid that contains exactly
#two million rectangles, find the area of the grid with the nearest solution.

#Function to find for specific nxm rectangles
'''def num_of_rectangles(n, m):
    count = 0
    for i in range(1, n + 1):
        column_placements = n - i + 1
        for j in range(1, m + 1):
            row_placements = m - j + 1
            count += column_placements * row_placements
    return count'''

Limit = 60  #Can be verified using n(n+1)/2 < sqrt(2_000_000)
T = [0]*(Limit + 1)
for i in range(1, Limit + 1):
    T[i] = T[i-1] + i   # triangular numbers


def go_till_nearest_to(LIMIT = 2_000_000):
    best_diff = float('inf')
    area = 0
    for i in range(1, Limit + 1):
        for j in range(i, Limit + 1):
            rectangles = T[i] * T[j]
            if rectangles > LIMIT + best_diff:
                break
            diff = abs(rectangles - LIMIT)
            if diff < best_diff:
                best_diff = diff
                area = i*j
    return area, best_diff

print(go_till_nearest_to(2_000_000))
