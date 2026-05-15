#Problem 10
#Find the sum of all the primes below two million.

#An ancient method of finding prime numbers
limit = 2_000_000
sieve = [True] * limit
sieve[0] = sieve[1] = False

p = 2
while p * p < limit:
    if sieve[p]:
        for multiple in range(p * p, limit, p):
            sieve[multiple] = False
    p += 1

print(sum(i for i in range(limit) if sieve[i]))
