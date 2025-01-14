import dash
from dash import  Input, Output, html, State, callback
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

dash.register_page(__name__, path_template = "/jobposting/<mode>/<job_id>")

job = {
    "id": 0,
    "title" : '',
    "company" : '',
    'location' : '',
    'workHours' : '',
    'wageAmount' : '',
    'description' : '',
    'qualifications' : '',
    'benefits' : '',
    'keywords' : '',
    'status' : '',
}

def layout(mode = None, jobID = None, **kwargs):
    global screenMode
    screenMode = mode

    global resumeID
    resumeID = jobID
    
    global job
    readOnly = ''
    onlyRead = False
