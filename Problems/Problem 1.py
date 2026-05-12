#Problem 1
#Find the sum of all the multiples of 3 or 5 below 1000

number = 1
sum_of_numbers = 0

while number < 1000:
    if number % 3 == 0:
        sum_of_numbers += number
        number += 1
    elif number % 5 == 0:
        sum_of_numbers += number
        number += 1
    else:
        number += 1

print(sum_of_numbers)
