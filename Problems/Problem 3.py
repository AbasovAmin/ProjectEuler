#Problem 3
#What is the largest prime factor of the number 600851475143?

import IsPrime, sys

our_number = 600851475143
k = int(our_number**0.5+1)

if k % 2 == 0:
    k -= 1

while k > 0:
    if IsPrime.isprime(k) == True:
        if our_number % k == 0:
            print(k)
            sys.exit()
        else:
            k -= 2
    else:
        k -= 2
            
