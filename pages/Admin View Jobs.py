import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.JobDataAccess import JobDataAccess
from beans.Job import Job
from pages import PageUtil

"""
This code handles viewing jobs for administrator
"""

dash.register_page(__name__, path='/viewjobs')

#Load all the jobs from the database
dataAccess = JobDataAccess()
df = dataAccess.getJobs("All")

def layout(**kwargs):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.

    Returns: Dash HTML tags to display.
    """
    layout = html.Div(
        style={
            "backgroundColor": "#FFFDF2", 
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
                        #{"id": 'description', "name": "Job Description", 'editable': False},
                        #{"id": 'qualifications', "name": "Job Qualifications", 'editable': False},
                        #{"id": 'benefits', "name": "Job Benefits", 'editable': False},
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
                    style_as_list_view=True,
            style_data={
                'whiteSpace': 'normal',  
                'max-height': '100px',  
                'overflow-wrap' : 'break-word',
                'backgroundColor':'#FFFDF2',
            },
            style_cell_conditional=[
                {'if': {'column_id': 'status'}, 
                        'height': '68px',  # Adjust this value until the border aligns
                        'minHeight': '38px', # 
                        'paddingTop': '0px', # Often dropdowns need less top/bottom padding
                        'paddingBottom': '0px',
                        #'verticalAlign': 'middle', # Ensures content is vertically centered
                 },
            ],
            style_table={
                'fontFamily': 'Garamond',  
                'color': 'black',  
            },
            style_header={
                'backgroundColor': 'black',  
                'color': '#FFFDF2',  
                'fontWeight': 'bold', 
            },
            style_cell={
                'padding': '10px', 
                'textAlign': 'left', 
                #'overflow': 'hidden',
                #'textOverflow': 'ellipsis',
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
    """
    Updates the job data in the database if the row is changed.

    Args:
        rows : rows in the data table.
        columns: columns in the data table.
        prev_rows: row data before edit.
    """
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
    """
    Loads the job data from the database.

    Args:
        value : filter value.
    
    Returns: dictionary of the Job records.
    
    """
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
    """
    Handles the intial load of the page.

    Args:
        data : session data.
    
    Returns: Menu to be displayed based on the session data. 
    E.g. The student menu for a student.
    
    """

    global session
    session = data
    return PageUtil.getMenu(session)


