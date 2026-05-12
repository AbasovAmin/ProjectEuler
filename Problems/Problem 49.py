#Problem 49
#The arithmetic sequence, 1487,4817,8147, in which each of the terms increases by 3330,
#is unusual in two ways:
#(i) each of the three terms are prime, and
#(ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?


limit = 10000
is_prime = [False, False] + [True] * (limit - 2)

# Faster sieve
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit, i):
            is_prime[j] = False

prime_numbers = [i for i, prime in enumerate(is_prime) if prime and i > 1000]  
prime_numbers_set = set(prime_numbers)


def check_perm():
    for p in prime_numbers:
        if p == 1487:
            continue
        perm = sorted(str(p))
        for k in range(1,4500):
            second = p+k
            third = p+2*k
            if second in prime_numbers_set and third in prime_numbers_set and perm == sorted(str(second)) and perm == sorted(str(third)) :
                return str(p)+str(second)+str(third)

print(check_perm())
        
        
            
        
