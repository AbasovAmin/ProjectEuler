#Problem 80
#It is well known that if the square root of a natural number is not an integer, then it is irrational.
#The decimal expansion of such square roots is infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880⋯, and the digital sum of the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.


nums = [num for num in range(2,100) if (int(num**0.5))**2 != num]


def sqrt_dig_sum(n, digits=100):
    s = str(n)
    if len(s) % 2 == 1:
        s = "0" + s
        
    pairs = [int(s[i:i+2]) for i in range(0, len(s), 2)]

    R = 0
    a = 0

    for p in pairs:
        R = R*100 + p
        x = 0
        for d in range(10):
            if (20*a + d)*d <= R:
                x = d
            else:
                break

        R -= (20*a + x)*x
        a = a*10 + x

    for _ in range(digits - 1):
        R = R*100
        x = 0
        for d in range(10):
            if (20*a + d)*d <= R:
                x = d
            else:
                break
            
        R -= (20*a + x)*x
        a = a*10 + x
    
        
    return sum(int(dig) for dig in str(a))

print(sum(sqrt_dig_sum(num) for num in nums))
    

