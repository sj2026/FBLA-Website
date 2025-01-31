from dataclasses import dataclass

#@dataclass
class Application:
    id: int = 0
    jobID: int = 0
    studentID: int = 0
    resumeID: int = 0
    status: str
    additionalDetails: str
    link_application : str = ''
    
    studentName :str = ""
    resumeName : str = ""
    
    
    def __str__(self):
        return f"Application: {{id = {self.id}, Job ID = {self.jobID}, Student ID = {self.studentID}, Resume ID = {self.resumeID}, status = {self.status}, Additional Details = {self.additionalDetails}}}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'jobID': self.jobID,
            'studentID': self.studentID,
            'resumeID': self.resumeID,
            'status' : self.status,
            'additionalDetails': self.additionalDetails,
            "link_application" : self.link_application,
            "studentName" : self.studentName,
            "resumeName" : self.resumeName
        }
    