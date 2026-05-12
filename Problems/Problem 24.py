#A permutation is an ordered arrangement of objects.
#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically, we call
#it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits
#0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

numbers = ['0','1','2','3','4','5','6','7','8','9']

def permutation(list_):
    if len(list_) <= 1:
        return [list_]
    
    else:
        perm_list = []
        
        for i in range(len(list_)):
            
            list_without_i = list_[:i] + list_[i+1:]
            
            for k in permutation(list_without_i):
                perm_list.append([list_[i]] + k)
                
        return perm_list
    

numbers_permutations = permutation(numbers)

for i in range(len(numbers_permutations)):
    ''.join(numbers_permutations[i])
    
numbers_permutations.sort()

print(''.join(numbers_permutations[999999]))
            
        
        
    
