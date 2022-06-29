#!/usr/bin/env python3
from random import choice,shuffle
import datetime 
from hashlib import sha1,sha224,sha256,sha384,sha512,sha3_224,sha3_256,sha3_384,sha3_512
from time import sleep
from os import system,path,chdir,mkdir

system("")

upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
special_letters = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]"]

letters = upper_letters + lower_letters + digits + special_letters
passwrd = []

pwd = "./CLI_Password_Gen"
doesExists = path.exists(pwd)
if doesExists == False:
	mkdir("./CLI_Password_Gen")
	chdir("./CLI_Password_Gen")
else:
	chdir("./CLI_Password_Gen")

print('''
		
\u001b[33m░█████╗░██╗░░░░░██╗  ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██║░░░░░██║  ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██║░░░░░██║  ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██║░░██╗██║░░░░░██║  ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
╚█████╔╝███████╗██║  ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
░╚════╝░╚══════╝╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\u001b[0m
	# Made by \u001b[37;1mSrcyDev\u001b[0m (https://github.com/SrcyDev/)
	# Project: \u001b[37;1mCLI Password Generator\u001b[0m (https://github.com/SrcyDev/CLI-Password-Generator/)
''')
def process():
	sleep(0.7)
	print("\u001b[36mEnter password length: \u001b[0m")
	pno = str(input("\u001b[32m>\u001b[1C \u001b[0m"))
	
	if pno == "":
		pno = 16
	pno = int(pno)
	if pno <= 0:
		print("\u001b[31mPassword Cannot be 0 or less.\u001b[0m")
		process()
	shuffle(letters)
	i = 1

	while i != pno:
		passwrd.append(choice(letters))
		i = i + 1
	
	shuffle(passwrd)
	c = "".join(passwrd)
	passwrd.clear()
	sleep(0.7)
	print("\u001b[36mEnter your password use-case incase you forget it. (Optional) : \u001b[0m")
	usecase = str(input("\u001b[32m>\u001b[1C \u001b[0m"))
	sleep(0.7)
	print("\u001b[36mDo you want to hash it and view the hashed password ? \u001b[34;1m(SHA)\u001b[0m\u001b[36m(\u001b[0m\u001b[37;1m[Y]\u001b[0mes/\u001b[37;1m[N]o\u001b[0m\u001b[36m) :\u001b[0m")
	ask = input("\u001b[32m>\u001b[1C \u001b[0m").lower()
	sleep(0.7)
	print("The password is: " + c)
	print("The generated password is also stored in \u001b[37;1m./CLI_Password_Gen\generated_password.txt\u001b[0m file.")
	generation_time = datetime.datetime.now()
	file = open("generated_password.txt","a")
	if usecase == "":	
		file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
	else:
		file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "-" + usecase + "\n")	
	file.close()
    
	if ask == "yes" or ask == "ye" or ask == "y":
        
		hash1 = sha1(c.encode()).hexdigest()
		hash224 = sha224(c.encode()).hexdigest()
		hash256 = sha256(c.encode()).hexdigest()
		hash384 = sha384(c.encode()).hexdigest()
		hash512 = sha512(c.encode()).hexdigest()	
		hash3_224 = sha3_224(c.encode()).hexdigest()
		hash3_256 = sha3_256(c.encode()).hexdigest()
		hash3_384 = sha3_384(c.encode()).hexdigest()
		hash3_512 = sha3_512(c.encode()).hexdigest()
        
		print("The hashed password in sha1 is: " + hash1)
		sleep(0.5)
		print("The hashed password in sha224 is: " + hash224)
		sleep(0.5)
		print("The hashed password in sha256 is: " + hash256)
		sleep(0.5)
		print("The hashed password in sha384 is: " + hash384)
		sleep(0.5)
		print("The hashed password in sha512 is: " + hash512)
		sleep(0.5)
		print("The hashed password in sha3_224 is: " + hash3_224)
		sleep(0.5)
		print("The hashed password in sha3_256 is: " + hash3_256)
		sleep(0.5)
		print("The hashed password in sha3_384 is: " + hash3_384)
		sleep(0.5)
		print("The hashed password in sha3_512 is: " + hash3_512)
		sleep(0.5)

		hash_store = open("hashed_password.txt","a")
		hash_store.write("The hashes for password "+ c +" generated at "  +  " : " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S"))  + " is: \n")
		hash_store.write("	The hash in sha1 is: " + str(hash1) + " \n")
		hash_store.write("	The hash in sha224 is: " + str(hash224) + " \n")
		hash_store.write("	The hash in sha256 is: " + str(hash256) + " \n")
		hash_store.write("	The hash in sha384 is: " + str(hash384) + " \n")
		hash_store.write("	The hash in sha512 is: " + str(hash512) + " \n")
		hash_store.write("	The hash in sha3_224 is: " + str(hash3_224) + " \n")
		hash_store.write("	The hash in sha3_256 is: " + str(hash3_256) + " \n")
		hash_store.write("	The hash in sha3_384 is: " + str(hash3_384) + " \n")
		hash_store.write("	The hash in sha3_512 is: " + str(hash3_512) + " \n\n")
		hash_store.close()
		print("The generated hash is also stored in \u001b[37;1m./CLI_Password_Gen\hash_password.txt\u001b[0m file.")
        
		

		
	elif ask == "no" or ask == "n" or ask == "":
		pass
	else:
		print("\u001b[31;1mHash was not generated.\u001b[0m")
	

def ask():
	sleep(0.7)
	print("\u001b[36mDo you want to continue ? (\u001b[37;1m[Y]\u001b[0mes/\u001b[37;1m[N]o\u001b[0m\u001b[36m) :\u001b[0m ")
	asks = input("\u001b[32m> \u001b[0m").lower()
	if asks == "yes" or asks == "ye" or asks == "y" or asks == "":
		while asks == "yes" or asks == "ye" or asks == "y" or asks == "":
			print("\u001b[32;1mContinuing...\u001b[0m")
			process()
			ask()
			
			break
	elif asks == "no" or asks == "n":
		print("\u001b[31;1mExiting...\u001b[0m")
		quit()
	else:
		print("\u001b[31;1mInvalid.\u001b[31mPlease try again.\u001b[0m")
		ask()
			
try:
	process()
	ask()
	
except KeyboardInterrupt:
	print("\n^C. \u001b[31;1m\nExitng...\u001b[0m")

except ValueError:
	print("\u001b[31mInvalid Values Passed.")
	print("\u001b[31;1mERROR....\u001b[0m")
	process()
	ask()