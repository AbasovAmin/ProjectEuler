#Problem 47
#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5.
 
#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2^2 × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
 
#Find the first four consecutive integers to have four
#distinct prime factors each. What is the first of these numbers?

limit = 100000
is_prime = [False, False] + [True]*(limit-2)  # 0 and 1 are not prime

for number in range(2, int(limit**0.5)+1):
    
    if is_prime[number]:
        
        for multiple in range(number*number, limit, number):
            
            is_prime[multiple] = False

# Collect primes
prime_numbers = [i for i, prime in enumerate(is_prime) if prime]

#Set to find primes easier
prime_numbers_set = set(prime_numbers)


def prime_factors(k):
    if k == 1:
        return 0
    if k in prime_numbers_set:
        return 1

    count = 0
    for prime in prime_numbers:
        if prime > k//2:
            return count
        if k % prime == 0:
            count += 1


finished = False
k = 420 #First number with 4 prime factors
while not finished:
    for i in range(k, k+4):
        
        if prime_factors(i) == 4:
            if i == k + 3:
                print(k)
                finished = True
            else:    
                continue
        else:
            k = i + 1
            break






    
    
