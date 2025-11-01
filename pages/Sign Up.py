import dash
from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User

"""
This code handles sign up of new users.
"""
# Keep this
dash.register_page(__name__, path='/signup')

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


def layout(**kwargs):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.

    Returns: Dash HTML tags to display.
    """
    return html.Div(
        style={
            "backgroundColor": "#FFFDF2",
            "height": "100vh",
            "padding": "0",
            "color": "black",
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
                    "backgroundColor": "#FFFDF2",
                },
                children=[
                    # logo
                    html.A(
                        href="/",
                        children=html.Img(
                            src="/assets/logo.png",
                            alt = "Website Logo. Shows image of a blue wolf (mascot of Sun Prairie West High School).",
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
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "width": "95%",
                    "backgroundColor": "none",
                },
                children=[
                    html.H2("Sign Up", style={"color": "black", "fontSize": "3vw"}),  
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
                                            style= input_style,
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
                                            style= input_style,
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
                                            style= input_style,
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
                                            style= input_style,
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
                                            style= input_style,
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
                                            style= input_style,
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
                            html.Div(id="message", style={"marginTop": "10px", "color": "black", "fontSize": "1.5vw"}),
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
    """
    Handles on submit. Creates the user in the database

    """
    data_access = UserDataAccess()
    new_user = User()
    new_user.firstName=first_name
    new_user.lastName=last_name
    new_user.email=email
    new_user.phoneNumber=phone_number
    new_user.isAdmin=False
    new_user.status="New"
    new_user.password=password
    new_user.username=username
    
    data_access.createUser(new_user)
    return (
        f"You have been registered! Please wait for approval. Use your username: '{username}' "
        f"and password: '{password}' to log in."
    )
