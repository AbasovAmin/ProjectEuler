#Problem 100
#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
#and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2.

#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

#By finding the first arrangement to contain over 10^12 = 1_000_000_000_000 discs in total, determine the number of blue discs that the box would contain.



#Looking at the math, for a box containing n blue and m red disks, the chances of taking two blue disks are n/(n+m) * (n-1)/(n+m-1) = n*(n-1)/(n+m)*(n+m-1)
#For this fraction to equal 1/2, we need numbers n and m such that 2*n^2 - 2*n = n^2 + m^2 - n - m + 2*n*m ===> n^2 + m - n - 2*n*m - m^2 = 0 so our requirements are
#n^2 + m - n - 2*n*m - m^2 = 0 and n + m > 10^12. Rewriting the equation, 2n^2 + m - n = (m + n)^2 ===> 2n^2 - 2*n = (m + n)^2 - (m + n) ===
#===> 8n^2 - 8n = 4(m + n)^2 - 4(m + n) ===> 2*(2*n - 1)^2 - 1 = (2*(m + n) - 1)^2. Suppose X = 2*n - 1 and Y = 2*(m + n) - 1. Then Y^2 - 2X^2 = -1 which is the Pell's equation.
#For this specific case of Pell's equation, once a solution is found, the next solutions are of the form
#X_(k+1) = 3X_k + 2Y_k
#Y_(k+1) = 4X_k + 3Y_k
#One solution is the obvious solution given in the question itself, 29 and 41, which we will then use to find the other solutions till (Y + 1)/2 > 10^12

X = 29
Y = 41

upper_bound = 10**12

while (Y + 1)//2 < upper_bound:
    X, Y = 3*X + 2*Y, 4*X + 3*Y

print((X + 1)//2)
