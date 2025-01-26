import dash
from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User

# Keep this
dash.register_page(__name__, path='/signup')

def layout(**kwargs):
    return html.Div(
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
                    html.Nav(
                        style={
                            "padding": "10px",
                            "display": "flex",
                            "justifyContent": "space-around", 
                            "gap": "20px",  # style and look for navbar
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
                    "top": "55%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "width": "95%",
                    "backgroundColor": "none",
                },
                children=[
                    html.H2("Sign Up", style={"color": "#1a1f61", "fontSize": "3vw"}),  
                    dbc.Form(
                        [
                            dbc.Row(
                                [
                                    dbc.Label("First Name", width=3, style={"fontSize": "1.5vw"}),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text",
                                            id="first_name_row",
                                            placeholder="Enter your first name",
                                            style={"backgroundColor": "#bec2cb",
                                                   "color": "#1a1f61",
                                                   "borderColor": "#1a1f61",
                                                   "fontSize": "1.5vw"},
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
                                            id="last_name_row",
                                            placeholder="Enter your last name",
                                            style={"backgroundColor": "#bec2cb",
                                                   "color": "#1a1f61",
                                                   "borderColor": "#1a1f61",
                                                   "fontSize": "1.5vw"},
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
                                            id="email_row",
                                            placeholder="Enter your email",
                                            style={"backgroundColor": "#bec2cb",
                                                   "color": "#1a1f61",
                                                   "borderColor": "#1a1f61",
                                                   "fontSize": "1.5vw"},
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
                                            type="tel",
                                            id="phone_number_row",
                                            placeholder="Enter your phone number",
                                            style={"backgroundColor": "#bec2cb",
                                                   "color": "#1a1f61",
                                                   "borderColor": "#1a1f61",
                                                   "fontSize": "1.5vw"},
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
                                            id="password_row",
                                            placeholder="Create your password",
                                            style={"backgroundColor": "#bec2cb",
                                                   "color": "#1a1f61",
                                                   "borderColor": "#1a1f61",
                                                   "fontSize": "1.5vw"},
                                        ),
                                        width=8,
                                    ),
                                ],
                                className="mb-3",
                            ),
                            dbc.Row(
                                [
                                    dbc.Label("Username", width=3, style={"fontSize": "1.5vw"}),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text",
                                            id="username_row",
                                            placeholder="Create your username",
                                            style={"backgroundColor": "#bec2cb",
                                                   "color": "#1a1f61",
                                                   "borderColor": "#1a1f61",
                                                   "fontSize": "1.5vw"},
                                        ),
                                        width=8,
                                    ),
                                ],
                                className="mb-3",
                            ),
                            html.Div(
                                dbc.Button(
                                    "Submit",
                                    id="submit_button_signUp",
                                    className="button",
                                    n_clicks=0,
                                    style={"backgroundColor": "#1a1f61",
                                           "color": "white",
                                           "fontSize": "1.5vw"},
                                ),
                                style={"textAlign": "center"},
                            ),
                            html.Div(id="message", style={"marginTop": "10px", "color": "#1a1f61", "fontSize": "1.5vw"}),
                        ]
                    ),
                ],
            ),
        ],
    )


@callback(
    Output("message", "children"),
    Input("submit_button_signUp", "n_clicks"),
    State("first_name_row", "value"),
    State("last_name_row", "value"),
    State("email_row", "value"),
    State("phone_number_row", "value"),
    State("password_row", "value"),
    State("username_row", "value"),
    prevent_initial_call=True,
)
def on_submit(n_clicks, first_name, last_name, email, phone_number, password, username):
    data_access = UserDataAccess()
    new_user = User(
        firstName=first_name,
        lastName=last_name,
        email=email,
        phoneNumber=phone_number,
        isAdmin=False,
        status="New",
        password=password,
        username=username,
    )
    data_access.createUser(new_user)
    return (
        f"You have been registered! Please wait for approval. Use your username: '{username}' "
        f"and password: '{password}' to log in."
    )
