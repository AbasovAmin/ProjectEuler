#Problem 92
#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,
# 44 > 32 > 13 > 10 > 1 > 1
# 85 > 89 > 145 > 42 > 20 > 4 > 16 > 37 > 58 > 89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?

sqr = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}

memo = {1: 1, 89: 89}

count = 0

for i in range(1, 10_000_000):
    num = i
    while num != 1 and num != 89:
        new_num = 0
        for dig in str(num):
            new_num += sqr[dig]
            
        if new_num in memo:
            num = memo[new_num]
        else:
            num = new_num
        
    memo[i] = num
    if num == 89:
        count += 1

print(count)
        
