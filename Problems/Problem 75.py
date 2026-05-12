#Problem 75
#Given that L is the length of the wire, for how many values of L <= 1 500 000 can exactly one integer sided right angle triangle be formed?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A right triangle with integer sides is either primitive (gcd(a,b,c)=1) or a scaled
# version of a primitive one. Primitive triples are generated uniquely by Euclid’s
# formula:
#     a = m^2 - n^2,  b = 2mn,  c = m^2 + n^2
# with m > n ≥ 1, gcd(m,n)=1, and m,n of opposite parity(m,n is odd,even or even,odd). The perimeter of a primitive
# triple is:
#     p0 = 2*m*(m+n).
#
# Every non-primitive triple is just t*(a,b,c) for some integer t ≥ 1, with perimeter t*p0.
#
# Therefore, a perimeter N has as many right-triangle solutions as the number of
# primitive perimeters p0 that divide N. Each such divisor contributes exactly one
# triangle (the scaled version of its primitive parent).
#
# So when considering divisors of N, keep only those which are primitive perimeters.
# Non-primitive divisors (e.g. 36 = 3*12) are ignored because their primitive ancestor
# is already counted.
#
# Example: 120 has primitive divisors {12, 30, 40}. Thus f(120)=3.

import math

limit = 1500000
counts = [0]*(limit+1)
m = 2
while 2*m*(m+1) <= limit:         # smallest n is 1 so check p0 <= limit
    for n in range(1, m):
        if (m-n)%2==1 and math.gcd(m,n) == 1:
            p0 = 2*m*(m+n)
            if p0 > limit:
                break
            for k in range(p0, limit+1, p0):
                counts[k] += 1
    m += 1


count = 0

for L in range(12, 1_500_001, 2):
    if counts[L] == 1:
        count += 1

print(count)
    
