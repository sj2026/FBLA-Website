import json
import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback, callback_context
from dash.dependencies import MATCH, ALL
import pandas as pd
from db.Searcher import Searcher
from beans.Job import Job
from pages import PageUtil
import dash_bootstrap_components as dbc
import urllib.parse

"""
This code handles listing job posting based on the search term.
"""
dash.register_page(__name__, path_template='/viewposting/<searchTerm>')

dataAccess = Searcher()

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
        button_id = {'type': 'view-details-button', 'index': row['id']}

        return dbc.Card(
            [
                dbc.CardImg(src= row['jobPicture'], top=True),
                dbc.CardBody(
                    [
                        html.H3(row['title'], className="card-title", style = {'color': "red"}),
                        html.H4("Description: " + trim_to_words(row['description'],30) + "...\n", className="card-text"),
                        dbc.Button("View Details", id = button_id, color="primary", n_clicks=0),
                    ]
                ),
            ],
            style={"width": "30rem", "margin": "7px", 'backgroundColor': "#ADD8E6"},
        )


def layout(searchTerm = None):
    """
    Searches the job posting based on search term.
    Embeds the content inside the template for the website.

     Args:
        searchTerm: search term.

    Returns: Dash HTML tags to display.
    """
    cards = []
    if searchTerm:
        df = dataAccess.search(searchTerm)
        if not df.empty:
            df = df.drop(['keywords'], axis=1)
            cards = [create_card(row) for index, row in df.iterrows()]

    
        layout = html.Div(children=cards, style={'display': 'flex', 'flex-wrap': 'wrap'})

        return PageUtil.getContentWithTemplate("navbar_viewpostingsUpdated", layout)

@callback(
    Output('navbar_viewpostingsUpdated', 'children'),
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
    Input({'type': 'view-details-button', 'index': ALL}, 'n_clicks'), # Input: n_clicks from ALL buttons of this type
    prevent_initial_call=True # Prevents the callback from firing when the app first loads
)
def handle_button_click(n_clicks_list):
    """
    Handles button clicks for the Job search result page.
    On click, navigates to the job details page for the student.
    
    """
    if any(element != 0 for element in n_clicks_list):
        
        triggered_id_str = callback_context.triggered[0]['prop_id'].split('.')[0]
        decoded_string = urllib.parse.unquote(triggered_id_str)
        data_dict = json.loads(decoded_string)
        index_value = data_dict.get('index')
        
        pathname ="/job/view_as_student/" + str(index_value) #redirects to homepage
        return pathname
