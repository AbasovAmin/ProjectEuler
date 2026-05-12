#Problem 58
#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
'''
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
'''
#It is interesting to note that the odd squares lie along the bottom right diagonal,
#but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈62%.


#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
#If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

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

def func():
    count_prime = 3
    count_total = 5
    n = 9
    sum_ = 4

    while True:
        count_total += 4
        for _ in range(4):
            n += sum_
            if isprime(n):
                count_prime += 1
        if count_prime/count_total < 0.1:
            return sum_ + 1
        sum_ += 2

print(func())
    
