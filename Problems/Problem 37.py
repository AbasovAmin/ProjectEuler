#Problem 37
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 
#3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#The limit for a truncatable prime number would be 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

LIMIT = 1000000

is_prime = [False, False] + [True] * (LIMIT - 2)
for i in range(2, int(LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, LIMIT, i):
            is_prime[j] = False

prime_set = {i for i, val in enumerate(is_prime) if val}


def is_truncatable(p):
    if p < 10:
        return False
    s = str(p)
    
    #Left
    for i in range(len(s)):
        if int(s[i:]) not in prime_set:
            return False
    
    #Right
    for i in range(1, len(s)+1):
        if int(s[:i]) not in prime_set:
            return False
    
    return True

truncatable_primes = []

for p in sorted(prime_set):   # ascending order
    if is_truncatable(p):
        truncatable_primes.append(p)
        if len(truncatable_primes) == 11:
            break

print(truncatable_primes)
print(sum(truncatable_primes))


