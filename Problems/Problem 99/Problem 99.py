#Problem 99
#Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2048 < 2187.

#However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

#Using base_exp.txt, a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

#NOTE: The first two lines in the file represent the numbers in the example given above.

from math import log10

base_exp_file = open('base_exp.txt').read()

nums = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in base_exp_file.split('\n')]

#As we know, for two positive integers a and b, a > b iff log_c(a) > log_c(b) for any base c > 1.(For this problem we will use base 10 but for extra accuracy one can use e or smaller bases)
#Additionally, log_c(a^b) = b*log_c(a) shall be used.

MAX = 0
line = 0

for i in range(len(nums)):
    big_num = nums[i][1] * log10(nums[i][0])
    if big_num > MAX:
        MAX = big_num
        line = i + 1

print(line)
