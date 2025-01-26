import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

dash.register_page(__name__, path_template='/viewcreations/<employerID>')

dataAccess = JobDataAccess()


def layout (employerID= None):
    #global employerID
    print(employerID)
    df = dataAccess.getEmployerJobs(employerID)
    #data = df.to_dict('records')
    print(df)
    return html.Div(
        dash_table.DataTable(
            id = 'job-view-table-employer',
            data = df.to_dict('records'), 
            columns = [
                #{"id": 'id', "name": "Job ID", 'editable' : False},
                {"id": 'link_student', "name": "View Full Job Posting", 'editable' : False, 'presentation': 'markdown'},
                {"id": 'link_application', "name": "View Applications", 'editable' : False, 'presentation': 'markdown'},
                {"id": 'company', "name": "Company Name", 'editable' : False},
                {"id": 'location', "name": "Job Location", 'editable' : False},
                {"id": 'description', "name": "Description", 'editable' : False},
                {"id": 'workHours', "name": "Work Hours", 'editable' : False},
                {"id": 'wageAmount', "name": "Wage Amount", 'editable' : False},
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


#@callback(
#    Input('session','data'),
#)
#def initial_load(data):
#    print(data)
#    global session 
##    session = data
 #   global employerID 
 #   employerID = session['id']
 #   print ("in initial load = " + str(employerID))
    