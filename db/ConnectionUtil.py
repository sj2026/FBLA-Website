import os
import sqlite3
#from cryptography.fernet import Fernet 

def getConnection():
    rootFolder = os. getcwd()
    connection_obj = sqlite3.connect(rootFolder + '\\FBLA Website 2024.db')
    return connection_obj

def getKey():
    #return "_4I-k9JPGDkwLN5Df9lVpQcWsJcASYDvp0pF-w80c_0="
    return ""
def encrypt(message):
    #fernet = Fernet(getKey())

    # then use the Fernet class instance 
    # to encrypt the string string must
    # be encoded to byte string before encryption
    #encMessage = fernet.encrypt(message.encode())
    #return encMessage
    return message

def decrypt(message):
    #fernet = Fernet(getKey())
    #decMessage = fernet.decrypt(message).decode()
    #return decMessage
    return message
