#Problem 41
#We shall say that an 𝑛-digit number is pandigital if it
#makes use of all the digits 1 to 𝑛 exactly once.
#For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest 𝑛-digit pandigital prime that exists?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#n can not be 10, 9, or 8 digital as the sum of the digits would be divisible by 3. So we will start checking primes from permutations of '1234567'.

LIMIT = 7654322

is_prime = [False, False] + [True] * (LIMIT - 2)
for i in range(2, int(LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, LIMIT, i):
            is_prime[j] = False

prime_set = {i for i, val in enumerate(is_prime) if val}

def permutation(list_):
    if len(list_) <= 1:
        return [list_]
    
    else:
        perm_list = []
        
        for i in range(len(list_)):
            
            list_without_i = list_[:i] + list_[i+1:]
            
            for k in permutation(list_without_i):
                perm_list.append([list_[i]] + k)
                
        return perm_list

all_perm = permutation(['1','2','3','4','5','6','7'])
all_perm.sort(reverse = True)

for perm in all_perm:
    num = int(''.join(perm))
    if num in prime_set:
        print(num)
        break



#Better Solution
'''from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

for p in permutations('7654321'):  # already descending
    num = int(''.join(p))
    if is_prime(num):
        print(num)
        break'''
