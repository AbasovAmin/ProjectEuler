#Problem 27
#Too long to write. Just check projecteuler

from IsPrime import isprime

#First we need to find the possible values of b which are prime numbers between 1 and 1000 since n^2 + an + b should be prime when n = 0

limit = 1000
is_prime = [False, False] + [True]*(limit-2)  # 0 and 1 are not prime

for number in range(2, int(limit**0.5)+1):
    
    if is_prime[number]:
        
        for multiple in range(number*2, limit, number):
            
            is_prime[multiple] = False

# Collect primes
prime_numbers = [i for i, prime in enumerate(is_prime) if prime]



longest_cycle = 0
product = 0

for a in range(-999,1000):
    for b in prime_numbers:
        cycle  = 0
        primeness = True
        n = 0
        
        while primeness:
            if isprime(n*n + a*n + b):
                cycle += 1
                n += 1
                continue
            else:
                primeness = False

        if longest_cycle < cycle:
            longest_cycle = cycle
            product = a*b
            
print(product)
