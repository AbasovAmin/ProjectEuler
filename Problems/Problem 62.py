#Problem 62
#The cube, 41063625 (345^3), can be permuted to produce two other cubes:
#56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.


cubes = [n**3 for n in range(10000)]

dct = {}

for cube in cubes:
    signature = ''.join(sorted(str(cube)))
    if signature in dct:
        dct[signature].append(cube)
    else:
        dct[signature] = [cube]

for lst in dct:
    if len(dct[lst]) == 5:
        print(dct[lst])

