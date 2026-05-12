#Problem 0
#Among the first 365 thousand square numbers, what is the sum of all the odd squares?
sum_of_square_numbers = 0
number = 1

while number <= 365000:
    sum_of_square_numbers += number**2
    number += 2

print(sum_of_square_numbers)
        
