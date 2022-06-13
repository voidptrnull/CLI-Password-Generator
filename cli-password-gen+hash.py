# Last edited on 12/06/22
import random
import datetime
import hashlib
from time import sleep
import os

# source of alphabets
upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
special_letters = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]"]

letters = upper_letters + lower_letters + digits + special_letters

passwrd = []

try:
	def process():
		
		pno = str(input("Enter password length: "))    
		random.shuffle(letters)
	
		if pno == "" or pno != int(pno):
			pno = 16

		pno = int(pno)

		# Proccess the password
		for i in range(pno):
			# Append the password in the list
			passwrd.append(random.choice(letters))
		random.shuffle(passwrd)
		c = "".join(passwrd)

		# asking the user for easier understanding
		usecase = str(input("Enter your password use-case incase you forget it. (Optional) : "))
		ask = input("Do you want to hash it and view the hashed password (sha) ? ([Y]es/[N]o): ").lower()

		m = c
		## Start the hasing process
		
		
		if ask == "yes" or ask == "ye" or ask == "y":
			generation_time = datetime.datetime.now()
			pwd = "./CLI_Password_Gen"
			doesExists = os.path.exists(pwd)
			if doesExists == False:
				os.mkdir("CLI_Password_Gen")
				os.chdir("./CLI_Password_Gen")
			else:
				os.chdir("./CLI_Password_Gen")
	
			# open the file to log the password
			file = open("generated_password.txt","a")
			if usecase == "":	
				file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
			else:
				file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "-" + usecase + "\n")	
			file.close()

			print("The password is: " + c)
			print("The generated password is also stored in `generated_password.txt` file.")
			
			# encode the password in binary
			c = c.encode()

			# proccess the hash
			hash1 = hashlib.sha1(c).hexdigest()
			hash224 = hashlib.sha224(c).hexdigest()
			hash256 = hashlib.sha256(c).hexdigest()
			hash384 = hashlib.sha384(c).hexdigest()
			hash512 = hashlib.sha512(c).hexdigest()
		
			hash3_224 = hashlib.sha3_224(c).hexdigest()
			hash3_256 = hashlib.sha3_256(c).hexdigest()
			hash3_384 = hashlib.sha3_384(c).hexdigest()
			hash3_512 = hashlib.sha3_512(c).hexdigest()

			
			sleep(1)
			print("The hashed password in sha1 is: " + hash1)
			print("The hashed password in sha224 is: " + hash224)
			print("The hashed password in sha256 is: " + hash256)
			print("The hashed password in sha384 is: " + hash384)
			print("The hashed password in sha512 is: " + hash512)
			print("The hashed password in sha3_224 is: " + hash3_224)
			print("The hashed password in sha3_256 is: " + hash3_256)
			print("The hashed password in sha3_384 is: " + hash3_384)
			print("The hashed password in sha3_512 is: " + hash3_512)

			# convert hex to string
			hash1 = str(hash1)
			hash224 = str(hash224)
			hash256 = str(hash256)
			hash384 = str(hash384)
			hash512 = str(hash512)
			hash3_224 = str(hash3_224)
			hash3_256 = str(hash3_256)
			hash3_384 = str(hash3_384)
			hash3_512 = str(hash3_512)

			# Write it in the file
			hash_store = open("hashed_password.txt","a")
			hash_store.write("The hashes for password "+ m +" generated at "  +  " : " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S"))  + " is: \n")
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
			print("The generated hash is also stored in `hash_password.txt` file.")
		elif ask == "no" or ask == "n" or ask == "":
			generation_time = datetime.datetime.now()
			pwd = "./CLI_Password_Gen"
			doesExists = os.path.exists(pwd)
			if doesExists == False:
				os.mkdir("CLI_Password_Gen")
				os.chdir("./CLI_Password_Gen")
			else:
				os.chdir("./CLI_Password_Gen")

			# open the file to log the password
			file = open("generated_password.txt","a")
			if usecase == "":	
				file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
			else:
				file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "-" + usecase + "\n")	
			file.close()

			print("The password is: " + c)
			print("The generated password is also stored in `generated_password.txt` file.")
				
	def ask():	
		asks = input("Do you want to continue ? ([Y]es/[N]o) : ")
		if asks == "yes" or asks == "ye" or asks == "y" or asks == "":
			while asks == "yes" or asks == "ye" or asks == "y" or asks == "":
				process()
				ask()
				break
		elif asks == "no" or asks == "n":
			print("Exiting...")
			quit()
		else:
			print("Invalid. Please try again.")
			ask()
	
	process()
	ask()

except KeyboardInterrupt:
		print("\n Shutdown requested...Goodbye...")
except ValueError:
		print("Continuing with default values...")
