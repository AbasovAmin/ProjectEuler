#Problem 52
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2⁢x, 3x, 4x, 5⁢x, and 6⁢x, contain the same digits.

def func():
    n = 1
    while True:
        s = sorted(str(n))

        # If 6n has more digits, jump to next digit range immediately
        if len(str(6*n)) != len(str(n)):
            n = 10 ** len(str(n))
            continue

        if all(sorted(str(k*n)) == s for k in range(2, 7)):
            return n

        n += 1


print(func())
        
