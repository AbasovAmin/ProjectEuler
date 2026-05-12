#Problem 7
#What is the 10001st prime number?

import IsPrime, sys

prime_number_n = 3
k = 2

while k < 10001:
    prime_number_n += 2
    if IsPrime.isprime(prime_number_n):
        k += 1

print(prime_number_n)
    
