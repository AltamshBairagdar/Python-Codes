import hashlib
import random
import time

print("\t\t********************************")
print("\t\t*  PASSWORD MANAGER IN PYTHON  *")
print("\t\t********************************")


print("\nMade by - Altamsh Bairagdar")
print("E-mail Id - bairagdaraltamsh@gmail.com")
print("****************************************")


time.sleep(3)
print("\n1.String To Hash Converter\n2.Password Strength Checker\n3.Random Password Genrator\n4.Guess Password")


userinput = int(input("\n>Enter Your Choice : "))


def fun1():
	print("------------------------------------")
	print("\n1] String To Hash Converter \n")

	a = input(">Enter Your String : ")
	print("Processing......")
	time.sleep(3)

	c = hashlib.md5(a.encode())
	g = c.hexdigest()
	print("\nMD5 Value : "+g)

	c = hashlib.sha1(a.encode())
	g = c.hexdigest()
	print("\nSHA1 Value : "+g)


def fun2():
	print("------------------------------------")
	print("\n2] Password Strength Checker\n")

	print("*Disclamair : Password must be contains Uppercase, Lowercase, Special \n Symbols, Digits and Greater than 8 Characters \n")
	password = input(">Enter Your password : ")

	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	special = "(){}[]\|:;,.<>?/!@#%^&*-+=_"
	digits = "0123456789"

	length=len(password)

	all = upper_case + lower_case + special + digits

	if length <= 8 or password == all:
		print("password is not Strong & not Contains all things ! ")
		print("Try Again !")

	else:
		print("\nPassword is Strong :" +password)

def fun3():

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	Symbol = "(){}[]\<>?/!@#%^&*_"

	all = lower + upper + digits + Symbol
	length = 15

	print("------------------------------------")
	print("\n3] Random Password Genrator\n")

	print("Genrating password.....")
	time.sleep(3)

	password = "".join(random.sample(all,length))
	print("Random password is : "+password)


def fun4():
	
	print("\n4] Guess Password\n")

	name = input(">Enter Any Name ,Target Name (no commas) :")
	pet_name = input(">Enter Any Pet Name (no commas) :")
	nick_name = input(">Enter Any Nick Name , Fav movies, Organization :")
	birth_Date = input(">Enter Any Birth Date (dd/mm/yy) :")
	email_id = input(">Enter Any Email_Id Related To Target :")
	old_password = input(">Enter Any Old Password :")
	pass_length = int(input(">Enter Any Password length :"))

	guess = name + pet_name + nick_name + birth_Date + email_id + old_password

	length = pass_length

	r1 = "".join(random.sample(guess,length))

	print("\nGuessed Password Is :" + r1)
	
##########################################################

if userinput == 1:
	fun1()

if userinput == 2:
	fun2()

if userinput == 3:
	fun3()

if userinput == 4:
	fun4()