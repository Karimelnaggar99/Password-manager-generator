from cryptography.fernet import Fernet
import os
from pwd_generator import *
 #Generate key in file once
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file: #write in bytes
        key_file.write(key)

if not os.path.exists("key.key"):
    write_key()

def load_key():
    file=open("key.key","rb")
    key = file.read()
    file.close
    return key



key=load_key() 
fer=Fernet(key)




def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw = data.split("|")
            print("Account Name: ",user,", Password: ",fer.decrypt(passw.encode()).decode())


def add():
    name=input("Account Name:")
    generate=input("Do you want a generated password?(y/n) ").lower() =='y'
    if generate:
        pwd=generate_password()
        print("The generated password is: ",pwd)
    else:
        pwd=input("Password: ")
    
    with open("passwords.txt",'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones?[view/add], press Q to quit: ").lower()
    if mode =="q":
        quit()

    if mode =="view":
        view()
    elif mode =="add":
        add()
    else:
        print("Invalid mode")
        continue
    
