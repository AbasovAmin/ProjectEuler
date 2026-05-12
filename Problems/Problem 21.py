#Problem 21
#Let d(n) be defined as the sum of proper divisors of n(numbers less than n
#which divide evenly into n).If d(a) = b and d(b) = a, where a != b, then
#a and b are an amicable pair and each of a and b are called amicable numbers.
#Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    sum_ = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                sum_ += i
            else:
                sum_ += i + n//i
    return sum_ - n
        

amicable_sum = 0

for a in range(1,10000):
    if d(d(a)) == a and d(a) < 10000 and d(a) != a:
        amicable_sum += a

print(amicable_sum)        
