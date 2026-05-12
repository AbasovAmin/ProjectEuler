#Problem 71
#By listing the set of reduced proper fractions n/d for n < d <= 1 000 000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

#We can find the largest fraction such that it is smaller than 3/7

from fractions import Fraction

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

our_frac = Fraction(3, 7)
max_frac = 0

for d in range(8, 1_000_001):
    n = d*3//7
    while gcd(n, d) != 1:
        n -= 1
        
    frac = Fraction(n, d)
    if frac > max_frac:
        max_frac = frac
        

print(max_frac)


#A better one without Fractions
'''
best_n = 0
best_d = 1

for d in range(2, 1_000_001):
    n = (3*d - 1) // 7  # guaranteed below 3/7
    if n * best_d > best_n * d:
        best_n, best_d = n, d

print(best_n, best_d)'''

