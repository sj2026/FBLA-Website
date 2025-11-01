import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
import plotly.graph_objects as go
from db.ApplicationDataAccess import ApplicationDataAccess
from beans.Job import Job
from beans.Application import Application
from pages import PageUtil

"""
This code handles listing all applications for the given job id.
"""
dash.register_page(__name__, path_template='/viewallapplications/<job_id>')

dataAccess = ApplicationDataAccess()


def layout (job_id = None):
    """
    Retrieves the application for the jobs
    Displays the bar chart based on application status and lists the applications in a table.
    Embeds the content inside the template for the website.

     Args:
        job id: job id

    Returns: Dash HTML tags to display.
    """
    global jobID
    jobID = job_id
    #print(jobID)
    
    dfChart = dataAccess.getApplicationChartData(jobID)
    chartColors = ["red", "orange", "yellow", "green", "blue", "purple"]
    fig = go.Figure(data=[go.Bar(x = dfChart["Application Status"], y = dfChart['Number of Applicants'], marker_color = chartColors)])
    fig.layout.plot_bgcolor = "#FFFDF2"
    fig.layout.paper_bgcolor = "#FFFDF2"
    fig.update_layout(title = 'Number of Applicants at each Status', xaxis = {'title': 'Application Status'}, yaxis = {'title':'Number of Applicants'})
    
    df = dataAccess.getJobApplications(jobID,None)
    if df is None:
        df = pd.DataFrame()
    layout = html.Div(
        children = [
            dcc.Graph(figure = fig, style = {'width': '100%', 'height': "350px"}),
            dcc.Dropdown(
                options=[
                    {'label': 'All Applications', 'value': 'All'},
                    {'label': 'New Applications', 'value': 'New'},
                    {'label': 'Screened Applications', 'value': 'Screened'},
                    {'label': 'Interview 1', 'value': 'Interview #1'},
                    {'label': 'Interview 2', 'value': 'Interview #2'},
                    {'label': 'Accepted', 'value': 'Accepted'},
                    {'label': 'Rejected', 'value': 'Rejected'},
                ],
                value='New',
                id='dropDownMenu-allApplications',
                style={
                    "width": "100%",  
                    "margin": "20px 0", 
                }),
        
        dash_table.DataTable(
            id = 'job-view-table-employer',
            data = df.to_dict('records'), 
            columns = [
                #{"id": 'id', "name": "Job ID", 'editable' : False},
                {"id": 'link_application', "name": "Application Id", 'editable' : False, 'presentation': 'markdown'},
                {"id": 'studentName', "name": "Student Name", 'editable' : False},
                {"id": 'resumeID', "name": "Resume ID", 'editable' : False},
                {"id": 'additionalDetails', "name": "Additional Details", 'editable' : False},
                {"id": 'status', "name": "Status", 'presentation': 'dropdown','editable' : True},
                {"id": 'InterviewInvite', "name": "Invite For interview", 'editable': False, 'presentation': 'markdown'},
            ],
            markdown_options = {'link_target' : '_self'},
            dropdown={
                        'status': {
                            'options': [
                                {'label': "New", 'value': 'New'},
                                {'label': "Screened", 'value': 'Screened'},
                                {'label': "Interview 1", 'value': 'Interview #1'},
                                {'label': "Interview 2", 'value': 'Interview #2'},
                                {'label': "Accepted", 'value': 'Accepted'},
                                {'label': "Rejected", 'value': 'Rejected'}
                            ]
                        }
                    },
            
        
            style_as_list_view=True,
            style_data={
                'whiteSpace': 'normal',  
                'height': 'auto',  
                  'backgroundColor':'#FFFDF2',
            },
            style_data_conditional=[
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
            },
            
        
        
        sort_action = "native",
        sort_mode = "single",
        page_action = "native",
        page_current = 0,
        page_size = 10,
        
        ),
        html.Div(id='dropdown-container-allApplications'),

            
        html.Div(id='action-result-allApplications', children="")
        ]
        )
        
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

@callback(
    Output('action-result-allApplications', 'children'),
    [Input('job-view-table-employer', 'data'),
     Input('job-view-table-employer', 'columns')],
    [State("job-view-table-employer", "data_previous")],
    prevent_initial_call=True
)
def update_tol_db_allApplications(rows, columns, prev_rows):
    """
    Updates the application data in the database if the row is changed.

    Args:
        rows : rows in the data table.
        columns: columns in the data table.
        prev_rows: row data before edit.
    """
    if prev_rows:
        df1 = pd.DataFrame(rows)
        df2 = pd.DataFrame(prev_rows)
        diff = dataframe_difference_jobs(df1, df2)
        application = Application()
        application.status = diff.iloc[0]['status']
        application.id = diff.iloc[0]['id']
        dataAccess.updateApplicationStatus(application)
        return ""
    return ""

def dataframe_difference_jobs(df1: pd.DataFrame, df2: pd.DataFrame):
    """Find rows which are different between two DataFrames."""
    return pd.concat([df1, df2]).drop_duplicates(keep=False)

@callback(
    Output('job-view-table-employer', 'data'),
    Input('dropDownMenu-allApplications', "value")
)
def loadTable(value):

    """
    Handles loading of dash table based on filter dropdown

    Args:
        value : job Status.
    
    Returns: Dictionary of applications
    
    """

    df = dataAccess.getJobApplications(jobID,value)
    #print(df)
    return df.to_dict('records')  

