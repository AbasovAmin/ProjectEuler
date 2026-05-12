#Problem 79
#A common security method used for online banking is to ask the user for three random characters from a passcode.
#For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

keylog_file = open('C:\\Users\\PC\\Desktop\\Project Euler\\Problem 79\\keylog.txt').read()

attempts = [attempt for attempt in keylog_file.split('\n') if attempt]

password = []
nodes = []

for attempt in attempts:
    ch1 = attempt[0]
    ch2 = attempt[1]
    ch3 = attempt[2]
    nodes.append((ch1,ch2))
    nodes.append((ch2,ch3))

for a, b in nodes:
    if a in password:
        index_a = password.index(a)
    else:
        password = [a] + password
        index_a = 0
    if b in password:
        index_b = password.index(b)
    else:
        password = password[:index_a] + [b] + password[index_a:]
        index_b = index_a + 1
        
    if index_a > index_b:
        password.remove(a)
        password = password[:index_b] + [a] +  password[index_b:]
        index_a = index_b - 1
    
print(''.join(password))




    
                
                
