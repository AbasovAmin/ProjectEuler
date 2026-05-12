#Problem 4
#Find the largest palindrome made from the product of two 3-digit numbers.

import IsPalindrome, sys

b = 999
c = 999
largest_palindrome = 0

while c > 0:
    if largest_palindrome < b*c:
        if IsPalindrome.isPalindrome(b*c):
            largest_palindrome = b*c
            if b == 0:
                c -= 1
                b = 999
            else:
                b -= 1
        else:
            if b == 0:
                c -= 1
                b = 999
            else:
                b -= 1
    else:
        if b == 0:
            c -= 1
            b = 999
        else:
            b -= 1

print(largest_palindrome)
    
