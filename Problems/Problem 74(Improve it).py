#Problem 74
#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#1!+4!+5!=1+24+120=145.

#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

#169→363601→1454→169
#871→45361→871
#872→45362→872
 
#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

#69→363600→1454→169→363601⁢(→1454)
#78→45360→871→45361⁢(→871)
#540→145⁢(→145)
 
#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?


factorial_l = [1,1,2,6,24,120,720,5040,40320,362880]

memo = {}
def sum_fac(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = sum(factorial_l[int(dig)] for dig in str(n))
    return memo[n]


def chain_length(n):
    terms = set([n])
    count = 1 #n itself
    while True:
        n = sum_fac(n)
        if n in terms:
            return count
        terms.add(n)
        count += 1

count = 0

for n in range(1, 1_000_001):
    if chain_length(n) == 60:
        count += 1

print(count)


        

