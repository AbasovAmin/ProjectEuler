#Problem 60
#The primes 3, 7, 109, and 673, are quite remarkable.
#By taking any two primes and concatenating them in any order the result will always be prime.
#For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

limit = 10000
sieve = [False,False] + [True]*(limit - 2)

for i in range(limit):
    if sieve[i] == True:
        for k in range(i*i, limit, i):
            sieve[k] = False

prime_list = [i for i, prime in enumerate(sieve) if prime and i != 2]


def isprime(k):
    if k <= 1:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
        
    return True


memo = {}
def conc_primes(a, b):
    if (a, b) in memo:
        return memo[(a, b)]
    if (b, a) in memo:
        return memo[(b, a)]
    result = isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a)))
    memo[(a, b)] = result
    return result


pairs = []

for i, prime in enumerate(prime_list):
    for prime2 in prime_list[i+1:]:
        if conc_primes(prime, prime2):
            pairs.append((prime, prime2))

triples = []

for prime, prime2 in pairs:
    for prime3 in prime_list:
        if prime3 > max(prime, prime2) and conc_primes(prime, prime3) and conc_primes(prime2, prime3):
            triples.append((prime, prime2, prime3))

quadruples = []

for t in triples:
    for prime4 in prime_list:
        if prime4 > max(t) and all(conc_primes(prime4, prime) for prime in t):
            quadruples.append(t + (prime4,))

quintuples = []

for q in quadruples:
    for prime5 in prime_list:
        if prime5 > max(q) and all(conc_primes(prime5, prime) for prime in q):
            quintuples.append(q + (prime5,))

for quint in quintuples:
    print(quint, sum(quint))
