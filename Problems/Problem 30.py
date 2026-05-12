#Problem 30
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#It is easy to see that since 9^5 * n < 10^(n-1) starts from n = 7 so we only have to check till 6 digit numbers.
#Our upper limit is 354294 since 6 * 9^5 = 354294.

list_of_numbers = []

for n in range(10, 354_295):
    if n == sum(int(digit)**5 for digit in str(n)):
        list_of_numbers.append(n)

print(list_of_numbers)  #To check it out
print(sum(n for n in list_of_numbers))
