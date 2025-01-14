import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

dash.register_page(__name__, path='/viewjobs')

dataAccess = JobDataAccess()

df = dataAccess.getJobs("All")

layout = html.Div(
    style={
        "backgroundColor": "#bec2cb", 
        "height": "100vh",  
        "padding": "10px", 
        "color": "#1a1f61", 
        "margin": "0",  
        "border": "10px double #1a1f61", 
        "overflow": "hidden",  
        "boxSizing": "border-box", 
        "fontFamily": "Garamond",  
    },
    children=[
        dcc.Dropdown(
            options=[
                {'label': 'All Jobs', 'value': 'All'},
                {'label': 'New Jobs', 'value': 'New'},
                {'label': 'Approved Jobs', 'value': 'Approved'},
                {'label': 'Denied Jobs', 'value': 'Denied'},
            ],
            value='New',
            id='dropDownMenu',
            style={
                "width": "100%",  
                "margin": "20px 0", 
            }
        ),

       
        html.Div(
            dash_table.DataTable(
                id='job-table',
                data=df.to_dict('records'), 
                columns=[
                    {"id": 'id', "name": "Job ID", 'editable': False},
                    {"id": 'title', "name": "Job Title", 'editable': False},
                    {"id": 'company', "name": "Company Name", 'editable': False},
                    {"id": 'location', "name": "Job Location", 'editable': False},
                    {"id": 'workHours', "name": "Work Hours", 'editable': False},
                    {"id": 'wageAmount', "name": "Wage Amount", 'editable': False},
                    {"id": 'description', "name": "Job Description", 'editable': False},
                    {"id": 'qualifications', "name": "Job Qualifications", 'editable': False},
                    {"id": 'benefits', "name": "Job Benefits", 'editable': False},
                    {"id": 'keywords', "name": "Job Keywords", 'editable': False},
                    {"id": 'status', "name": "User Status", 'presentation': 'dropdown', 'editable': True},
                ],
                dropdown={
                    'status': {
                        'options': [
                            {'label': "New", 'value': 'New'},
                            {'label': "Approved", 'value': 'Approved'},
                            {'label': "Denied", 'value': 'Denied'}
                        ]
                    }
                },
                sort_action="native", 
                sort_mode="single", 
                page_action="native", 
                page_current=0,
                page_size=10, 
                style_table={
                    "width": "100%",
                    "overflowX": "auto",
                    "margin": "20px 0",  
                },
                style_cell={
                    "textAlign": "center", 
                    "fontSize": "15px",  
                }
            )
        ),

        
        html.Div(id='dropdown-container-jobs'),

        
        html.Div(id='action-result', children="")
    ]
)


@callback(
    Output('action-result', 'children'),
    [Input('job-table', 'data'),
     Input('job-table', 'columns')],
    [State("job-table", "data_previous")],
    prevent_initial_call=True
)
def update_tol_db_jobs(rows, columns, prev_rows):
    if prev_rows:
        df1 = pd.DataFrame(rows)
        df2 = pd.DataFrame(prev_rows)
        diff = dataframe_difference_jobs(df1, df2)
        job = Job()
        job.status = diff.iloc[0]['status']
        job.id = diff.iloc[0]['id']
        dataAccess.updateJob(job)
    return "Job status updated successfully."


@callback(
    Output('job-table', 'data'),
    Input('dropDownMenu', "value")
)
def loadTable(value):
    df = dataAccess.getJobs(value)
    return df.to_dict('records')  


def dataframe_difference_jobs(df1: pd.DataFrame, df2: pd.DataFrame):
    """Find rows which are different between two DataFrames."""
    return pd.concat([df1, df2]).drop_duplicates(keep=False)
