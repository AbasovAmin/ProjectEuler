#Problem 32

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
#exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 
#1 through 9  pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#the product should be less than 10**4 as if a*b >= 10_000 a, b should have 1,3 ; 2,2 ; 3,1 number of digits respectively which is not possible.
#the product should be greater than or equal to 10**3 since if a*b < 1000 a and b should have the number of digits more than or equal to our product which is not possible. 

product_list = set()

for a in range(1, 5000):
    for b in range(1, 10000//a):
        product = a*b
        list_ = list(map(int, (str(a) + str(b) + str(product))))
        list_.sort()
        if list_ == [1,2,3,4,5,6,7,8,9]:
            product_list.add(product)

print(sum(product for product in product_list))
