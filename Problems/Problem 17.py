#Problem 17
#If all the numbers from 1 to 1000 (one thousand) inclusive were
#written out in words, how many letters would be used?

number_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven' , 12: 'twelve', 13: 'thirteen', 
               14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
               50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred',
               500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred'}


def letterInNumber(k):
    if k in number_dict:
        return number_dict[k]
    
    hundreds = k//100*100
    ones = k%10
    tens = k - ones - hundreds
    if number_dict[hundreds] != '':
        letters = number_dict[hundreds] + 'and' + letterInNumber(k%100)
    else:
        letters = number_dict[tens] + number_dict[ones]
    return letters

answer = 11 #one thousand

for i in range(1,1000):
    answer += len(letterInNumber(i))

print(answer)
    
    
