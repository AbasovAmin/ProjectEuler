#Problem 98
#By replacing each of the letters in the word CARE with 1, 2, 9, 6 and  respectively, we form a square number: 1296 = 36^2.
#What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square
#number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes
#are not permitted, neither may a different letter have the same digital value as another letter.

#Using words.txt, a 16K text file containing nearly
#two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

#What is the largest square number formed by any member of such a pair?
#NOTE: All anagrams formed must be contained in the given text file.

from itertools import combinations
from math import isqrt

words_file = open('words.txt').read()

#First we got to find all anagram duos
words = [i.strip('"') for i in words_file.split(',')]

dct_for_anagrams = {}

for word in words:
    sd_word = ''.join(sorted(word))
    if sd_word in dct_for_anagrams:
        dct_for_anagrams[sd_word].add(word)
    else:
        dct_for_anagrams[sd_word] = set([word])
        
all_duos = []

for sd_word in dct_for_anagrams:
    set_of_w = dct_for_anagrams[sd_word]
    if len(set_of_w) != 1:
        for duo in combinations(set_of_w, 2):
            all_duos.append(duo)

#Second let us find every anagram square number duos till the longest word we have in our duos
longest_word_length = max((len(duo[0]) for duo in all_duos))
all_squares = []
upper_bound = isqrt(10**(longest_word_length))
n = 4

while upper_bound > n:
    all_squares.append(str(n*n))
    n += 1

dct_for_anagram_squares = {}

for square in all_squares:
    sd_num = ''.join(sorted(square))
    if sd_num in dct_for_anagram_squares:
        dct_for_anagram_squares[sd_num].add(square)
    else:
        dct_for_anagram_squares[sd_num] = set([square])

all_duo_squares = []

for sd_num in dct_for_anagram_squares:
    set_of_n = dct_for_anagram_squares[sd_num]
    if len(set_of_n) != 1:
        for duo in combinations(set_of_n, 2):
            all_duo_squares.append(duo)
            

squares_by_length = {}
for sq_duo in all_duo_squares:
    L = len(sq_duo[0])
    if L not in squares_by_length:
        squares_by_length[L] = []
    squares_by_length[L].append(sq_duo)

#Third let us compare these two lists of duos
def is_square_anagram(duo):
    word1 = duo[0]
    word2 = duo[1]

    length = len(word1)

    sq_list = squares_by_length.get(length, [])

    MAX = 0

    for sq_duo in sq_list:
        num1 = sq_duo[0]
        num2 = sq_duo[1]
        correspondence = set(zip(word1, num1))
        if len(correspondence) == len(set(word1)) and len(correspondence) == len(set(num1)):
            copy_word2 = word2
            for each in correspondence:
                copy_word2 = copy_word2.replace(each[0], each[1])
                
            if copy_word2 == num2:
                num = max(int(num1), int(num2))
                if num > MAX:
                    MAX = num
    return MAX

full_MAX = 0

for duo in all_duos:
    full_num = is_square_anagram(duo)
    if full_num > full_MAX:
        full_MAX = full_num

print(full_MAX)
    
