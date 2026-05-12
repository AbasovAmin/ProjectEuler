#Problem 9
#There exists exactly one Pythagorean triplet
#for which a+b+c = 1000.Find the product abc.

import sys

for i in range(1,1000):
    for k in range(1,1000-i):
        c = 1000 - k - i
        if i**2 + k**2 == c**2:
            print(str(i) + ', ' + str(k) + ', ' + str(c))
            print(i*k*c)
            sys.exit()

