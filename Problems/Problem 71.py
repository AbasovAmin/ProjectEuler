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
