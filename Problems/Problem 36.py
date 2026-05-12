#Problem 36
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def ispalindrome(k):
    if k < 10:
        return True
    if k%10 == 0:
        return False #Skip numbers that end with 0
    list_ = list(str(k))
    for i in range(len(list_)):
        if list_[i] != list_[len(list_) - i - 1]:
            return False
    return True

def base10to2(k):
    list_ = []
    while k >= 1:
        list_.append(str(k%2))
        k //= 2
    list_.append(str(k))
    list_.reverse()
    return int(''.join(list_))

sum_ = 0

for i in range(1,1000000):
    if ispalindrome(i) and ispalindrome(base10to2(i)):
        sum_ += i

print(sum_)
