#Problem 77
#What is the first value which can be written as the sum of primes in over five thousand different ways?


Limit = 10000
sieve = [False, False] + [True]*(Limit - 2)
for i in range(2, Limit):
    if sieve[i] == True:
        for k in range(i*i, Limit, i):
            sieve[k] = False

prime_list = [i for i, prime in enumerate(sieve) if prime]


def prime_ways(N):
    ways = [0] * (N + 1)
    ways[0] = 1

    for prime in prime_list:
        if prime >= N:
            break
        for i in range(prime, N + 1):
            ways[i] += ways[i - prime]
    return ways[N]


def first():
    n = 1
    while True:
        if prime_ways(n) < 5000:
            n += 1
        else:
            return n

print(first())
