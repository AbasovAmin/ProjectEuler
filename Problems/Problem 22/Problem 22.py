name_file = open('22_names.txt')

Alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

list_of_names = list(map(str, name_file.read().split(',')))

for i in range(len(list_of_names)):
    list_of_names[i] = list_of_names[i].strip('"')

list_of_names.sort()

sum_ = 0

for i in range(len(list_of_names)):
    letter_sum = 0
    for letter in list_of_names[i]:
        letter_sum += Alphabet.index(letter)
    sum_ += letter_sum * (i+1)

print(sum_)
        
    
    
