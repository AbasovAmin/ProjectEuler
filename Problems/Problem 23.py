#Problem 23
#A number n is called deficient if the sum of its proper divisors is less than n
#and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1+2+3+4+6=16 , the smallest number
#that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
#it can be shown that all integers greater than 28123 can be written as the sum
#of two abundant numbers. However, this upper limit cannot be reduced any
#further by analysis even though it is known that the greatest number that
#cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be
#written as the sum of two abundant numbers.

def d(n):
    sum_ = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                sum_ += i
            else:
                sum_ += i + n//i
    return sum_ - n


#Since dictionary finds elements much faster than lists
abundant_n_list = {}

for n in range(1,28214):
    if d(n) > n:
        abundant_n_list[n] = None

numbers = []

for i in range(1,28214):
    for k in abundant_n_list:
        if k>i:
            numbers.append(i)
            break
        else:
            if i-k in abundant_n_list:
                break

print(sum(numbers))
        



