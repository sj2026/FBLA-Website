from dataclasses import dataclass

@dataclass
class Session:
    id: int = 0
    userStatus = ''
    loggedIn = bool = False
    textSize = 22
    textColor = "black"
    backgroundColor = "#FFFDF2"

    def __str__(self):
        return f"Session: {{id = {self.id}, user status = {self.userStatus}, logged in = {self.loggedIn}, text size = {self.textSize}, text color = {self.textColor}, background color = {self.backgroundColor}}}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'userStatus': self.userStatus,
            'loggedIn': self.loggedIn,
            'textSize': self.textSize,
            'textColor': self.textColor,
            'backgroundColor': self.backgroundColor
        }