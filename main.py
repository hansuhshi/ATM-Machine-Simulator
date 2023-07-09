from stdiomask import getpass #Stdiomask is a module for entering passwords to a stdio terminal and displaying a **** mask.
#The getpass() function is used to prompt to users using the string prompt and reads the input from the user as password

from os import system, name, fdopen, remove

import hashlib #Used the hashlib hashing function to convert the passwords and 'encrypt' them  

from tempfile import mkstemp #This module creates temporary files and directories. mkstemp 

from shutil import move, copymode #This module helps automate copying files and directories.

#this is for time.sleep() to stop the code for a bit
import time

#this is for generating random numbers on the receipt so it looks cooler and more legit
import random

#this is for the time for the receipt so I can get instant time
from datetime import datetime

#used for listdir() which returns a list containing the names of the entries in the directory given by path
import os

#scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object 
import re

#construct a list from those elements of the iterable names that match pattern.
import fnmatch

#function to clear screen (stackoverflow)
def clearScreen():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def ascii(): #Just incase it is used multiple times, the bank's ascii art title will be saved here (priyesh)
																																																			
  print("▒▒▒▒▒▒╗      ▒▒╗▒▒▒▒▒▒▒╗▒▒▒▒▒▒▒╗▒▒╗  ▒▒╗▒▒▒▒▒▒▒╗    ▒▒▒▒▒▒╗  ▒▒▒▒▒╗ ▒▒▒╗   ▒▒╗▒▒╗  ▒▒╗")
  print("▒▒╔══▒▒╗     ▒▒║▒▒╔════╝▒▒╔════╝▒▒║  ▒▒║▒▒╔════╝    ▒▒╔══▒▒╗▒▒╔══▒▒╗▒▒▒▒╗  ▒▒║▒▒║ ▒▒╔╝")
  print("▒▒▒▒▒▒╔╝     ▒▒║▒▒▒▒▒╗  ▒▒▒▒▒▒▒╗▒▒▒▒▒▒▒║▒▒▒▒▒╗      ▒▒▒▒▒▒╔╝▒▒▒▒▒▒▒║▒▒╔▒▒╗ ▒▒║▒▒▒▒▒╔╝ ")
  print("▒▒╔══▒▒╗▒▒   ▒▒║▒▒╔══╝  ╚════▒▒║▒▒╔══▒▒║▒▒╔══╝      ▒▒╔══▒▒╗▒▒╔══▒▒║▒▒║╚▒▒╗▒▒║▒▒╔═▒▒╗ ")
  print("▒▒▒▒▒▒╔╝╚▒▒▒▒▒╔╝▒▒▒▒▒▒▒╗▒▒▒▒▒▒▒║▒▒║  ▒▒║▒▒▒▒▒▒▒╗    ▒▒▒▒▒▒╔╝▒▒║  ▒▒║▒▒║ ╚▒▒▒▒║▒▒║  ▒▒╗")
  print("╚═════╝  ╚════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝")

#written by "Anthony Rota" https://github.com/anthonyrota (Copyright 2020 - MIT License)
# Copyright 2020 Anthony Rota
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#this function will check if there is a valid input for option selection
def userInput(answer, conditions):
	print()
	error = ""
	while True:
		#prints the first/previous error
		if error:
			print(error)
			print()
		userInput = input(answer)
		#if there is no input continue the loop
		if userInput == None:
			continue
		for condition, errormessage in conditions:
			#if the user input is invalid under this condition, save the error message for this condition to be printed next time in the loop
			if not condition(userInput.strip()):
				error = errormessage
				break
		#if there are no errors return the input
		else:
			return userInput

#validates input so user can only input chosen repsonses (hansuh)
def confirmOption4(input):
	return input == "1" or input == "2" or input == "3" or input == "4"

#response to the input (hansuh)
def askOption4(question):
	optionOutput = userInput(question, [[confirmOption4, "PLEASE RESPOND WITH 1, 2, 3 OR 4"]])
	return optionOutput

#validates input so user can only input chosen repsonses (hansuh)
def confirmOption2(input):
	return input == "1" or input == "2"

#response to the input (hansuh)
def askOption2(question):
	optionOutput = userInput(question, [[confirmOption2, "PLEASE RESPOND WITH 1 OR 2"]])
	return optionOutput

