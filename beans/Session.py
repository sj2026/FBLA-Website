from dataclasses import dataclass

@dataclass
class Session:
    id: int = 0
    userStatus = ''
    loggedIn = bool = False

    def __str__(self):
        return f"Session: {{id = {self.id}, user status = {self.userStatus}, logged in = {self.loggedIn}}}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'userStatus': self.userStatus,
            'loggedIn': self.loggedIn
        }