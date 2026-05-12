#Problem 14
#Which starting number, under one million, produces the longest Collatz Sequence chain?

cache = {1: 1}

def collatz_length(n):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3*n + 1
    length = 1 + collatz_length(next_n)
    cache[n] = length
    return length

max_len = 0
max_start = 0

for i in range(1, 1_000_000):
    length = collatz_length(i)
    if length > max_len:
        max_len = length
        max_start = i

print(max_start)



#My solution for this problem which took it 19 seconds
'''dictionary_of_numbers_and_their_chain = {}
biggest_chain_length = 0
biggest_chain_length_generator = 0

for i in range(1,1000000):
    starting_Number = i
    chain_length = 1
    
    while starting_Number != 1:
        
        if starting_Number % 2 == 0:
            starting_Number //= 2
            chain_length += 1
        else:
            starting_Number *= 3
            starting_Number += 1
            chain_length += 1

    dictionary_of_numbers_and_their_chain[i] = chain_length
    if dictionary_of_numbers_and_their_chain[i] > biggest_chain_length:
        biggest_chain_length = dictionary_of_numbers_and_their_chain[i]
        biggest_chain_length_generator = i
        
print(biggest_chain_length_generator)'''



