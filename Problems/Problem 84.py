#A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

#In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

#At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

#Community Chest (2/16 cards):
#Advance to GO
#Go to JAIL
#Chance (10/16 cards):
#Advance to GO
#Go to JAIL
#Go to C1
#Go to E3
#Go to H2
#Go to R1
#Go to next R (railway company)
#Go to next R
#Go to next U (utility company)
#Go back 3 squares.
#The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

#By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

#Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

#If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

def simulation():
    squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1',
           'B2', 'B3', 'J', 'C1', 'U1', 'C2', 'C3', 'R2',
           'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2',
           'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1',
           'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

    squares_count = [0] * 40

    CC = ['AGO', 'G2J'] + ['']*14
    CH = ['AGO', 'G2J', 'G2C1', 'G2E3', 'G2H2', 'G2R1', 'G2nR', 'G2nR', 'G2nU', 'Gb3s'] + ['']*6
    random.shuffle(CC)
    random.shuffle(CH)
    curr_square = 0
    d_count = 0

    for _ in range(1_000_000):
        d_1 = random.randint(1, 4) #four sided dice
        d_2 = random.randint(1, 4) #four sided dice

        if d_1 == d_2:
            if d_count == 2:
                curr_square = 10
                squares_count[curr_square] += 1
                d_count = 0
                continue
            else:
                d_count += 1
        else:
            d_count = 0

        curr_square += d_1 + d_2
        curr_square %= 40
        curr_square_name = squares[curr_square]

        if ('CC' not in curr_square_name) and ('CH' not in curr_square_name) and curr_square_name != 'G2J': #If nothing happens
            squares_count[curr_square] += 1
            continue

        elif 'CC' in curr_square_name:
            #take one card
            card = CC[0]
            CC = CC[1:] + [card] #put it to the end of the deck
            
            if card == '': #if nothing relevant to movement shows up
                squares_count[curr_square] += 1
                continue
            else:
                if card == 'AGO':
                    curr_square = 0
                    squares_count[curr_square] += 1
                    continue
                else:
                    curr_square = 10
                    squares_count[curr_square] += 1
                    continue
                
        elif 'CH' in curr_square_name:
            #take one card
            card = CH[0]
            CH = CH[1:] + [card] #put it to the end of the deck

            if card == '': #if nothing relevant to movement shows up
                squares_count[curr_square] += 1
                continue
            else:
                if 'G2' in card:
                    if 'n' not in card:
                        curr_square = squares.index(card[2:])
                        squares_count[curr_square] += 1
                        continue
                    elif 'n' in card:
                        if 'R' in card:
                            while squares[curr_square][0] != 'R':
                                 curr_square = (curr_square + 1)%40
                            squares_count[curr_square] += 1
                            continue
                        else:
                            while squares[curr_square][0] != 'U':
                                 curr_square = (curr_square + 1)%40
                            squares_count[curr_square] += 1
                            continue
                elif 'b' in card:
                    curr_square = (curr_square - 3) % 40
                    if curr_square == 33:
                        #take one card
                        card = CC[0]
                        CC = CC[1:] + [card] #put it to the end of the deck
                        
                        if card == '': #if nothing relevant to movement shows up
                            squares_count[curr_square] += 1
                            continue
                        else:
                            if card == 'AGO':
                                curr_square = 0
                                squares_count[curr_square] += 1
                                continue
                            else:
                                curr_square = 10
                                squares_count[curr_square] += 1
                                continue
                    else:
                        squares_count[curr_square] += 1
                        continue
                else:  #'AGO'
                    curr_square = 0
                    squares_count[curr_square] += 1
                    continue
                
        elif curr_square_name == 'G2J':
            curr_square = 10
            squares_count[curr_square] += 1
            continue

    top_3 = []
    for _ in range(3):
        a = squares_count.index(max(squares_count))
        a_str = str(a)
        if len(a_str) != 2:
            a_str = '0' + a_str
        squares_count[a] = -1
        top_3.append(a_str)
    return ''.join(top_3)

print(simulation())
