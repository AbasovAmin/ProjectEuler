#Problem 78
#Let 𝑝⁡(𝑛) represent the number of different ways in which 𝑛 coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so 𝑝⁡(5) =7.

#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O
#Find the least value of 𝑛 for which 𝑝⁡(𝑛) is divisible by one million.



#Check out this link https://en.wikipedia.org/wiki/Partition_function_(number_theory)
def partition_mod(limit=1_000_000):
    dp = [1]  # p(0)=1

    for n in range(1, 200000):
        total = 0
        k = 1
        while True:
            g1 = k*(3*k - 1)//2
            if g1 > n:
                break
            sign = 1 if (k % 2) != 0 else -1
            total += sign * dp[n - g1]

            g2 = k*(3*k + 1)//2
            if g2 <= n:
                total += sign * dp[n - g2]

            k += 1

        total %= limit
        dp.append(total)
        if total == 0:
            return n

print(partition_mod())
