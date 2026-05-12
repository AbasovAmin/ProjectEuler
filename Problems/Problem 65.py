#Problem 65
#Check project euler

sequence = [2,1,2]
k = 2
for i in range(1,100):
    if i%3 == 0:
        sequence.append(2*k)
        k += 1
    else:
        sequence.append(1)

def nth_numerator(n):
    numerator = 1
    denominator = sequence[n-1]
    
    for i in range(n - 2, 0, -1):
        numerator, denominator = denominator, sequence[i]*denominator + numerator

    numerator, denominator = 2*denominator + numerator, denominator #at the end, 2 + n/d becomes (2d+n)/d
    return [numerator, denominator, sum(int(digit) for digit in str(numerator))]

print(nth_numerator(100))


        
    

