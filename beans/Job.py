from dataclasses import dataclass

@dataclass
class Job:
    id: int = 0
    title = str
    company = str
    location = str
    workHours = str
    wageAmount = str
    description = str
    qualifications = str
    benefits = str
    keywords = str
    status = str
    link_student = str = ''
    link_applications = str = ''
    link = str
    employerID = 0
    
    def __str__(self):
        return f"Job: {{id = {self.id}, title = {self.title}, company = {self.company}, location = {self.location}, work hours = {self.workHours}, wage amount = {self.wageAmount}, description = {self.description}, qualifications = {self.qualifications}, benefits = {self.benefits}, keywords = {self.keywords}, status = {self.status}}}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company' : self.company,
            'location' : self.location,
            'workHours' : self.workHours,
            'wageAmount' : self.wageAmount,
            'description' : self.description,
            'qualifications' : self.qualifications,
            'benefits' : self.benefits,
            'keywords' : self.keywords,
            'status' : self.status,
            'link' : self.link,
            'link_student' : self.link_student,
            'link_applications' : self.link_applications,
            'employerID': self.employerID
        }
    