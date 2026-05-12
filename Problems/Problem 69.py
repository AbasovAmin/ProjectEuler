#Problem 69
#Find the value of n <= 1 000 000 for which n/𝜙⁡(n) is a maximum.

N = 1_000_000

n_div_phi = [1]*(N+1)
for p in range(2, N + 1):
    if n_div_phi[p] == 1:
        for k in range(p, N + 1, p):
            n_div_phi[k] *= p
            n_div_phi[k] /= p-1

#For bigger n the code can lose the value of the fraction because of many stacked primes. Because of this keeping the fraction is better with this sieve.
'''
from fractions import Fraction

N = 1_000_000

n_div_phi = [Fraction(1,1)] * (N+1)
for p in range(2, N+1):
    if n_div_phi[p] == 1:
        frac = Fraction(p, p-1)
        for k in range(p, N+1, p):
            n_div_phi[k] *= frac'''

best_n = 0
best_ratio = 0

for n in range(2, N+1):
    if n_div_phi[n] > best_ratio:
        best_n = n
        best_ratio = n_div_phi[n]

print(best_n)
        
        
    
