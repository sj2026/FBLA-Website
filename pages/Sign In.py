import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User
from db import ConnectionUtil
from beans.Session import Session

dash.register_page(__name__, path="/signin")

layout = html.Div(
    style={
        "backgroundColor": "#bec2cb",
        "height": "100vh",
        "padding": "0",
        "color": "#1a1f61",
        "margin": "0",
        "border": "10px double #1a1f61",
        "overflow": "hidden",
        "boxSizing": "border-box",
        "fontFamily": "Garamond",
    },
    children=[
        # header with logo and navbar
        html.Div(
            style={
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
                "padding": "10px 20px",
                "backgroundColor": "#bec2cb",
            },
            children=[
                # logo
                html.A(
                    href="/",
                    children=html.Img(
                        src="/assets/logo.png",
                        style={
                            "height": "80px",
                            "width": "auto",
                            "cursor": "pointer",
                        },
                    ),
                ),
                # navbar
                html.Nav(
                    style={
                        "padding": "10px",
                        "display": "flex",
                        "justifyContent": "space-around",
                        "gap": "20px",
                        "alignItems": "center",
                    },
                    children=[
                             html.A("Home", href="/", className="navbar"),
                html.A("Sign Up", href="/signup", className="navbar"),
                html.A("Sign In", href="/signin", className="navbar"),
            ]
                ),
            ],
        ),

        html.Div(
            style={
                "textAlign": "center",
                "position": "absolute",
                "top": "53%",
                "left": "50%",
                "transform": "translate(-50%, -50%)",
                "width": "95%",
                "backgroundColor": "none",
            },
            children=[
                html.H2("Sign In", style={"color": "#1a1f61", "fontSize": "3vw"}),
                dbc.Form(
                    [
                        dbc.Row(
                            [
                                dbc.Label("Username", width=3, style={"fontSize": "1.5vw"}),
                                dbc.Col(
                                    dbc.Input(
                                        type="text",
                                        id="username_input",
                                        placeholder="Enter your username",
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
                                dbc.Label("Password", width=3, style={"fontSize": "1.5vw"}),
                                dbc.Col(
                                    dbc.Input(
                                        type="password",
                                        id="password_input",
                                        placeholder="Enter your password",
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
                                "Submit",
                                id="submit_button_Signin",
                                className="button",
                                n_clicks=0,
                                style={
                                    "backgroundColor": "#1a1f61",
                                    "color": "white",
                                    "fontSize": "1.5vw",
                                },
                            ),
                            style={"textAlign": "center"},
                        ),
                        html.Div(
                            id="finalMessage",
                            style={"marginTop": "10px", "color": "#1a1f61", "fontSize": "1.5vw"},
                        ),
                    ]
                ),
                html.Div(id="redirectOutput")
            ],
        ),
    ],
)


@callback(
    [Output('session', 'data'), Output("redirectOutput", 'children')],
    Input('submit_button_Signin', 'n_clicks'),
    State('password_input', 'value'),
    State('username_input', 'value'),
    prevent_initial_call=True,
)
def onSubmit(clicks, username, password):
    dataAccess = UserDataAccess()
    if username:
        result = dataAccess.doesUserExist(username, password)

        if result > 0:
            session = Session()
            session.id = result
            session.userStatus = dataAccess.getUserStatus(result)
            session.loggedIn = True
            return [session.to_dict(), dcc.Location(pathname="/", id="locationID")]

    session = Session()
    session.loggedIn = False
    return [session.to_dict(), ""]
