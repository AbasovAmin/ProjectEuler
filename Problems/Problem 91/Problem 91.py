#Problem 91
#The points P(x_1,y_1) and Q(x_2,y_2) are plotted at integer co-ordinates
#and are joined to the origin, O(0,0), to form OPQ.

#There are exactly fourteen triangles containing a right angle that can be formed
#when each co-ordinate lies between 0 and 2 inclusive; that is, 0 <= x_1, y_1, x_2, y_2 <= 2.

#Given that 0 <= x_1, y_1, x_2, y_2 <= 50, how many right triangles can be formed?

from math import gcd

S1 = 50*50 + 50*50
S2 = 50*50

S3 = 0

#Calculation for S3
for x in range(1, 51):
    for y in range(1, 51):
        #go along the line perpendicular to OA
        new_x = x
        new_y = y
        g = gcd(x,y)
        delta_x, delta_y = y // g, -x // g
        count = 0

        #Bringing the line to the start
        while new_x >= 0 and new_y <= 50:
            new_x -= delta_x
            new_y -= delta_y

        while new_x <= 50 and new_y >= 0:
            new_x += delta_x
            new_y += delta_y
            count += 1

        S3 += count - 2 #Removing the point itself and extra point at the end

print(S1 + S2 + S3)
        
