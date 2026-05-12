#Problem 20
#Find the sum of the digits in the number 100!.

from DigitProduct import digitSum

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(sum(int(d) for d in str(factorial(100))))
