#Problem 90
#Each of the six faces on a cube has a different digit (0 to 9) written on it;
#the same is done to a second cube. By placing the two cubes side-by-side in
#different positions we can form a variety of 2-digit numbers.

#By carefully choosing the digits on both cubes it is possible to display
#all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

#For example, one way this can be achieved is by placing {0,5,6,7,8,9} on one cube
#and {1,2,3,4,8,9} on the other cube.

#However, for this problem we shall allow the 6 or 9 to be turned upside-down so
#that an arrangement like {0,5,6,7,8,9} and {1,2,3,4,6,7} allows for all nine square numbers
#to be displayed; otherwise it would be impossible to obtain 09.

#In determining a distinct arrangement we are interested in the digits on each cube, not the order.

#{1,2,3,4,5,6} is equivalent to {3,6,4,1,2,5}
#{1,2,3,4,5,6} is distinct from {1,2,3,4,5,9}
#But because we are allowing  and  to be reversed, the two distinct sets in the
#last example both represent the extended set {1,2,3,4,5,6,9} for the purpose of forming 2-digit numbers.

#How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

from itertools import combinations as comb

nums = ['0','1','2','3','4','5','6','7','8','9']
needed = ['01','04','09','16','25','36','49','64','81']
count = 0

for dice1 in comb(nums, 6):
    for dice2 in comb(nums, 6):
        if dice1 != dice2:
            if '6' in dice1:
                dice1 += ('9',)
            elif '9' in dice1:
                dice1 += ('6',)
                
            if '6' in dice2:
                dice2 += ('9',)
            elif '9' in dice2:
                dice2 += ('6',)
                
            
            for square in needed:
                if (square[0] in dice1 and square[1] in dice2) or (square[0] in dice2 and square[1] in dice1):
                    continue
                else:
                    count -= 1
                    break
            count += 1

print(int(count/2))
                    
