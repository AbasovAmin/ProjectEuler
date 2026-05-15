#Problem 66
#Consider quadratic Diophantine equations of the form:
#   x^2 - D*y^2 = 1

#For example, when D = 13, the minimal solution in x is 649^2 − 13 × 180^2 = 1.

#It can be assumed that there are no solutions in positive integers when D is square.

#By finding minimal solutions in x for D = {2,3,5,6,7}, we obtain the following:

#3^2 − 2×2^2 = 1
#2^2 − 3×1^2 = 1
#9^2 − 5×4^2 = 1
#5^2 − 6×2^2 = 1
#8^2 − 7×3^2 = 1
 
#Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D = 5.

#Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

import math

list_of_D = [D for D in range(2,1001) if int(D**0.5)**2 != D]

def cont_frac_sqrt(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return (a0, []) 

    m = 0
    d = 1
    a = a0

    period = []

    while True:
        m = d * a - m
        d = (n - m*m) // d
        a = (a0 + m) // d
        period.append(a)

        if a == 2*a0:  
            break

    return (a0, period)

max_x = 0
max_D = 0

for D in list_of_D:
    a0, period = cont_frac_sqrt(D)
    p_minus2, p_minus1 = 0, 1
    q_minus2, q_minus1 = 1, 0

    # First convergent (a0)
    p = a0 * p_minus1 + p_minus2
    q = a0 * q_minus1 + q_minus2

    if p*p - D*q*q == 1:
        if p > max_x:
            max_x = p
            max_D = D
            continue
    else:
        p_minus2, p_minus1 = p_minus1, p
        q_minus2, q_minus1 = q_minus1, q
        i = 0
        while True:
            a = period[i % len(period)]
            p = a * p_minus1 + p_minus2
            q = a * q_minus1 + q_minus2

            if p*p - D*q*q == 1:
                if p > max_x:
                    max_x = p
                    max_D = D
                break

            p_minus2, p_minus1 = p_minus1, p
            q_minus2, q_minus1 = q_minus1, q
            i += 1

print(max_x)
print(max_D)
