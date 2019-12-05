#! python3

#One of my signature practice, no purpose scripts ;-)
#7hi5 i5 4 7iny 1i7713 5(2ip7 7h47 7u2n5 236u142 73x7 in70 1337, (uz why n07?

while True:
    choice = input('Would you like to encode or decode leet? (e or d)' )
    choice = choice.lower()

    if choice == 'e':
        uInput = input('What would you like to turn 1337? ')
        uInput = uInput.lower()

        #The line below is split into multiple lines to keep things looking neat
        leet = uInput\
                .replace('a', '4')\
                .replace('c', '(')\
                .replace('e', '3')\
                .replace('g', '6')\
                .replace('l', '1')\
                .replace('o', '0')\
                .replace('r', '2')\
                .replace('s', '5')\
                .replace('t', '7')
        break
    elif choice == 'd':
        uInput = input('What would you like to decode from 1337? ')
        uInput = uInput.lower()

        #See above comment
        leet = uInput\
                .replace('4', 'a')\
                .replace('(', 'c')\
                .replace('3', 'e')\
                .replace('6', 'g')\
                .replace('1', 'l')\
                .replace('0', 'o')\
                .replace('2', 'r')\
                .replace('5', 's')\
                .replace('7', 't')
        break
    else:
        print("That's not an option!")

print('OUTPUT: ' + leet)
