#Problem 42
#The nth term of the sequence of triangle numbers is given by, t_n = ⁢n(n+1)/2; so the first ten triangle numbers are:
#1,3,6,10,15,21,28,36,45,55,…

#By converting each letter in a word to a number corresponding to its alphabetical position
#and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
#If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?



words_file = open('words.txt').read()


set_of_names = {word.strip('"') for word in words_file.split(',')}

Alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

set_of_tri_nums = {n*(n+1)//2 for n in range(1,len(max(set_of_names, key = len))*2)}   #longest word in this file is 14 letters so our limit for triangle numbers would be 26*14 = 26*28/2 < 27*28/2

count = 0

for name in set_of_names:
    sum_ = 0
    
    for symbol in name:
        sum_ += Alphabet.find(symbol)
        
    if sum_ in set_of_tri_nums:
        count += 1

print(count)
    