#screen for welcome users (hansuh)
def welcomeScreen():
	clearScreen()
	print("WELCOME TO\n")
	ascii()
	print("\nPRESS ENTER TO CONTINUE")
	input()
	print()
	clearScreen()
	print("BJESHE BANK")
	print("--------------------")
	print()
	print("1. LOGIN")
	print("2. REGISTER")
	userChoice = askOption2("ENTER AN OPTION: ")
	if userChoice == "1":
		login()
	else:
		register()

#function that registers users to (hansuh)
def register():
	clearScreen()
	print("REGISTER")
	print("--------------------")
	print()
	#loop for asking username 
	while True:
		#.title() returns a string where the first letter is capitalised
		userName = input("ENTER YOUR NAME (NO DIGITS OR SPECIAL CHARACTERS OR SPACES ALLOWED): ").title()
		if not userName.isalpha():
			print("ONLY CHARACTERS FROM THE ALPHABET ALLOWED\n")
			continue
		else:
			break
	userName = modifyName(userName)
	if userAlreadyExists(userName):
		userAlreadyExistsMessage()
	else:
		#loop for asking password
		while True:
			#asks for password and puts it in asterisks
			userPassword = getpass("ENTER YOUR PASSWORD (4 DIGIT PIN): ")
			if len(userPassword) == 4:
				try:
					int(userPassword)
					break
				except ValueError:
					print("YOUR PASSWORD MUST BE 4 DIGITS\n")
					continue
			else:
				print("YOUR PASSWORD MUST BE 4 DIGITS\n")
		while True:
			confirmPassword = getpass("CONFIRM YOUR PASSWORD (4 DIGIT PIN): ")
			if confirmPassword == userPassword:
				break
			else:
				print("PASSWORDS DON'T MATCH")
	#adds the username and hashed password into the user information txt file
	addUserInformation([userName, hashPassword(userPassword), "0"])
	print()
	afterRegister = askOption2("REGISTRATION COMPLETE\n\n1. LOGIN\n2. EXIT\n\nENTER AN OPTION: ")
	if afterRegister == "1":
		login() 
	else:
		welcomeScreen()

#login function (hansuh)
def login():
	clearScreen()
	print("LOGIN")
	print("--------------------")
	print()
	global usersInformation
	#blank dictionary
	usersInformation = {}
	#opens user information file for reading 
	with open("userInformation.txt", "r") as file:
		for line in file:
			line = line.split() 
			#puts names and passwords in dictionary
			usersInformation.update({line[0]: line[1]})
	while True:
		global userName
		userName = input("ENTER YOUR USERNAME: ").title()
		userName = modifyName(userName)
		#checks for input in dictionary and if it is not then get them to register or try again
		if userName not in usersInformation:
			print()
			error = askOption2("YOU ARE NOT REGISTERED\n\n1. TRY AGAIN\n2. REGISTER\n\nENTER AN OPTION: ")
			if error == "1":
				login() 
			else:
				register() 
		else:
			break
	while True:
		global userPassword
		userPassword = getpass("ENTER YOUR PASSWORD: ")
		#checks for if input matches unencoded stored password
		if not checkPasswordHash(userPassword, usersInformation[userName]):
			print("INCORRECT PASSWORD")
			print() 
		else:
			break
	print()
	print("LOGGED IN")
	mainMenu()

#function for writing register input into user information txt file (hansuh)
def addUserInformation(userInformation: list):
	with open("userInformation.txt", "a") as file:
		file.write(" ".join(userInformation))
		file.write("\n")

#checks for the user and if they are in the txt file (hansuh)
def userAlreadyExists(userName, userPassword=None):
	if userPassword == None:
		#opens the user information and searches for the username
		with open("userInformation.txt", "r") as file:
			for line in file:
				line = line.split()
				#if the username is in the file then it returns true and in the login function it will go to the message
				if line[0] == userName:
					return True
		#otherwise return false and go to else in the login function 
		return False
	#if the user is not in the user information txt file
	else:
		userPassword = hashPassword(userPassword)
		#empty dictionary
		usersInformation = {}
		with open("userInformation.txt", "r") as file:
			for line in file:
				line = line.split() 
				if line[0] == userName and line[1] == userPassword:
					#updates dictionary with the username and passwords
					usersInformation.update({line[0]: line[1]})
		#if the updated dictionary is empty then return false and go to else in the login function
		if usersInformation == {}:
			return False
		return usersInformation[userName] == userPassword

