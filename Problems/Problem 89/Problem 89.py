#Problem 89
#Too long, check projecteuler

def roman_to_number(k):
    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    list_ = [numerals[symbol] for symbol in k]
    number = 0
    for i in range(len(list_)):
        if i == len(list_) - 1:
            return number + list_[i]
        if list_[i] < list_[i+1]:
            number -= list_[i]
        else:
            number += list_[i]
    return number

def number_to_roman(num):
    roman_map = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]
    
    result = ""
    for roman, value in roman_map:
        count = num // value
        result += roman * count
        num -= value * count
    return result

roman_file = open('C:\\Users\\PC\\Desktop\\Olympiad\\Python\\Project Euler\\Problem 89\\roman.txt').read()

count = 0

for roman in roman_file.split('\n'):
    count += len(roman) - len(number_to_roman(roman_to_number(roman)))

print(count)


