#Problem 88
#A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,{a_1, a_2,...,a_k}  is called a product-sum number:
#N = a_1 + a_2 +...+ a_k = a_1*a_2*...*a_k .

#For example, 6 = 1 + 2 + 3 = 1*2*3.

#For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
#The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

# k = 2: 4 = 2 + 2 = 2*2     
# k = 3: 6 = 1 + 2 + 3 = 1*2*3         
# k = 4: 8 = 1 + 1 + 2 + 4 = 1*1*2*4        
# k = 5: 8 = 1 + 1 + 2 + 2 + 2 = 1*1*2*2*2          
# k = 6: 12 = 1 + 1 + 1 + 1 + 2 + 6 = 1*1*1*1*2*6

#Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted once in the sum.

#In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

#What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?


def all_sums_and_counts(i, p = 2):
    all_lst = [(i, 1)]
    for k in range(p, int(i**0.5) + 1):
        if i%k == 0:
            sum_k = k
            rem_i = i//k
            all_k = all_sums_and_counts(rem_i, k)
            for SUM, COUNT in all_k:
                all_lst.append((SUM + sum_k, COUNT + 1))

    return all_lst


def num_list(k = 12000):
    dct_of_k = {i: False for i in range(2, 12001)} 
    product_sum_nums = set()
    for i in range(4,24001):
        for SUM, COUNT in all_sums_and_counts(i)[1:]:
            count_i_j = COUNT + i - SUM
            if count_i_j < k + 1 and dct_of_k[count_i_j] == False:
                product_sum_nums.add(i)
                dct_of_k[count_i_j] = True
    return sum(product_sum_nums)

if __name__ == '__main__':
    print(num_list())
            
        
