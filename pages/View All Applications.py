import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.ApplicationDataAccess import ApplicationDataAccess
from beans.Job import Job
from pages import PageUtil

dash.register_page(__name__, path_template='/viewallapplications/<job_id>')

dataAccess = ApplicationDataAccess()


def layout (job_id = None):
    global jobID
    jobID = job_id
    #print(jobID)
    df = dataAccess.getJobApplications(jobID)
    if df is None:
        df = pd.DataFrame()
    layout = html.Div(
        dash_table.DataTable(
            id = 'job-view-table-employer',
            data = df.to_dict('records'), 
            columns = [
                #{"id": 'id', "name": "Job ID", 'editable' : False},
                {"id": 'link_application', "name": "Application Id", 'editable' : False, 'presentation': 'markdown'},
                {"id": 'studentName', "name": "Student Name", 'editable' : False},
                {"id": 'resumeID', "name": "Resume Id", 'editable' : False},
                {"id": 'additionalDetails', "name": "Additional Details", 'editable' : False},
                {"id": 'status', "name": "Status", 'editable' : True},
            ],
            markdown_options = {'link_target' : '_self'},
        
               style_as_list_view=True,
            style_data={
                'whiteSpace': 'normal',  
                'height': 'auto',  
                  'backgroundColor':'#bec2cb',
            },
            style_cell_conditional=[
                {'if': {'column_id': 'description'}, 'width': '30%'},
            ],
            style_table={
                'fontFamily': 'Garamond',  
                'color': '#1a1f61',  
            },
            style_header={
                'backgroundColor': '#1a1f61',  
                'color': 'white',  
                'fontWeight': 'bold', 
            },
            style_cell={
                'padding': '10px', 
                'textAlign': 'left', 
            },
        
        
        sort_action = "native",
        sort_mode = "single",
        page_action = "native",
        page_current = 0,
        page_size = 10
        ))
    return PageUtil.getContentWithTemplate("navbar_viewallapplications",layout)
    
@callback(
    Output('navbar_viewallapplications', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp,data):
    global session
    session = data
    return PageUtil.getMenu(session)
