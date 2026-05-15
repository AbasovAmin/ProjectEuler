#Problem 97
#The first known prime found to exceed one million digits was discovered in 1999, and is a
#Mersenne prime of the form 2^6972593 - 1; it contains exactly 2098960 digits. Subsequently other Mersenne primes, of the form 2^p - 1, have been found which contain more digits.

#However, in 2004 there was found a massive non-Mersenne prime which contains 2357207 digits: 28433*(2^7830457) + 1.

#Find the last ten digits of this prime number.

MOD = 10**10
power_part = pow(2, 7830457, MOD)
result = (28433 * power_part + 1) % MOD

print(result)



