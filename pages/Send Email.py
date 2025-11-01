import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from datetime import date

from pages import PageUtil

from db.CreateEmail import CreateEmail
from db.UserDataAccess import UserDataAccess
from db.JobDataAccess import JobDataAccess


"""
This code handles sending emails to job applicants
"""
#Registers page on website (to make it visible)
dash.register_page(__name__, path_template="/sendEmail/<studentID>/<jobID>")


input_style = {
    "backgroundColor": "#FFFDF2",
    "color": "black",
    "width": "80%",
    "height": "25px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid black",
    "overflowY": "auto",
    "fontSize": "1.5vw",
}

def layout(studentID = None, jobID = None, **kwargs):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.

    Args:
        studentID: student id
        jobID : job id

    Returns: Dash HTML tags to display.
    """
    global applicantID
    applicantID = studentID

    global jobIDGlobal
    jobIDGlobal = jobID

    form = dbc.Form(
        [
            dbc.Row(
                [
                    dbc.Col([
                        html.Div("Select Interview Date:", style={'textAlign':'center', 'fontSize': '1.8vw', 'marginBottom': '10px'}),
                        html.Div(
                            dcc.DatePickerSingle(
                                id='interview-date-picker',
                                min_date_allowed=date(2025, 1, 1),
                                initial_visible_month=date(2025, 8, 15),
                                date=date(2025, 8, 15),
                                display_format='MMM Do, YY', # Example: Aug 15, 25
                                # Adjust style to control its size for centering
                                style={
                                    'width': '250px', # Give it a fixed width
                                    'height': 'auto',
                                    'fontSize': '1.5vw',
                                    'padding': '10px',
                                    'margin': 'auto' # This is key for centering a fixed-width block element
                                }
                            ),
                            style={'textAlign': 'center', 'width': '100%'} # This outer div ensures centering of its child
                        )
                    ], width=6), # Use width=6 for half the row

                    dbc.Col([
                        html.Div("Select Interview Time:", style={'textAlign':'left', 'fontSize': '1.8vw', 'marginBottom': '10px'}),
                        html.Div(
                            dmc.TimeInput(leftSection=DashIconify(icon="bi:clock"),
                                          w=200, # Set a fixed width for the TimeInput
                                          size="xl", # Make the time input larger
                                          variant="filled",
                                          radius="xl",
                                          withAsterisk=True,
                                          id = "interview_time_picker",
                            ),
                            # This outer div ensures centering of its child
                            style={"textAlign":"center", 'width': '100%'}
                        )
                    ], width=6), # Use width=6 for half the row
                ],
                className="mb-4", # Add margin bottom for spacing between rows
                align="center", # Vertically align content in the middle
            ),

            dbc.Row([
                dbc.Col(
                    dcc.Textarea(
                        id="additionalComments",
                        placeholder="Additional Comments:",
                        style={'width': '80%', 'height': '150px', 'fontSize': '1.5vw', 'padding': '15px'} # Bigger and more padding
                    ),
                    width=12, # Take full width of the row
                    className="d-flex justify-content-center" # Center the textarea
                ),
            ],
            className="mb-4" # Add margin bottom for spacing
            ),

            html.Div([
                dbc.Button(
                    "Send Email",
                    id="sendEmail_button",
                    className="button",
                    n_clicks=0,
                    style={
                        "backgroundColor": "#0F9AE6",
                        "color": "white",
                        "padding": "15px 30px", # Increase padding for a bigger button
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "fontSize": "1.8vw", # Increase font size for the button
                    },
                ),

                dbc.Alert(
                    "Email Successfully Sent!",
                    id="emailSent_alert",
                    dismissable=True,
                    fade=True,
                    is_open=False,
                    color="success", # Make the alert green for success
                    style={"marginTop": "20px", "fontSize": "1.5vw"} # Style the alert
                ),
            ],
            style={"textAlign": "center"}
            ),
        ],
        className="mb-3",
    )

    layout = html.Div(
        children = [
            html.H2("Select Interview Specifics", style={"color": "black", "fontSize": "3vw", 'textAlign' : "center", 'marginBottom': '40px'}),
            html.Div(
                children=form,
                style={'maxWidth': '900px', 'margin': 'auto', 'padding': '20px', 'border': '1px solid #eee', 'borderRadius': '8px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)'} # Add a container style
            ),
        ]
    )

    return PageUtil.getContentWithTemplate("navbar_sendEmail",layout)




@callback(
    Output('emailSent_alert', 'is_open'),
    Input("sendEmail_button", "n_clicks"),
    State("interview-date-picker", "date"),
    State("interview_time_picker", 'value'),
    State('additionalComments', 'value'),
    prevent_initial_call=True,
)
def sendEmail(n_clicks, datePicked, timePicked, additionalComments):

    """
    Sends email to the job applicant.
    Setups the zoom meeting for the given date and time

    """
    #print("Date picked: " + datePicked)
    #print("Time picked: " + timePicked)

    userAccess = UserDataAccess()
    jobAccess = JobDataAccess()
    createEmail = CreateEmail()

    userData = userAccess.getUserById(applicantID)
    jobData = jobAccess.getJob(jobIDGlobal)

    createEmail.sendStudentEmail(userData.firstName, 'sanjayjagadeesh2021@gmail.com', jobData.title, str(datePicked), str(timePicked), str(additionalComments))
    #userData['email']

    return True

@callback(
    Output('navbar_sendEmail', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp,data):
    """
    Handles the intial load of the page.

    Args:
        data : session data.
    
    Returns: 
        a) Value for Resume drop down
        b) Menu to be displayed based on the session data. 
    
    """
    session = data
    return PageUtil.getMenu(session)