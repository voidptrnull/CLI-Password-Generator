# Last edited on 14/06/22
import random
import datetime
import hashlib
from time import sleep
import os

os.system("")

upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
special_letters = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]"]

letters = upper_letters + lower_letters + digits + special_letters
passwrd = []

pwd = "./CLI_Password_Gen"
doesExists = os.path.exists(pwd)
if doesExists == False:
	os.mkdir("CLI_Password_Gen")
	os.chdir("./CLI_Password_Gen")
else:
	os.chdir("./CLI_Password_Gen")

def clear():
	os.system("clear")


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
	random.shuffle(letters)
	i = 1

	while i != pno:
		passwrd.append(random.choice(letters))
		i = i + 1
	
	random.shuffle(passwrd)
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
		hash_store = open("hashed_password.txt","a")
		hash_store.write("The hashes for password "+ c +" generated at "  +  " : " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S"))  + " is: \n")
		hash_store.write("	The hash in sha1 is: " + hash1 + " \n")
		hash_store.write("	The hash in sha224 is: " + hash224 + " \n")
		hash_store.write("	The hash in sha256 is: " + hash256 + " \n")
		hash_store.write("	The hash in sha384 is: " + hash384 + " \n")
		hash_store.write("	The hash in sha512 is: " + hash512 + " \n")
		hash_store.write("	The hash in sha3_224 is: " + hash3_224 + " \n")
		hash_store.write("	The hash in sha3_256 is: " + hash3_256 + " \n")
		hash_store.write("	The hash in sha3_384 is: " + hash3_384 + " \n")
		hash_store.write("	The hash in sha3_512 is: " + hash3_512 + " \n\n")
		hash_store.close()
		print("The generated hash is also stored in \u001b[37;1m./CLI_Password_Gen\hash_password.txt\u001b[0m file.")
	
		c = c.encode()
		hash1 = hashlib.sha1(c).hexdigest()
		hash224 = hashlib.sha224(c).hexdigest()
		hash256 = hashlib.sha256(c).hexdigest()
		hash384 = hashlib.sha384(c).hexdigest()
		hash512 = hashlib.sha512(c).hexdigest()	
		hash3_224 = hashlib.sha3_224(c).hexdigest()
		hash3_256 = hashlib.sha3_256(c).hexdigest()
		hash3_384 = hashlib.sha3_384(c).hexdigest()
		hash3_512 = hashlib.sha3_512(c).hexdigest()

		sleep(0.5)
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

	elif ask == "no" or ask == "n" or ask == "":
		pass
	else:
		print("\u001b[31;1mHash was not generated.\u001b[0m")
	

def ask():
	sleep(0.7)
	print("\u001b[36mDo you want to continue ? (\u001b[37;1m[Y]\u001b[0mes/\u001b[37;1m[N]o\u001b[0m\u001b[36m) :\u001b[0m ")
	asks = input("\u001b[32m> \u001b[0m")
	if asks == "yes" or asks == "ye" or asks == "y" or asks == "":
		while asks == "yes" or asks == "ye" or asks == "y" or asks == "":
			print("\u001b[32;1mContinuing...\u001b[0m")
			process()
			ask()
			clear()
			break
	elif asks == "no" or asks == "n":
		print("\u001b[31;1mExiting...\u001b[0m")
		quit()
	else:
		print("\u001b[31;1mInvalid.\u001b[31mPlease try again.\u001b[0m")
		ask()
	clear()
			
try:
	process()
	ask()
	
except KeyboardInterrupt:
	print("\n^C. \u001b[31;1m\nExitng...\u001b[0m")

except ValueError:
	print("\u001b[31mInvalid Values Passed.")
	print("\u001b[31m;1mERROR....\u001b[0m")
	process()
	ask()
