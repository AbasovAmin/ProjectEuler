#Problem 54
#Too long again, check projecteuler

#Let us create a value function
suits = ['C', 'S', 'H', 'D']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
hand_ranking = ['HC', 'OP', 'TP', 'TK', 'S', 'F', 'FH', 'FK', 'SF', 'RF']

def value(hand):
    Flush = False
    Straight = False
    Pair = False
    Three_of_a_kind = False
    values_hand = []
    suits_hand = []
    relevant_value_hand = []
    
    for value in hand:
        values_hand.append(values[value[0]])
        suits_hand.append(value[1])
    values_hand.sort()
    
    for suit in suits:   #Flush check
        if suits_hand.count(suit) == 5:
            Flush = True
            
    if (len(set(values_hand)) == 5 and max(values_hand) - min(values_hand) + 1 == 5) or values_hand == [2, 3, 4, 5, 14]:    #Straight check
        Straight = True

    if Straight == True and Flush == True:
        if values_hand == [10,11,12,13,14]:
            return ['RF', values_hand, values_hand]
        else:
            return ['SF', values_hand, values_hand]
    elif Straight == True:
        return ['S', values_hand, values_hand]
    elif Flush == True:
        return ['F', values_hand, values_hand]

    if not Straight:
        for value in set(values_hand):
            count = values_hand.count(value)
            if  count == 2:
                if Three_of_a_kind == True:
                    return ['FH', values_hand, values_hand]
                elif Pair == False:
                    Pair = True
                    for _ in range(2):
                        relevant_value_hand.append(value)
                else:
                    for _ in range(2):
                        relevant_value_hand.append(value)
                    return ['TP', relevant_value_hand, values_hand]
                    
            elif count == 3:
                if Pair == False:
                    Three_of_a_kind = True
                    for _ in range(3):
                        relevant_value_hand.append(value)
                else:
                    return ['FH', values_hand, values_hand]
            elif count == 4:
                for _ in range(4):
                    relevant_value_hand.append(value)
                return ['FK', relevant_value_hand, values_hand]

    if Pair == True:
        return ['OP', relevant_value_hand, values_hand]
    else:
        if Three_of_a_kind == True:
            return ['TK', relevant_value_hand, values_hand]

    return ['HC', values_hand, values_hand]


#Now a comparison function
def compare(hand1, hand2):
    result_1 = value(hand1)
    result_2 = value(hand2)
    
    value_1 = hand_ranking.index(result_1[0])
    value_2 = hand_ranking.index(result_2[0])
    
    relevant_1 = sorted(result_1[1])
    relevant_2 = sorted(result_2[1])

    general_1 = result_1[2]
    general_2 = result_2[2]
    
    if  value_1 > value_2:
        return True
    elif value_1 < value_2:
        return False
    else:
        if relevant_1 == [2,3,4,5,14]:
            return False
        elif relevant_2 == [2,3,4,5,14]:
            return True
        
        for i in range(len(relevant_1) - 1, -1, -1):
            if relevant_1[i] > relevant_2[i]:
                return True
            elif relevant_1[i] < relevant_2[i]:
                return False
        for i in range(4, -1, -1):
            if general_1[i] > general_2[i]:
                return True
            elif general_1[i] < general_2[i]:
                return False
            

poker_file = open('C:\\Users\\PC\\Desktop\\Project Euler\\Problem 54\\poker.txt').read()

games = [
    [game.split()[0:5], game.split()[5:10]]
    for game in poker_file.strip().split('\n')
    if game.strip()
    ]

count_win = 0
for game in games:
    if compare(game[0], game[1]) == True:
        count_win += 1

print(count_win)
        































