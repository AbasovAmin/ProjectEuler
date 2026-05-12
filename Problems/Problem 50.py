#Problem 50
#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13.
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

limit = 1000000
is_prime = [False, False] + [True] * (limit - 2)

# Faster sieve
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit, i):
            is_prime[j] = False

prime_numbers = [i for i, pr in enumerate(is_prime) if pr]
prime_numbers_set = set(prime_numbers)



def func():
    max_len = 0
    max_sum = 0

    for right in range(len(prime_numbers)):
        left = 0
        current_sum = sum(prime_numbers[left:(right + 1)])
        
        while current_sum > 1000000:
            current_sum -= prime_numbers[left]
            left += 1
            if left == 500:  #A chain starting at 500th prime cannot be a candidate for maximum length since their sum would need to exceed 1000000 to have length of at least 500
                return max_len, max_sum 
        
        while current_sum not in prime_numbers_set:
            if right - left + 1 < max_len:
                break
            current_sum -= prime_numbers[left]
            left += 1

        length = right - left + 1

        if length > max_len:
            max_sum = current_sum
            max_len = length
            print("New best:", max_len, max_sum, "left", left, "right", right)
        
print(func())


#Better solution
'''
limit = 1_000_000
is_prime = [False, False] + [True] * (limit - 2)
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit, i):
            is_prime[j] = False

prime_numbers = [i for i, pr in enumerate(is_prime) if pr]
prime_set = set(prime_numbers)

max_len = 0
max_sum = 0

left = 0
current_sum = 0

for right in range(len(prime_numbers)):
    # expand window to include prime_numbers[right]
    current_sum += prime_numbers[right]

    # shrink from the left while sum exceeds the limit
    while current_sum > limit and left <= right:
        current_sum -= prime_numbers[left]
        left += 1

    # Now try to tighten left to see if we can find a prime sum for this right,
    # but only while the window length is still potentially better than max_len.
    # NOTE: this permanently advances left (that's intended for this algorithm).
    while left <= right and (right - left + 1) > max_len:
        if current_sum in prime_set:
            # found a prime sum longer than previous best
            max_len = right - left + 1
            max_sum = current_sum
            # once found, we could break this tightening loop if we want,
            # but we continue trying to shrink to possibly find a different prime
            # with the same right but shorter length (not necessary for correctness).
            break
        # otherwise shrink from left and keep searching
        current_sum -= prime_numbers[left]
        left += 1

# final result
print(max_len)
print(max_sum)'''








    
