import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

# Registering the page
dash.register_page(__name__, path="/createposting")


# Navbar with logo
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

# Standard input style
input_style = {
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "width": "100%",
    "height": "40px",
    "borderRadius": "5px",
    "padding": "5px",
    "borderColor":"#1a1f61",
}

# Form inputs
jobTitle_input = dbc.Row(
    [
        dbc.Label("Job Title", html_for="jobTitle_row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="jobTitle_row",
                placeholder="Enter the Job Title",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

wageAmount_input = dbc.Row(
    [
        dbc.Label("Wage Amount", html_for="wageAmount_row", width=2),
        dbc.Col(
            dbc.Input(
                type="number",
                id="wageAmount_row",
                placeholder="Enter the Wage Amount",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

workHours_input = dbc.Row(
    [
        dbc.Label("Work Hours", html_for="workHours_row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="workHours_row",
                placeholder="Enter the Work Hours",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

location_input = dbc.Row(
    [
        dbc.Label("Job Location", html_for="location_row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="location_row",
                placeholder="Enter the Job Location",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

company_input = dbc.Row(
    [
        dbc.Label("Company Name", html_for="company_row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="company_row",
                placeholder="Enter the Company Name",
                style=input_style,
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

textarea_style = {
    "width": "100%",
    "height": "100px",
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "borderRadius": "5px",
    "padding": "5px",
    "borderColor":"#1a1f61",
}

jobQualifications_input = dbc.Row(
    [
        dbc.Label("Job Qualifications", html_for="jobQualifications_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="jobQualifications_row",
                placeholder="Enter the Job's Qualifications",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

jobDescription_input = dbc.Row(
    [
        dbc.Label("Job Description", html_for="jobDescription_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="jobDescription_row",
                placeholder="Enter the Job's Description",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

benefits_input = dbc.Row(
    [
        dbc.Label("Job Benefits", html_for="benefits_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="benefits_row",
                placeholder="Enter the Job's Benefits",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

keywords_input = dbc.Row(
    [
        dbc.Label("Job Keywords", html_for="keywords_row", width=2),
        dbc.Col(
            dcc.Textarea(
                id="keywords_row",
                placeholder="Enter Keywords to Help Find the Job",
                style=textarea_style,
            ),
        ),
    ],
    className="mb-3",
)

message = html.Div(id="confirmation", style={"color": "#1a1f61", "fontSize": "16px"})

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
        jobTitle_input,
        company_input,
        location_input,
        workHours_input,
        wageAmount_input,
        jobDescription_input,
        jobQualifications_input,
        benefits_input,
        keywords_input,
        submitButton,
        message,
    ],
)

layout = html.Div(
    style={
        "border": "10px double #1a1f61",  # Double dark blue border
        "padding": "0",  # Spacing between border and content
        "boxSizing": "border-box",  # Ensure border doesn't affect layout dimensions
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
                html.H2("Create Job Posting", style={"textAlign": "center"}),
                html.Div(
                    style={
                        "textAlign": "center",
                        "margin": "20px auto",
                        "width": "95%",
                        "backgroundColor": "none",
                        "height": "calc(90vh - 140px)",  # Account for navbar height
                        "overflowY": "auto",  # Enable scrolling
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
