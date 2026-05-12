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
