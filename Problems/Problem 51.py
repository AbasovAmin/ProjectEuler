#Problem 51
#By replacing the 1st digit of the 2-digit number *3,
#it turns out that six of the nine possible values:
#13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit,
#this 5-digit number is the first example having seven primes among
#the ten generated numbers, yielding the family: 56003, 56113, 56333,
#56443, 56663, 56773, and 56993. Consequently 56003, being the first
#member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number
#(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sieve
LIMIT = 1000000
is_prime = [False,False] + [True]*(LIMIT - 2) #0 and 1 are not primes

for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        for k in range(i*i, LIMIT, i):
            is_prime[k] = False

prime_numbers = [i for i, prime in enumerate(is_prime) if prime and i > 10]
prime_set = set(prime_numbers)


list_of_digits = ['0','1','2','3','4','5','6','7','8','9']

def func():
    for prime in prime_numbers:
        str_prime = str(prime)
        set_of_digits = set(str_prime)
        
        for digit in set_of_digits:
            count = 0
            for num in list_of_digits:
                str_prime_k = str_prime.replace(digit, num)
                
                if str_prime_k[0] == '0':
                    continue
                
                if int(str_prime_k) in prime_set:
                    count += 1
            
            if count == 8:
                return prime
            
print(func())
    
    
    






        
