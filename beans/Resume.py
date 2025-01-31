from dataclasses import dataclass

@dataclass
class Resume:
    id: int = 0
    resumeName = str
    studentID = int
    pastExperience = str
    skillset = str
    summary = str
    link_edit=str = ''
    link_delete=str = ''
    
    def __str__(self):
        return f"Resume: {{id = {self.id}, resume name = {self.resumeName}, student id = {self.studentID}, past experience = {self.pastExperience}, skillset = {self.skillset}, summary = {self.summary}}}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'resumeName': self.resumeName,
            'studentID' : self.studentID,
            'pastExperience' : self.pastExperience,
            'skillset' : self.skillset,
            'summary' : self.summary,
            'link_edit' : self.link_edit,
            'link_delete' : self.link_delete,
            
        }
    