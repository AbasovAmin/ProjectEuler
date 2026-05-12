#Problem 34

#145 is a curious number, as 1! + 4! + 5! = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# (9!)*8 < 2903040 < 10^7 so we only have to search until the seven digit number (9!)*7 = 2540160


list_facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

sum_ = 0

for i in range(10,2540160):
    f_sum = sum(list_facts[int(digit)] for digit in str(i))
    if f_sum == i:
        sum_ += i

print(sum_)
