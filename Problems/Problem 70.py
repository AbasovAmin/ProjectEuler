#Problem 70
#Find the value of n, 1 < n <10^7, for which phi(n) is a permutation of n and the ratio n/phi⁡(n) produces a minimum.

N = 10_000_000
phi = list(range(N + 1))

for i in range(2, N + 1):
    if phi[i] == i:          # i is prime
        for j in range(i, N + 1, i):
            phi[j] -= phi[j] // i

def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))
            

min_fraction = 3
min_n = 0

for n in range(2,N+1):
    phi_n = phi[n]
    if is_perm(n, phi_n):
        frac = n/phi_n
        if frac < min_fraction:
            min_fraction = frac
            min_n = n

print(min_n)