#message for if the user already exists (hansuh)
def userAlreadyExistsMessage():
	print()
	error = askOption2("THIS USERNAME IS TAKEN\n\n1. TRY AGAIN\n2. LOGIN\n\nENTER AN OPTION: ") 
	if error == "1":
		register() 
	else:
		login() 

#splits username and joins for the system to recognise (hansuh)
def modifyName(userName):
	userName = userName.split()
	userName = '-'.join(userName)
	return userName

#encodes password for extra security in the txt file (stackoverflow)
def hashPassword(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

#reverse the encoding for the system to check if it is the right password (hansuh)
def checkPasswordHash(password, hash):
	return hashPassword(password) == hash

#function for the main menu (hansuh)
def mainMenu():
	clearScreen()
	print("MAIN MENU")
	print("--------------------")
	print() 
	print("1. ACCOUNT DETAILS\n2. WITHDRAW\n3. DEPOSIT\n4. EXIT")
	mainMenuChoice = askOption4("ENTER AN OPTION: ")
	if mainMenuChoice == "1":
		accountDetails()
	elif mainMenuChoice == "2":
		withdrawal()
	elif mainMenuChoice == "3":
		deposit()
	elif mainMenuChoice == "4":
		welcomeScreen()

#function for new name (hansuh)
def askNewName():
	while True:
		clearScreen()
		newName = input("ENTER YOUR NEW ACCOUNT NAME: ").title()
		#checks if the input is all alphabet letters
		if not newName.isalpha():
			while True:
				error = askOption2("ONLY CHARACTERS FROM THE ALPHABET ALLOWED\n\n1. TRY AGAIN\n2. GO BACK")
				if error == "1":
					askNewName() 
				else:
					accountDetails()			
		else:
			break
	newName = modifyName(newName)
	if userAlreadyExists(newName):
		while True:
			error = askOption2("THAT NAME IS ALREADY TAKEN\n\n1. TRY AGAIN\n2. GO BACK\n\nENTER AN OPTION: ") 
			if error == "1":
				askNewName()
			else:
				accountDetails() 
	else:
		while True:
			confirmName = input("CONFIRM YOUR NEW ACCOUNT NAME: ").title()
			if modifyName(confirmName) == newName:
				with open('userInformation.txt','r') as file:
					lines = file.read().split("\n")
				for i, line in enumerate(lines):
					if userName in line: 
						with open("userInformation.txt") as file:
							lines = file.readlines()
							originalLine = lines[i]
							a,b,c = lines[i].split(" ")
							a = confirmName
							joinedLine = (a,b,c)
							newName = " ".join(joinedLine)
							searchAndReplace("userInformation.txt", originalLine, newName)
				print("\nYOUR CHANGES HAVE BEEN SAVED")
				time.sleep(2.5)
				clearScreen()
				welcomeScreen()
			else:
				print("USERNAMES DON'T MATCH")

#function for new password (hansuh)
def askNewPassword():
	while True:
		clearScreen() 
		userPassword = getpass("ENTER YOUR PASSWORD (4 DIGIT PIN): ")
		#checks if the password is 4 digits long
		if len(userPassword) == 4:
			#then it checks if it is an integer
			try:
				int(userPassword)
				break
			except ValueError:
				print("YOUR PASSWORD MUST BE 4 DIGITS\n")
				continue
		else:
			print("YOUR PASSWORD MUST BE 4 DIGITS\n")
	while True:
		confirmPassword = getpass("CONFIRM YOUR PASSWORD (4 DIGIT PIN): ")
		if confirmPassword == userPassword:
			with open('userInformation.txt','r') as file:
				lines = file.read().split("\n")
			for i, line in enumerate(lines):
				if userName in line: 
					with open("userInformation.txt") as file:
						lines = file.readlines()
						originalLine = lines[i]
						a,b,c = lines[i].split(" ")
						#changes the password
						b = hashPassword(confirmPassword)
						joinedLine = (a,b,c)
						newPassword = " ".join(joinedLine)
						searchAndReplace("userInformation.txt", originalLine, newPassword)
					print("\nYOUR CHANGES HAVE BEEN SAVED")
					time.sleep(2.5)
					clearScreen() 
					welcomeScreen()
		else:
					print("PASSWORDS DON'T MATCH")

#function for viewing the balance and changing the account details (hansuh)
def accountDetails():
	clearScreen()
	print("ACCOUNT DETAILS")
	print("--------------------")
	print()
	print("NAME:", userName)
	checkBalance()
	change = askOption2("1. EDIT ACCOUNT DETAILS\n2. GO BACK\n\nENTER AN OPTION: ")
	if change == "1":
		clearScreen() 
		changeWhat = askOption4("1. CHANGE NAME\n2. CHANGE PASSWORD\n3. DELETE ACCOUNT\n4. GO BACK\n\nENTER AN OPTION: ")
		if changeWhat == "1":
			clearScreen() 
			passwordSecurity()
			askNewName()
		elif changeWhat == "2":
			clearScreen() 
			passwordSecurity()
			askNewPassword()
		elif changeWhat == "3":
			deleteAccount()
		else:
			clearScreen()
			accountDetails()
	else:
		mainMenu()

#function for looping for asking for password (hansuh)
def passwordSecurity():
	while True:
		userPassword = getpass("ENTER YOUR PASSWORD: ")
		if not checkPasswordHash(userPassword, usersInformation[userName]):
			print("INCORRECT PASSWORD")
			print() 
		else:
			break

#function for searching and replacing things in the text file (stackoverflow)
def searchAndReplace(filePath, pattern, subst):
	#create temporary file
	fh, absPath = mkstemp()
	with fdopen(fh,'w') as newFile:
		with open(filePath) as oldFile:
			for line in oldFile:
				newFile.write(line.replace(str(pattern), subst))
	#copy the file permissions from the old file to the new file
	copymode(filePath, absPath)
	#remove original file
	remove(filePath)
	#move new file
	move(absPath, filePath)

def is_whole(n): #checks if the withdrawal amount is a whole number by telling us how many remainders we have when we divide by 1 (priyesh)
    return n % 1 == 0

#function to withdraw money from the account (priyesh/hansuh)
def withdrawal():
	global c
	global transactionType
	transactionType = "WITHDRAW"
	clearScreen()
	print("WITHDRAW")
	print("--------------------")
	while True:
		with open('userInformation.txt','r') as file:
			lines = file.read().split("\n")
		for i, line in enumerate(lines):
			if userName in line: 
				with open("userInformation.txt") as file:
					lines = file.readlines()
					originalLine = lines[i]
					a,b,c = lines[i].split(" ")
					#turns the balance into an integer so it can be added to or subtracted from
					balance = int(str.format(c))
		try:
			global amount
			amount = int(input("\nHOW MUCH WOULD YOU LIKE TO WITHDRAW (ONLY NOTES ABOVE $10 CAN BE WITHDRAWN): $"))
			if amount < 0: # if not a positive integer
				print("ENTER A POSITIVE NUMBER\nNOT ACCEPTED")
			elif balance - amount < 0:
				print("BALANCE WILL BE NEGATIVE\nNOT ACCEPTED")
			elif is_whole(amount/10) == True: #Making sure the amount asking to be withdrawn is a multiple of 10
				c = str(balance-amount) #Converts new balance to str so it can be used in the searchAndReplace function
				joinedLine = (a,b,c)
				newBalance = " ".join(joinedLine)
				searchAndReplace("userInformation.txt", originalLine, "{}\n".format(newBalance)) #replaces balance with the new one
				print("\nTHANK YOU FOR WITHDRAWING WITH BJESHE BANK")
				while True:
					receiptChoice = askOption2("WOULD YOU LIKE A RECEIPT\n\n1. YES\n2. NO\n\nENTER AN OPTION: ")
					if receiptChoice == "1":
						receipt() 
						break
					else: 
						break
				welcomeScreen()
			elif is_whole(amount/10) == False:
				print("ONLY NOTES ABOVE $10 CAN BE WITHDRAWN")
		except ValueError:
			print("COINS AND $5 NOTES ARE NOT ACCEPTED")		

#function to deposit money into the account (priyesh/hansuh)
def deposit():
	global c
	global transactionType
	transactionType = "DEPOSIT"
	clearScreen()
	print("DEPOSIT")
	print("--------------------")
	while True:
		with open('userInformation.txt','r') as file:
			lines = file.read().split("\n")
		for i, line in enumerate(lines):
			if userName in line: 
				with open("userInformation.txt") as file:
					lines = file.readlines()
					originalLine = lines[i]
					a,b,c = lines[i].split(" ")
					balance = int(str.format(c))
		try:
			global amount
			amount = int(input("\nHOW MUCH WOULD YOU LIKE TO DEPOSIT? (ONLY NOTES ABOVE $10 CAN BE DEPOSITED): $"))
			if amount < 0:
				print("ENTER A POSITIVE NUMBER\nNOT ACCEPTED")
			elif is_whole(amount/10) == True:
				c = str(balance + amount) 
				joinedLine = (a,b,c)
				newBalance = " ".join(joinedLine)
				searchAndReplace("userInformation.txt", originalLine, "{}\n".format(newBalance)) 
				print("\nTHANK YOU FOR DEPOSITING WITH BJESHE BANK")
				while True:
					receiptChoice = askOption2("WOULD YOU LIKE A RECEIPT\n\n1. YES\n2. NO\n\nENTER AN OPTION: ")
					if receiptChoice == "1":
						receipt() 
						break
					else: 
						break
				welcomeScreen()
			elif is_whole(amount/10) == False:
				print("ONLY NOTES ABOVE $10 CAN BE DEPOSITED")
		except ValueError:
			print("COINS AND $5 NOTES ARE NOT ACCEPTED")

#function for deleting account (hansuh)
def deleteAccount():
	clearScreen()
	passwordSecurity() 
	clearScreen()
	confirmDeletion = askOption2("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT\n\n1. YES\n2. NO\n\nENTER AN OPTION: ")
	if confirmDeletion == "1":
		searchAndReplace("userInformation.txt", lines[i], "")
		clearScreen() 
		welcomeScreen()
	else:
		clearScreen() 
		mainMenu()

#function for the receipt (hansuh/stackoverflow)
def receipt():
	# uppercase because it's a constant
	ROOT = "./"
	# i'm supposing that each item in ROOT folder that matches "{}'s Receipt.txt*".format(userName) is a file which we are looking for
	files = fnmatch.filter((f for f in os.listdir(ROOT)), "{}'s Receipt*.txt".format(userName))
	# if it is empty
	if not files:
		number = ""
	elif len(files) == 1:
		number = "(1)"
	else:
		# files is supposed to contain "{}'s Receipt.txt".format(userName)"
		files.remove("{}'s Receipt.txt".format(userName))
		number = "(%i)" % (int(re.search(r"\(([0-9]+)\)", max(files)).group(1)) + 1)
	with open("{}'s Receipt%s.txt".format(userName) % number, "w") as f:
		f.write("------------------------------\nBJESHE BANK ATM\n------------------------------\n\nTERMINAL #            {}\n".format(random.randint(10000000, 99999999)))
		f.write("SEQUENCE #              {}\n".format(random.randint(100000, 999999)))
		f.write("AUTH #                {} 00\n".format(random.randint(10000, 99999)))
		now = datetime.now()
		f.write("DATE       {}\n\n".format(now.strftime("%d/%m/%Y %H:%M:%S")))
		f.write("CUSTOMER NAME: {}\n".format(userName))
		f.write("TRANSACTION TYPE: {}\n".format(transactionType))
		f.write("TRANSACTION AMOUNT: ${}\n".format(amount))
		f.write("CURRENT BALANCE: ${}".format(c))

#function for checking balance (hansuh)
def checkBalance():
	global lines
	global i
	#opens the file and splits for reading
	with open('userInformation.txt','r') as file:
		lines = file.read().split("\n")
	#enumerate giving back count and value of the item
	for i, line in enumerate(lines):
		if userName in line: 
			with open("userInformation.txt") as file:
				#gets the line with username and password and gets the balance
				lines = file.readlines()
				break
	a,b,c = lines[i].split(" ")
	print("BALANCE: ${}".format(c))

#function 

welcomeScreen()

#password for dunne = 1111, hansuh = 1234, hari = 4444, priyesh = 2222