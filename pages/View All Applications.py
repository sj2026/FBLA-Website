import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.ApplicationDataAccess import ApplicationDataAccess
from beans.Job import Job

dash.register_page(__name__, path_template='/viewallapplications/jobID')

dataAccess = ApplicationDataAccess()


def layout (jobid = None):
    global jobID
    jobID = jobid
    df = dataAccess.getJobApplications(jobID)
    return html.Div(
        dash_table.DataTable(
            id = 'job-view-table-employer',
            data = df.to_dict('records'), 
            columns = [
                #{"id": 'id', "name": "Job ID", 'editable' : False},
                {"id": 'link_application', "name": "View Application", 'editable' : False, 'presentation': 'markdown'},
                {"id": 'studentID', "name": "Company Name", 'editable' : False},
                {"id": 'resumeID', "name": "Job Location", 'editable' : False},
                {"id": 'additionalDetails', "name": "Description", 'editable' : False},
                {"id": 'status', "name": "Work Hours", 'editable' : True},
            ],

        
            style_as_list_view=True,
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
             },
            style_cell_conditional=[
            {'if': {'column_id': 'description'},
            'width': '30%'}
            ],
        
        
        sort_action = "native",
        sort_mode = "single",
        page_action = "native",
        page_current = 0,
        page_size = 10
        ))
