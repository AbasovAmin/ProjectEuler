#Problem 57
#Check projecteuler

numerator = 3
denominator = 2

count = 0

for _ in range(999):
    numerator, denominator = numerator + 2*denominator, numerator + denominator
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print(count)
