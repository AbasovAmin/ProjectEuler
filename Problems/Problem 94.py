#Problem 94
#It is easily proved that no equilateral triangle exists with integral length sides and integral
#area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion.

import math

def is_square(n):
    if n < 0: return False
    sqrt_n = math.isqrt(n)
    return sqrt_n**2 == n


SUM = 0
lst_ = []
lst__ = []

for a in range(3, 333333335, 2): #equal sides can only be odd
    s_a = 3*a*a
    p_a = 3*a
    h1 = s_a - 2*a - 1
    if is_square(h1):
        SUM += p_a + 1
    h2 = s_a + 2*a - 1
    if is_square(h2):
        SUM += p_a - 1

print(SUM)
