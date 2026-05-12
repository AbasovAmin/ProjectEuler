#Problem 73
#How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12 000?

import math

count = 0

for d in range(2, 12001):
    for n in range(math.ceil(d/3), math.floor(d/2) + 1):
        if math.gcd(d, n) == 1:
            count += 1
            
print(count - 2) #We have gcd(1,3) and gcd(1,2) which should be excluded

