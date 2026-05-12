#Problem 64
#Check Project Euler

import math

def cont_frac_sqrt(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return (a0, []) 

    m = 0
    d = 1
    a = a0

    period = []

    while True:
        m = d * a - m
        d = (n - m*m) // d
        a = (a0 + m) // d
        period.append(a)

        if a == 2*a0:  
            break

    return (a0, period)

count = 0
for n in range(1,10001):
    if len(cont_frac_sqrt(n)[1]) % 2 == 1:
        count += 1

print(count)
