import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import flask

import pandas as pd

from beans.User import User
from db.ResumeDataAccess import ResumeDataAccess
from db.UserDataAccess import UserDataAccess
from pages import PageUtil

"""
This code handles profile for the logged in user
"""

# Standard input style
input_style = {
    "backgroundColor": "white",
    "color": "black",
    "width": "100%",
    "height": "30px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid black",
    "overflowY": "auto",
    "fontSize": "1.5vw",  
}


dash.register_page(__name__, path_template='/profile/<profile_id>')

def layout(profile_id = None,**kwargs):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.
    Args:
        profile_id : profile id for the logged in user

    Returns: Dash HTML tags to display.
    """
    user_data = {
            'firstName': '',
            'lastName' : '',
            'email' : '',
            'phoneNumber' : ''
    }
    resumes = pd.DataFrame()
    if profile_id is not None:
        userAccess = UserDataAccess()
        user = userAccess.getUserById(profile_id)
        if user:
            user_data['firstName'] = user.firstName
            user_data['lastName'] = user.lastName
            user_data['email'] = user.email
            user_data['phoneNumber'] = user.phoneNumber
            
            #Get the resumes 
            resumeAccess = ResumeDataAccess()
            resumes = resumeAccess.getResumes(profile_id,"dataframe")
    
    layout = html.Div(
        children=[
            
            
            html.Div(
                
                style={
                            "textAlign": "center",
                            "margin": "20px auto",
                            "width": "95%",
                            "backgroundColor": "none",
                            "height": "100vh",
                            "overflowY": "none",
                            "padding": "20px",
                            "boxSizing": "border-box",

                        },
                children=[
                    html.H2("Your Profile", style={"textAlign": "center", "fontSize": "3vw"}),
                    dbc.Form(
                        [
                            dbc.Row(
                                [
                                    dbc.Label("First Name", width=3, style={"fontSize": "1.5vw"}),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text",
                                            id="name-input",
                                            placeholder="Enter your first name",
                                            value=user_data['firstName'],  # fill with user data
                                            style=input_style,
                                        ),
                                        width=8,
                                    ),
                                ],
                                className="mb-3",
                            ),
                            
                            dbc.Row(
                                [
                                    dbc.Label("Last Name", width=3, style={"fontSize": "1.5vw"}),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text",
                                            id="name-input",
                                            placeholder="Enter your last name",
                                            value=user_data['lastName'],  # fill with user data
                                            style=input_style,
                                        ),
                                        width=8,
                                    ),
                                ],
                                className="mb-3",
                            ),
                            dbc.Row(
                                [
                                    dbc.Label("Email", width=3, style={"fontSize": "1.5vw"}),
                                    dbc.Col(
                                        dbc.Input(
                                            type="email",
                                            id="email-input",
                                            placeholder="Enter your email",
                                            value=user_data['email'],  # fill with user data
                                            style=input_style,
                                        ),
                                        width=8,
                                    ),
                                ],
                                className="mb-3",
                            ),
                            
                            dbc.Row(
                                [
                                    dbc.Label("Phone Number", width=3, style={"fontSize": "1.5vw"}),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text",
                                            id="phone-input",
                                            placeholder="Enter your phone number",
                                            value=user_data['phoneNumber'],  # fill with user data
                                            style=input_style
                                        ),
                                        width=8,
                                    ),
                                ],
                                className="mb-3",
                            ),
                            
                            html.Div(
                                dbc.Button(
                                    "Save Profile",
                                    id="save-profile-btn",
                                    className="button",
                                    n_clicks=0,
                                    style={
                                        "backgroundColor": "#0F9AE6",
                                        "color": "white",
                                        "fontSize": "1.5vw",  
                                    },
                                ),
                                style={"textAlign": "center", "marginTop": "20px"},
                            ),
                            
                            html.Div(
                                style = {
                                    "paddingTop": "0.5%"
                                },
                                children = [
                                dbc.Label("Resumes", width=10, style={"fontSize": "1.5vw"}),
                                dash_table.DataTable(
                                    id = 'resume-table',
                                    data = resumes.to_dict('records'), 
                                    columns = [
                                        
                                        {"id": 'link_edit', "name": "Edit", 'editable' : False, 'presentation': 'markdown'},
                        
                                        {"id": 'resumeName', "name": "Resume Name", 'editable' : False},
                                    
                                    ],

                                    markdown_options = {'link_target' : '_self'},
                                    style_as_list_view=True,
                                    

            style_data={
                'whiteSpace': 'normal',  
                'height': 'auto',  
                  'backgroundColor':'white',
            },
            style_cell_conditional=[
                {'if': {'column_id': 'description'}, 'width': '30%'},
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
                'textAlign': 'center',
                "fontSize":'1.2vw' 
            },

                                sort_action = "native",
                                sort_mode = "single",
                                page_action = "native",
                                page_current = 0,
                                page_size = 10
                                )
                                ]
                            )
                        
                            
                            
                        ]
                    )
                ]
            )
        ],
    )
    return PageUtil.getContentWithTemplate("navbar_profile",layout)


@callback(
    Output('navbar_profile', 'children'),
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
            
