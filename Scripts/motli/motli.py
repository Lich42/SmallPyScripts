#This is a script for documenting when you do something you're happy about.
#It will keep a log inside a .txt file that you can look back on for motivation.
#I mainly wrote this for practice, and because I thought it was a cool idea for my own personal use ;)

import datetime

file = open('motivation.txt', 'r')
print(file.read())

uDid = input('What did you do? (ex = exit, cl = clear) ').lower()

if uDid == 'cl':
	open('motivation.txt', 'w').close()
elif uDid == 'ex':
	quit()
else:
	date = str(datetime.datetime.now())
	did  = date+': '+uDid

	file = open('motivation.txt', 'a')
	file.write(did+'\n')