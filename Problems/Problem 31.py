#Problem 31
#In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#It is possible to make £2 in the following way:

#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

#How many different ways can £2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

ways = [0] * (target + 1)
ways[0] = 1

for c in coins:
    for i in range(c, target + 1):
        ways[i] += ways[i - c]

print(ways[target])



#My favorite brute-force
'''
count = 0 
Goal = 200
for two_hundred in range(0, Goal + 1, 200):
    for hundred in range(0, Goal - two_hundred + 1, 100):
        for fifty in range(0, Goal - two_hundred - hundred + 1, 50):
            for twenty in range(0, Goal - two_hundred - hundred - fifty + 1, 20):
                for ten in range(0, Goal - two_hundred - hundred - fifty - twenty + 1, 10):
                    for five in range(0, Goal - two_hundred - hundred - fifty - twenty - ten + 1, 5):
                        for two in range(0, Goal - two_hundred - hundred - fifty - twenty - ten - five + 1, 2):
                            count += 1

print(count)'''


