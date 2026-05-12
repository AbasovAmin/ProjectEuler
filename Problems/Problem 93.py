#Problem 93
#By using each of the digits from the set, {1,2,3,4}, exactly once, and making use of the
#four arithmetic operations (+,-,*,/) and brackets/parentheses, it is possible to form different positive integer targets.

#For example,

# 8 = (4*(1 + 3))/2

#Note that concatenations of the digits, like 12 + 34 , are not allowed.

#Using the set, {1,2,3,4}, it is possible to obtain thirty-one different target numbers of
#which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

#Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

from fractions import Fraction
from itertools import combinations, permutations, product

nums = {0,1,2,3,4,5,6,7,8,9}

operations = {'+','-','*','/'}

def operate(a,b,o):
    if a == 'bad' or b == 'bad':
        return 'bad'
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a*b
    else:
        if b != 0:
            return Fraction(a,b)
        else:
            return 'bad'

MAX_nums = {1,2,3,4}
MAX_num = 0

for a,b,c,d in combinations(nums, 4):
    num_set = set()
    for a,b,c,d in permutations({a,b,c,d}, 4):
        for o1, o2, o3 in product(operations, repeat = 3):
            num_set.add(operate(operate(a,b,o1),operate(c,d,o3),o2))
            num_set.add(operate(operate(operate(a,b,o1),c,o2),d,o3))
            num_set.add(operate(operate(a,operate(b,c,o2),o1),d,o3))
            num_set.add(operate(a,operate(b,operate(c,d,o3),o2),o1))
            num_set.add(operate(a,operate(operate(b,c,o2),d,o3),o1))

    i = 1
    count = 0
    while i in num_set:
        count += 1
        i += 1
    if count > MAX_num:
        MAX_num = count
        MAX_nums = {str(a),str(b),str(c),str(d)}

print(''.join(sorted(list(MAX_nums))))
