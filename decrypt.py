inding files in the directory
import os

#for encrypting files in the dirctory
from cryptography.fernet import Fernet



phrase="iwatani"

uphrase=input("Enter Phrase\n")

if uphrase == phrase:

	with open("fkey","rb") as fkey:
		seckey=fkey.read()


	files=[]

	for file in  os.listdir():
		if file =="naofumi.py" or file =="fkey" or file == "decrypt.py" :
			continue
		if os.path.isfile(file):
			files.append(file)
	print(files)

	for file in files:
		with open(file,"rb") as ofile:
			info=ofile.read()
		info_decry=Fernet(seckey).decrypt(info)
		with open(file,"wb") as ofile:
			ofile.write(info_decry)
	print("Decrypted")
else:
	print("????????????") 
