import random
import datetime

upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
special_letters = ["!","@","#","$","%","^","&","*","(",")"]

letters = upper_letters + lower_letters + digits + special_letters
passwrd = []
def passwd():
	pno = int(input("Enter password length: "))    
	random.shuffle(letters)
	for i in range(pno):
		passwrd.append(random.choice(letters))
	random.shuffle(passwrd)
	c = "".join(passwrd)
	now = datetime.datetime.now()
	file = open("generated_password.txt","a")	
	file.write("\n" + c + ": " + str(now.strftime("%d/%m/%Y %H:%M:%S")))
	file.close()
	print("The password is: " + c)
	print("The generated password is also stored in `generated_password.txt` file.")

passwd()