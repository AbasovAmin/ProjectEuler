#Problem 72
#How many elements would be contained in the set of reduced proper fractions for d <= 1 000 000?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#There would be phi(d) number of reduced proper fractions for any d

#Sieve for phi
N = 1_000_000
phi = list(range(N+1))
for p in range(2, N+1):
    if phi[p] == p:
        for k in range(p, N+1, p):
            phi[k] -= phi[k]//p

print(sum(phi[2:]))          
