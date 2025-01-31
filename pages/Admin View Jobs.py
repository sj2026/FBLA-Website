import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.JobDataAccess import JobDataAccess
from beans.Job import Job
from pages import PageUtil

dash.register_page(__name__, path='/viewjobs')

dataAccess = JobDataAccess()

df = dataAccess.getJobs("All")

def layout(**kwargs):
    layout = html.Div(
        style={
            "backgroundColor": "#bec2cb", 
            "height": "80vh",  
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
                  #style_as_list_view=True,
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
                )
            ),

            
            html.Div(id='dropdown-container-jobs'),

            
            html.Div(id='action-result', children="")
        ]
    )
    return PageUtil.getContentWithTemplate("navbar_adminviewjobs",layout)


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
        return ""
    return ""


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

@callback(
    Output('navbar_adminviewjobs', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp,data):
    global session
    session = data
    return PageUtil.getMenu(session)


