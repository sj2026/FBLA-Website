import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ResumeDataAccess import ResumeDataAccess
from beans.Resume import Resume

# Registering the page
dash.register_page(__name__, path_template="/resume/<mode>/<resume_id>")

resume = Resume()

# Standard input style
input_style = {
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "width": "100%",
    "height": "40px",
    "borderRadius": "5px",
    "padding": "5px",
    "borderColor": "#1a1f61",
}

# Textarea style
textarea_style = {
    "width": "100%",
    "height": "100px",
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "borderRadius": "5px",
    "padding": "5px",
    "borderColor": "#1a1f61",
}

# Navbar
navbar = html.Div(
    style={
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "space-between",
        "padding": "10px 20px",
        "backgroundColor": "#bec2cb",
    },
    children=[
        # Logo
        html.A(
            href="/home",
            children=html.Img(
                src="/assets/logo.png",
                style={
                    "height": "80px",
                    "width": "auto",
                    "cursor": "pointer",
                },
            ),
        ),
        # Navbar links
        html.Nav(
            style={
                "display": "flex",
                "gap": "20px",
                "alignItems": "center",
            },
            children=[
               html.A("Home", href="home", className="navbar"),
                html.A("View Jobs", href="jobs", className="navbar"),                   # navbar buttons
                html.A("Sign Up", href="signup", className="navbar"),
                html.A("Post a Job", href="createposting", className="navbar"),
                html.A("Contact Us", href="contactus", className="navbar"),]
        ),
    ],
)

# Form inputs
resumeName_input = dbc.Row(
    [
        dbc.Label("Resume Name", html_for="resumeName_row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="resumeName_row",
                placeholder="Enter the Resume's Name",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

studentID_input = dbc.Row(
    [
        dbc.Label("Student ID", html_for="studentID_row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="studentID_row",
                placeholder="Enter your Student ID",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

pastExperience_input = dbc.Row(
    [
        dbc.Label("Past Experience", html_for="pastExperience_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="pastExperience_row",
                placeholder="Enter your past experiences",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

skillset_input = dbc.Row(
    [
        dbc.Label("Skillset", html_for="skillset_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="skillset_row",
                placeholder="Enter your skillsets",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

summary_input = dbc.Row(
    [
        dbc.Label("Summary", html_for="summary_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="summary_row",
                placeholder="Enter a summary",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

message = html.Div(
    id="outMessage",
    style={"color": "#1a1f61", "fontSize": "16px"}
)

submitButton = html.Div(
    html.Button(
        "Submit",
        id="submit_button",
        className="button",
        n_clicks=0,
        style={
            "backgroundColor": "#1a1f61",
            "color": "white",
            "padding": "10px 20px",
            "border": "none",
            "borderRadius": "5px",
            "cursor": "pointer",
            "fontSize": "16px",
        },
    ),
    style={"textAlign": "center", "marginTop": "20px"},
)

form = dbc.Form(
    style={
        "backgroundColor": "none",
        "padding": "20px",
    },
    children=[
        resumeName_input,
        studentID_input,
        pastExperience_input,
        skillset_input,
        summary_input,
        submitButton,
        message,
    ],
)

layout = html.Div(
    style={
        "border": "10px double #1a1f61",
        "padding": "0",
        "boxSizing": "border-box",
        "backgroundColor": "#bec2cb",
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "#bec2cb",
                "height": "100vh",
                "padding": "0",
                "color": "#1a1f61",
                "fontFamily": "Garamond",
            },
            children=[
                navbar,
                html.H2("Resume", style={"textAlign": "center"}),
                html.Div(
                    style={
                        "textAlign": "center",
                        "margin": "20px auto",
                        "width": "95%",
                        "backgroundColor": "none",
                        "height": "calc(90vh - 140px)",
                        "overflowY": "auto",
                        "padding": "20px",
                        "boxSizing": "border-box",
                        "borderRadius": "5px",
                        "border": "2px solid #1a1f61",
                    },
                    children=form,
                ),
            ],
        ),
    ],
)