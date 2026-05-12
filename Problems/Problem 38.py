#Problem 38
#What is the largest 1 to 9 pandigital 9-digit number that can be
#formed as the concatenated product of an integer with (1,2,...,n) where n>1?

#--------------------------------------------------------------------------------------------

#The biggest generator for a pandigital
#9 digit number via concatenated product can have at most 4-digits.

def create_pandigital(k):
    pand = str(k)
    n = 2
    while len(pand) < 9:
        pand += str(n*k)
        n += 1

    if len(pand) == 9 and set(pand) == set('123456789'):
        return int(pand)

max_ = 0

for i in range(1, 10000):
    s = str(i)
    if '0' in s or len(set(s)) != len(s):
        continue
    pand = create_pandigital(i)
    if pand and pand >= max_:
        max_ = pand

print(max_)
