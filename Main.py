from simplecrypt import encrypt, decrypt
from pycrypto import *
from time import *
# Funtions
def ask()
	print("1 pour encripter, 2 pour decripter")
	x=int(input("Choix>"))
	if x == 1:
		encript()
	elif x == 2:
		decript()
	else:
		print("reponse inconue, sois 1 ou 2")
def encript():
	Text=str(input("Message> "))
	Clef=str(input("Clef> "))
	ciphertext = encrypt(Clef, Text)
	print(ciphertext)
def decript()
	Text=str(input("Message> "))
	Clef=str(input("Clef> "))
	plaintext = decrypt(Clef, Text)
# Start
While 1:
	ask()
	
