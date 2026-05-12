#Problem 43
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
#but it also has a rather interesting sub-string divisibility property.

#Let d_1 be the 1st digit, 𝑑2 be the 2nd digit, and so on. In this way, we note the following:

#d_2 d_3 d_4 = 406 is divisible by 2
#d_3 d_4 d_5 = 063 is divisible by 3
#d_4 d_5 d_6 = 635 is divisible by 5
#d_5 d_6 d_7 = 357 is divisible by 7
#d_6 d_7 d_8 = 572 is divisible by 11
#d_7 d_8 d_9 = 728 is divisible by 13
#d_8 d_9 d_10 = 289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.


from itertools import permutations

list_primes = [2, 3, 5, 7, 11, 13, 17]

sum_ = 0

for perm in permutations('9876543210'):
    num_str = ''.join(perm)
    pieces = []
    for i in range(1,8):
        pieces.append(int(number[i:(i+3)]))
    for i in range(0,7):
        if (pieces[i])%(list_primes[i]) == 0:
            if i == 6:
                sum_ += int(number)
            else:
                continue
        else:
            break

print(sum_)


#Cleaner version
'''
from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
total = 0

for p in permutations('9876543210'):
    num_str = ''.join(p)
    for i, prime in enumerate(primes):
        if int(num_str[i+1:i+4]) % prime != 0:
            break
    else:
        total += int(num_str)

print(total)'''
