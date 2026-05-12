#Problem 87
#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
#In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#28 = 2^2 + 2^3 + 2^4
#33 = 3^2 + 2^3 + 2^4
#49 = 5^2 + 2^3 + 2^4
#47 = 2^2 + 3^3 + 2^4

#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#We do not need to check all numbers till 50 million. We can just go through the combinations of primes till they pass 50 million.

import math

def solve(LIMIT = 50_000_000):
    limit = int(math.sqrt(LIMIT))
    is_prime = [False, False] + [True] * (limit - 2)

    # Faster sieve
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False

    prime_numbers = [i for i, pr in enumerate(is_prime) if pr]

    num_lst = set()

    for i in prime_numbers: # second power
        i_sqr = i*i
        for j in prime_numbers: # third power
            j_cub = j*j*j
            if i_sqr + j_cub >= LIMIT:
                break
            for k in prime_numbers: # fourth power
                num = i_sqr + j_cub + k**4
                if num >= LIMIT:
                    break
                num_lst.add(num)

    print(len(num_lst))

if __name__ == "__main__":
    solve()

    
