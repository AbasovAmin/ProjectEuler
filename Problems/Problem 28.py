#Problem 28
#Starting with the number 1 and moving to the right in a
#clockwise direction a 5 by 5 spiral is formed as follows:
'''
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''

#It can be verified that the sum of the numbers on the diagonals is 
#101. What is the sum of the numbers on the diagonals in a 
#1001 by 1001 spiral formed in the same way?

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# For ring n (side length = 2n−1), the four diagonal values are:
#   (2n−1)^2 − k*(2n−2), for k = 0..3
# Summing these gives: 4*(2n−1)^2 − 6*(2n−2)

def ring_sum(n):
    if n == 1:
        return 1
    else:
        return 4*((2*n-1)**2) - 6*((2*n-1) - 1)
        
sum_ = 0

for n in range(1,502):
    sum_ += ring_sum(n)

print(sum_)
    
