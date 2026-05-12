#Problem 35
#The number 197 is called a circular prime because all rotations of the digits:
#197,971, and 719 are themselves prime.

#How many circular primes are there below one million?

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

def checkcircular(k):
    if not isprime(k):
        return False
    
    list_ = list(digit for digit in str(k))
    
    for _ in range(len(list_)):
        
        number = list_[0]
        list_.remove(number)
        list_.append(number)
        new_k = int(''.join(list_))
        
        if not isprime(new_k):
            return False
    return True

count = 1 #counting 2

for i in range(3, 1000000, 2):
    if checkcircular(i):
        count += 1

print(count)
