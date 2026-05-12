#Problem 15
#Starting in the top left corner of a 2x2 grid, and only being
#able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20x20 grid?

def factorial(k):
    if k == 0:
        return 1
    else:
        return k*factorial(k-1)

print(factorial(40)//factorial(20)**2)
    
