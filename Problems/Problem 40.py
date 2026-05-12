#Problem 40
#An irrational decimal fraction is created by concatenating the positive integers:
#  0.123456789101112131415161718192021.....
#It can be seen that the 12th digit of the fractional part is 1.
#If d_n represents the nth digit of the fractional part,
#find the value of the following expression.

# d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

def find__d_n(n):
    k = 2
    string = '1'
    while len(string) < n:
        string += str(k)
        k += 1
    return int(string[n-1])

print(find__d_n(1)*find__d_n(10)*find__d_n(100)*find__d_n(1000)*find__d_n(10000)*find__d_n(100000)*find__d_n(1000000))
