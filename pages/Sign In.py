import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User
from db import ConnectionUtil
from beans.Session import Session

"""
This code handles sign-in.
"""

#Registers page on website (to make it visible)
dash.register_page(__name__, path="/signin")

# Styling for all input boxes
input_style = {
    "backgroundColor": "#FFFDF2", # Sets background color
    "color": "black", # Sets input box color
    "width": "80%", #Sets width of input box
    "height": "30px", #Sets height of input box
    "borderRadius": "5px", #Sets the border of the input box
    "padding": "5px", #Adds padding between input boxes
    "border": "1px solid black", #Sets thickness and color or border
    "overflowY": "auto", #Manages text overflow
    "fontSize": "1.5vw",  #Text font size
}

#UI
layout = html.Div(
    #Style of all UI features
    style={
        "backgroundColor": "#FFFDF2", # Sets background color
        "height": "100vh", #Sets height of UI features
        "padding": "0", #Adds padding between UI features
        "color": "black",#Sets color of UI features
        "margin": "0", #Margin of UI features
        "border": "10px double black", #Border thickness and color for UI features
        "overflow": "hidden", #Manages UI text overflow
        "boxSizing": "border-box", #Sets UI format
        "fontFamily": "Garamond", #Sets UI text font type
    },
    #UI features being displayed
    children=[
        # header with logo and navbar
        html.Div(
            style={
                "display": "flex", #display
                "alignItems": "center", #alignment
                "justifyContent": "space-between", #spacing
                "padding": "10px 20px", #padding
                "backgroundColor": "#FFFDF2", #background color
            },
            children=[
                # logo
                html.A(
                    href="/",
                    children=html.Img(
                        src="/assets/logo.png",
                        alt = "Website Logo. Shows image of a blue wolf (mascot of Sun Prairie West High School).",
                        style={
                            "height": "80px", #Height of image
                            "width": "auto", #Width of image
                            "cursor": "pointer", #Lets you click image
                        },
                    ),
                ),
                # navbar
                html.Nav(
                    style={
                        "padding": "10px", #Navbar padding
                        "display": "flex", #Navbar display
                        "justifyContent": "space-around", #Navbar spacing
                        "gap": "20px", #Gap between Navbar links
                        "alignItems": "center", #Navbar alignment
                    },
                    #Navar links
                    children=[
                             html.A("Home", href="/", className="navbar"),
                            html.A("Sign Up", href="/signup", className="navbar"),
                            html.A("Sign In", href="/signin", className="navbar"),
            ]
                ),
            ],
        ),

        #Page UI
        html.Div(
            style={
                "textAlign": "center", #Alignment
                "position": "absolute", #Position
                "top": "53%", #Alignment from top
                "left": "50%", #Alignment from left
                "transform": "translate(-50%, -50%)", #Transformation
                "width": "95%", #Width of boxes
                "backgroundColor": "none", #Boxes background color
            },
            #Sign In Inputs
            children=[
                html.H2("Sign In", style={"color": "black", "fontSize": "3vw"}), #Sign in label

                # Makes sign in form                   
                dbc.Form(
                    [
                        #Username input row
                        dbc.Row(
                            [
                                dbc.Label("Username", width=3, style={"fontSize": "1.5vw"}), #Username Input Label
                                dbc.Col(
                                    #Allows for input
                                    dbc.Input(
                                        type="text",
                                        id="username_input", #Username input id (for callback)
                                        placeholder="Enter your username", #Text displayed in input box
                                        style=input_style, #Sets styling
                                    ),
                                    width=8,
                                ),
                            ],
                            className="mb-3",
                        ),
                        #Password input row
                        dbc.Row(
                            [
                                dbc.Label("Password", width=3, style={"fontSize": "1.5vw"}), #Password input label
                                dbc.Col(
                                    #Allows for input
                                    dbc.Input(
                                        type="password",
                                        id="password_input", #Password input id (for callback)
                                        placeholder="Enter your password", #Text displayed in input box
                                        style=input_style, #Sets styling
                                    ),
                                    width=8,
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Div(
                            #Sign in button
                            dbc.Button(
                                "Submit", #displayed label
                                id="submit_button_Signin", #button id
                                className="button",
                                n_clicks=0,
                                #Styling for button
                                style={
                                    "backgroundColor": "black",
                                    "color": "#FFFDF2",
                                    "padding": "10px 20px",
                                    "border": "none",
                                    "borderRadius": "5px",
                                    "cursor": "pointer",
                                    "fontSize": "1.5vw",  
                                    "position": "center",
                                    "top": "100%",
                                    "left": "550px"
                                },
                            ),
                            style={"textAlign": "center"},
                        ),
                        #Displaying message
                        html.Div(
                            id="finalMessage",
                            style={"marginTop": "10px", "color": "black", "fontSize": "1.5vw"},
                        ),
                    ]
                ),
                #Redirection to homepage after signing ing
                html.Div(id="redirectOutput")
            ],
        ),
    ],
)

#Call back when you sign in
@callback(
    [Output('session', 'data',allow_duplicate=True), Output("redirectOutput", 'children')], #redirects to homepage after sign in
    Input('submit_button_Signin', 'n_clicks'), #Checks for button click
    State('password_input', 'value'), #Checks password input
    State('username_input', 'value'), #Checks username input
    prevent_initial_call=True,
)
#Method checks if sign in is valid
def onSubmit(clicks, username, password):
    """
    Handles on submit. 
    Signs in the user by matching username and password.
    Sets the user informtion in session.

    Returns: 
        User session details

    """
    dataAccess = UserDataAccess() #Connects to database
    
    #Checks if username exists and searches database for user with username
    if username:
        result = dataAccess.doesUserExist(username, password)

        if result > 0: #if user exists
            session = Session() #creates session for website usage
            session.id = result
            session.userStatus = dataAccess.getUserStatus(result)
            session.loggedIn = True
            return [session.to_dict(), dcc.Location(pathname="/", id="locationID")] #redirects to homepage


    #If sign in is incorrect, don't sign in
    session = Session()
    session.loggedIn = False
    return [session.to_dict(), ""]
