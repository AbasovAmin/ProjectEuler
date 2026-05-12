#Problem 95
#The proper divisors of a number are all the divisors excluding the number itself.
#For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
#forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

# 12496 ---> 14288 ---> 15472 ---> 14536 ---> 14264 ---> (12496 ---> ....)

#Since this chain returns to its starting point, it is called an amicable chain.

#Find the smallest member of the longest amicable chain with no element exceeding one million.

limit = 1000000
is_prime = [False, False] + [True] * (limit - 2)

# Faster sieve
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit, i):
            is_prime[j] = False

prime_numbers = [i for i, pr in enumerate(is_prime) if pr]
memo = set(prime_numbers)

sums = [1] * limit
for i in range(2, limit // 2):
    for j in range(i * 2, limit, i):
        sums[j] += i

longest_chain = 1
best_num = 0

for i in range(6, 1_000_000):
    if i in memo:
        continue
    memo.add(i)
    set_ = set()
    new_num = sums[i]
    chain = 1

    while new_num != i and new_num < 1_000_000 and new_num not in memo and new_num not in set_:
        set_.add(new_num)
        new_num = sums[new_num]
        chain += 1

    if new_num > 1_000_000 or (new_num in memo and new_num != i) or new_num in set_:
        continue
    memo = memo | set_
    if chain > longest_chain:
        best_num = i
        longest_chain = chain

print(best_num)
    
