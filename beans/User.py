from dataclasses import dataclass

@dataclass
class User:
    id: int = 0
    firstName = str
    lastName = str
    email = str
    phoneNumber = str
    isAdmin = str
    status = str
    username = str = ''
    password = str
    
    def __str__(self):
        return f"User: {{id = {self.id}, firstName = {self.firstName}, lastName = {self.lastName}, email = {self.email}, phone number = {self.phoneNumber}, is admin = {self.isAdmin}, status = {self.status}, password = {self.password}, username = {self.username}}}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName' : self.lastName,
            'email' : self.email,
            'phoneNumber' : self.phoneNumber,
            'isAdmin' : self.isAdmin,
            'status' : self.status,
            'password' : self.password,
            'username' : self.username
        }
    