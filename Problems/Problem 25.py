#Problem 25
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

f1 = 1
f2 = 1
count = 2

while True:
    if len(str(f2)) == 1000:
        print(count)
        break
    else:
        f1,f2 = f2,f1+f2
        count += 1
