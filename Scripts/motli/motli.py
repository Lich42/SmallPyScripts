#This is a script for documenting when you do something you're happy about.
#It will keep a log inside a .txt file that you can look back on for motivation.
#I mainly wrote this for practice, and because I thought it was a cool idea for my own personal use ;)

import datetime

file = open('motivation.txt', 'r') #Opens the document in read mode
print(file.read()) #Prints the contents of motivation.txt

uDid = input('What did you do today? (ex = exit, cl = clear) ').lower()

if uDid == 'cl':
	open('motivation.txt', 'w').close() #Clears the document
elif uDid == 'ex':
	quit() #Exits the script
else:
	date = str(datetime.datetime.now()) #Gets the current date/time
	did  = date+': '+uDid #Mashes the date/time and user-defined action together

	file = open('motivation.txt', 'a') #Opens the document in append mode
	file.write(did+'\n') #Pastes the user's action into the document then adds a new blank line