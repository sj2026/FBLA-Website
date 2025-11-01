import json
import dash
from dash import ALL, Dash, callback_context, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.JobDataAccess import JobDataAccess
from beans.Job import Job
from pages import PageUtil
import dash_bootstrap_components as dbc
import urllib.parse

"""
This code handles viewing job postings for the employer.
"""
dash.register_page(__name__, path_template='/viewcreations/<employerID>')
dataAccess = JobDataAccess()

def trim_to_words(text, num_words):
    """
    Trims a string to a specified number of words.

    Args:
        text (str): The input string.
        num_words (int): The desired number of words to keep.

    Returns:
        str: The trimmed string.
    """
    words = text.split()
    trimmed_words = words[:num_words]
    return ' '.join(trimmed_words)


def create_card(row):
        """
        Creates a dash card component for the given job details.

        Args:
            row: job details. 

        Returns: Dash Card tag to display.
        """
        button_details_id = {'type': 'view-details-button', 'index': row['id']}
        button_application_id = {'type': 'view-application-button', 'index': row['id']}

        return dbc.Card(
            [
                dbc.CardImg(src= row['jobPicture'], top=True),
                dbc.CardBody(
                    [
                        html.H3(row['title'], className="card-title", style = {'color': "red"}),
                        html.H4("Description: " + trim_to_words(row['description'],30) + "...\n", className="card-text"),
                        dbc.Button(
                        "View Details",
                        id=button_details_id,
                        color="primary",
                        n_clicks=0,
                        style={'margin-right': '10px'} # Add space to the right
                        ),
                        dbc.Button(
                            "View Applications",
                            id=button_application_id,
                            color="primary",
                            n_clicks=0
                        ),
                    ]
                ),
            ],
            style={"width": "30rem", "margin": "7px", 'backgroundColor': "#ADD8E6"},
        )


def layout(employerID = None):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.

     Args:
        employerID: Employer Id. 

    Returns: Dash HTML tags to display.
    """
    cards = []
    
    #print(employerID)
    df = dataAccess.getEmployerJobs(employerID)
    
    if not df.empty:
        cards = [create_card(row) for index, row in df.iterrows()]

    
        layout = html.Div(children=cards, style={'display': 'flex', 'flex-wrap': 'wrap'})

        return PageUtil.getContentWithTemplate("navbar_employerViewPostings", layout)

@callback(
    Output('navbar_employerViewPostings', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp, data):
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


@callback(
    Output('url', 'pathname',allow_duplicate=True),
    Input({'type': 'view-details-button', 'index': ALL}, 'n_clicks'),
    Input({'type': 'view-application-button', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def handle_button_clicks(details_n_clicks_list, application_n_clicks_list):
    """
    Handles button clicks for the Job postings.
    If the click event/trigger is from view details button, then navigate to view job page.
    If the click event/trigger is from view application button, then navigate to view all application page.
    
    """
    triggered_id = callback_context.triggered[0]['prop_id']
    if (any(element != 0 for element in details_n_clicks_list) or any(element != 0 for element in application_n_clicks_list)):        
        
        if 'view-details-button' in triggered_id:
            decoded_string = urllib.parse.unquote(triggered_id.split('.')[0])
            data_dict = json.loads(decoded_string)
            index_value = data_dict.get('index')
            return "/job/view/" + str(index_value)
        elif 'view-application-button' in triggered_id:
            decoded_string = urllib.parse.unquote(triggered_id.split('.')[0])
            data_dict = json.loads(decoded_string)
            index_value = data_dict.get('index')
            return "/viewallapplications/" + str(index_value)
    
    return dash.no_update # In case no relevant button was clicked
