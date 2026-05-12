#Problem 33
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 
#49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

numerator = 1
denominator = 1

for a in range(11,100):
    for b in range(a+1,100):
        if a%10 != 0 and b%10 != 0:
            list_a = [a//10, a%10]
            list_b = [b//10, b%10]
            for i in list_a:
                if i in list_b:
                    list_a.remove(i)
                    list_b.remove(i)
                    new_a = list_a[0]
                    new_b = list_b[0]
                    if a*new_b == b*new_a:
                        numerator *= a
                        denominator *= b

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(denominator//gcd(numerator, denominator))

        
        
