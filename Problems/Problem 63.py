#Problem 63
#The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#We have to find a limit for the numbers a, n in a^n. 1 <= a <= 9 is obvious. For n, let us check 9^n > 10^(n-1). From taking log10 on both sides and some more simple operations we get n can not be greater than 21.

count = 0

for a in range(1,10):
    for n in range(1,22):
        if len(str(a**n)) == n:
            count += 1

print(count)
