import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import flask

import pandas as pd

from beans.User import User
from db.ResumeDataAccess import ResumeDataAccess
from db.UserDataAccess import UserDataAccess
from pages import PageUtil

#user_data = {
#    'firstName': ''
#}

dash.register_page(__name__, path_template='/profile/<profile_id>')

def layout(profile_id = None,**kwargs):
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
                                            style={
                                                "backgroundColor": "#bec2cb",
                                                "color": "#1a1f61",
                                                "borderColor": "#1a1f61",
                                                "fontSize": "1.5vw",  
                                            },
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
                                            style={
                                                "backgroundColor": "#bec2cb",
                                                "color": "#1a1f61",
                                                "borderColor": "#1a1f61",
                                                "fontSize": "1.5vw",  
                                            },
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
                                            style={
                                                "backgroundColor": "#bec2cb",
                                                "color": "#1a1f61",
                                                "borderColor": "#1a1f61",
                                                "fontSize": "1.5vw", 
                                            },
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
                                            style={
                                                "backgroundColor": "#bec2cb",
                                                "color": "#1a1f61",
                                                "borderColor": "#1a1f61",
                                                "fontSize": "1.5vw", 
                                            },
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
                                        "backgroundColor": "#1a1f61",
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
    global session
    session = data
    return PageUtil.getMenu(session)
            
