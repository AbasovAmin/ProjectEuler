#Problem 68
#Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

#Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

#It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

#Total	Solution Set
#9	4,2,3; 5,3,1; 6,1,2
#9	4,3,2; 6,2,1; 5,1,3
#10	2,3,5; 4,5,1; 6,1,3
#10	2,5,3; 6,3,1; 4,1,5
#11	1,4,6; 3,6,2; 5,2,4
#11	1,6,4; 5,4,2; 3,2,6
#12	1,5,6; 2,6,4; 3,4,5
#12	1,6,5; 3,5,4; 2,4,6

#By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

#Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#We need to have all 5 groups of three have the same sum n. 5 numbers are on external nodes; so they each will be only on one group. The other 5 will be on the internal nodes,
#So they will appear twice.
#The third member of the first group of three would be the second member of the second group, and the third member of the second group would be the second member of the third and so on.
#10 should be on an external node, as if it is on an internal node, the formed string would have 17-digits which is not what we need for the question.
#For the 3 - gon, the sum of the numbers 1-6 is 21 and the max they could theoretically generate would be 1+2+3+4*2+5*2+6*2 = 36/3 = 12 which is the 7th and 8th solutions in the example.
#The minimum would be 4+5+6+(1+2+3)*3 = 27/3 = 9
#For the 5 - gon, we would have 1-10 with 10 as an external node, which our maximum theoretically would be 1+2+3+4+10+(5+6+7+8+9)*2 = 90/5 = 18. The minimum theoretically would be
#6+7+8+9+10+(1+2+3+4+5)*2 = 70/5 = 14. From this, we can deduce that we have to look for gons such that the sum should be between 14 and 18.

from itertools import permutations
numbers = [1,2,3,4,5,6,7,8,9]

max_ = 0

for permutation in permutations(numbers):
    groups = [['', '', ''],
          ['', '', ''],
          ['', '', ''],
          ['', '', ''],
          [10, '', '']]
    i = 0
    for k in range(5):
        for j in range(3):
            if groups[k][j] == '':
                if j == 0:
                    groups[k][j] = permutation[i]
                    i += 1
                elif j == 1:
                    groups[k][j] = permutation[i]
                    groups[k-1][j+1] = permutation[i]
                    i += 1
                else:
                    groups[k][j] = permutation[i]
                    groups[k+1][j-1] = permutation[i]
                    i += 1
                    
    group1 = groups[0]
    if all(sum(group1) == sum(group) for group in groups[1:]):
        #Start from smallest external node
        index_min_g = groups.index(min(groups))
        groups = groups[index_min_g:] + groups[:index_min_g]
        sixteen_d = ''
        for group in groups:
            for num in group:
                sixteen_d += str(num)
        if int(sixteen_d) > max_:
            max_ = int(sixteen_d)

print(max_)
        
        
    
    
    
    
    
    
    
                



