#Problem 26
# 0.1(6) means 0.16666666.... , and has a 1-digit recurring cycle.
#It can be seen that 1/7 has a 6-digit recurring cycle as 1/7 = 0.(142857)
#Find the value of d < 1000 for which 1/d contains the longest
#recurring cycle in its decimal fraction part.

maximum = 0
the_number = 0

for d in range(1,1000):
    seen_remainders = []
    position = 0
    remainder = 1

    while remainder not in seen_remainders:
         seen_remainders.append(remainder)
         remainder = (remainder*10)%d
         position += 1

    if maximum < len(seen_remainders[seen_remainders.index(remainder):]):
        maximum = len(seen_remainders[seen_remainders.index(remainder):])
        the_number = d

print(the_number)


#Cleaner solution by ChatGPT
'''
maximum = 0
the_number = 0

for d in range(1, 1000):
    seen_remainders = {}  # remainder -> position
    remainder = 1
    position = 0

    while remainder not in seen_remainders:
        seen_remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1

    cycle_length = position - seen_remainders[remainder]

    if cycle_length > maximum:
        maximum = cycle_length
        the_number = d

print(the_number)'''
