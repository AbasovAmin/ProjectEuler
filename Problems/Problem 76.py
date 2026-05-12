#Problem 76
#It is possible to write five as a sum in exactly six different ways:

#4+1
#3+2
#3+1+1
#2+2+1
#2+1+1+1
#1+1+1+1+1
 
#How many different ways can one hundred be written as a sum of at least two positive integers?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ways(N):
    ways = [0] * (N + 1)
    ways[0] = 1

    for num in range(1, N+1):
        for i in range(num, N + 1):
            ways[i] += ways[i - num]

    return ways[N] - 1

print(ways(100))
