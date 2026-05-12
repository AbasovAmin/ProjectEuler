#Problem 39
#If p is the perimeter of a right angle triangle with integral length sides, 
#{a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52},{24,45,51},{30,40,50}

#For which value of p <= 1000, is the number of solutions maximised?

def numofsol(p):
    num = 0
    for a in range(1, p//3 + 1):  #a < c = p-a-b < p-2a ==>  a<p/3
        for b in range(max(a+1, p//2 - a), (p - a)//2 + 1):  # b < c = p-a-b ==> b < (p-a)/2; a + b > c ==> b > p - b - a - a ==> b > (p/2) - a
            c = p - a - b  #hypotenuse candidate
            if a*a + b*b == c*c:
                num += 1
    return num

max_  = 0
the_number = 0
for i in range(12,1001):
    num_ = numofsol(i)
    if num_ > max_:
        max_ = num_
        the_number = i

print(max_)
print(the_number)
