#Problem 19
#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

day = 2 #Since 1 Jan 1901 is a Tuesday

list_month = [31,28,31,30,31,30,31,31,30,31,30,31]
count = 0

for i in range(1901,2001):
    for k in range(len(list_month)):
        if k == 1:
            if i % 4 == 0:
                day += list_month[k] + 1
            else:
                day += list_month[k]
        else:
            day += list_month[k]
        
        if day % 7 == 0:
            count += 1

#Even though this code checks 1 Jan 2001 aswell, since it is a monday it does not matter.
print(count)
        
        
    
    
