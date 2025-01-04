import os
import sqlite3

def getConnection():
    rootFolder = os. getcwd()
    connection_obj = sqlite3.connect(rootFolder + '\\FBLA Website 2024.db')
    return connection_obj
