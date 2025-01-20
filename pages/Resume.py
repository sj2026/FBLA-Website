import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ResumeDataAccess import ResumeDataAccess
from beans.Resume import Resume

dash.register_page(__name__, path_template="/resume/<mode>/<resume_id>")

# Default resume data structure
resume = {
    'resumeName': '',
    'studentID': 0,
    'pastExperience': 'Enter your past experiences',
    'skillset': 'Enter your skillsets',
    'summary': 'Enter a summary',
}

# Standard input style
input_style = {
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "width": "100%",
    "height": "40px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid #1a1f61",
    "overflowY": "auto",
}

# Textarea style with scroll
textarea_style = {
    "width": "100%",
    "height": "100px",
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "borderRadius": "5px",
    "padding": "5px",
    "resize": "vertical",
    "overflowY": "auto",
    "border": "1px solid #1a1f61",
}

# Navbar styling
navbar = html.Div(
    style={
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "space-between",
        "padding": "10px 20px",
        "backgroundColor": "#bec2cb",
    },
    children=[
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
                "display": "flex",
                "gap": "20px",
                "alignItems": "center",
                "fontFamily": "Garamond",  # Ensure consistent font for navbar links
            },
            children=[
                html.A("Home", href="/", className="navbar"),
                html.A("View Jobs", href="/jobposting/<mode>/<job_id>", className="navbar"),
                html.A("Sign Up", href="/signup", className="navbar"),
                html.A("Sign In", href="/signin", className="navbar"),
                html.A("Post a Job", href="/job/<mode>/<job_id>", className="navbar"),
            ]
        ),
    ],
)

# Layout function for Resume page
def layout(mode=None, resume_id=None, **kwargs):
    global screenMode
    screenMode = mode

    global resumeID
    resumeID = resume_id

    global resume
    readOnly = ''
    onlyRead = False

    # Set resume details for 'view' and 'edit' modes
    if resume_id is None:
        resume = {
            'resumeName': '',
            'studentID': '',
            'pastExperience': '',
            'skillset': '',
            'summary': '',
        }
    elif mode in ("view", "edit"):
        resumeAccess = ResumeDataAccess()
        resumeTemp = resumeAccess.getResume(resume_id)
        resume['resumeName'] = resumeTemp.resumeName
        resume['studentID'] = resumeTemp.studentID
        resume['pastExperience'] = resumeTemp.pastExperience
        resume['skillset'] = resumeTemp.skillset
        resume['summary'] = resumeTemp.summary

    if mode == 'view':
        readOnly = "readOnly"
        onlyRead = True

    # Form inputs
    inputs = [
        {
            "label": "Resume Name",
            "id": "resumeName_row",
            "value": resume['resumeName'],
            "placeholder": "Enter the Resume's Name",
        },
        {
            "label": "Student ID",
            "id": "studentID_row",
            "value": resume['studentID'],
            "placeholder": "Enter your Student ID",
        },
    ]

    textareas = [
        {
            "label": "Past Experience",
            "id": "pastExperience_row",
            "value": resume['pastExperience'],
            "placeholder": "Enter your past experiences",
        },
        {
            "label": "Skillset",
            "id": "skillset_row",
            "value": resume['skillset'],
            "placeholder": "Enter your skillsets",
        },
        {
            "label": "Summary",
            "id": "summary_row",
            "value": resume['summary'],
            "placeholder": "Enter a summary",
        },
    ]

    input_rows = [
        dbc.Row(
            [
                dbc.Label(input_item["label"], html_for=input_item["id"], width=2, style={"color": "#1a1f61"}),
                dbc.Col(
                    dbc.Input(
                        id=input_item["id"],
                        value=input_item["value"],
                        placeholder=input_item["placeholder"],
                        style=input_style,
                        readonly=onlyRead,
                    ),
                    width=10,
                ),
            ],
            className="mb-3",
        )
        for input_item in inputs
    ]

    textarea_rows = [
        dbc.Row(
            [
                dbc.Label(textarea_item["label"], html_for=textarea_item["id"], width=2, style={"color": "#1a1f61"}),
                dbc.Col(
                    dcc.Textarea(
                        id=textarea_item["id"],
                        value=textarea_item["value"],
                        placeholder=textarea_item["placeholder"],
                        style=textarea_style,
                        readOnly=onlyRead,
                    ),
                    width=10,
                ),
            ],
            className="mb-3",
        )
        for textarea_item in textareas
    ]

    # Submit button
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

    form = dbc.Form(input_rows + textarea_rows + ([submitButton] if mode != "view" else []))

    return html.Div(
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
                    html.H2("Create Resume", style={"textAlign": "center"}),
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
