#Problem 5
#What is the smallest positive number that is evenly
#divisible by all of the numbers from 1 to 20?

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

result = 1

for i in range(1, 21):
    result = lcm(result, i)

print(result)
         
            
