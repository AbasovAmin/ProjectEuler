#Problem 53
#Check projecteuler

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def n_r(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))


count = 0

for n in range(1,101):
    for r in range(0, n//2 + 1):
        if n_r(n,r) > 1_000_000:
            if n == 2*r:
                count += 1
            else:
                count += 2
            
print(count)
