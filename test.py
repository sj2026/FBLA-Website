from cryptography.fernet import Fernet
from db import ConnectionUtil
from db.Searcher import Searcher

message = "hello"

#key = Fernet.generate_key()

#encMessage = ConnectionUtil.encrypt(message)

#print(encMessage)

#decMessage = ConnectionUtil.decrypt(encMessage)

#print(decMessage)

searcher = Searcher()

print(searcher.search("ceo"))