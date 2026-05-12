#Problem 46
#It was proposed by Christian Goldbach that every odd composite
#number can be written as the sum of a prime and twice a square.

#9 = 7 + 2 × 1^2
#15 = 7 + 2 × 2^2
#21 = 3 + 2 × 3^2
#25 = 7 + 2 × 3^2
#27 = 19 + 2 × 2^2
#33 = 31 + 2 × 1^2
 
#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


import sys

limit = 10000
is_prime = [False, False] + [True]*(limit-2)  # 0 and 1 are not prime

for number in range(2, int(limit**0.5)+1):
    
    if is_prime[number]:
        
        for multiple in range(number*2, limit, number):
            
            is_prime[multiple] = False

# Collect odd composites
composite_odd_numbers = [i for i, prime in enumerate(is_prime) if not prime and i%2 == 1 and i != 1] #remove 1 and even numbers

# Collect primes
prime_numbers = [i for i, prime in enumerate(is_prime) if prime and i != 2]  #remove 2


for i in range(0,len(composite_odd_numbers)):
    comp_num = composite_odd_numbers[i]
    for k in prime_numbers:
        if k > comp_num:
            print(comp_num)
            sys.exit()
        the_test = ((comp_num - k)//2)**0.5
        if int(the_test) == the_test:
            break


