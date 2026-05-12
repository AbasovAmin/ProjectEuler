#Problem 2
#By considering the terms in the Fibonacci sequence whose
#values do not exceed four million, find the sum of the even-valued terms.

f1 = 1
f2 = 2
new_number_1 = 2
new_number_2 = 1
sum_of_numbers = 0

while new_number_1 < 4000000:
    if new_number_1 % 2 == 0:
        sum_of_numbers += new_number_1
        new_number_1 , new_number_2 = new_number_1 + new_number_2 , new_number_1
    else:
       new_number_1 , new_number_2 = new_number_1 + new_number_2 , new_number_1

print(sum_of_numbers)
