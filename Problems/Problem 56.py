#Problem 56
#A googol (10^100) is a massive number: one followed by one-hundred zeros;
#100^100 is almost unimaginably large: one followed by two-hundred zeros.
#Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, a^b, where a,b <100, what is the maximum digital sum?


max_ = 0

for a in range(1,100):
    for b in range(1,100):
        power_sum = sum(int(d) for d in str(a**b))
        if power_sum > max_:
            max_ = power_sum
print(max_)
