import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

dash.register_page(__name__, path_template="/job/<mode>/<job_id>")

# Default job data structure
job = {
    "id": 0,
    "title": '',
    "company": '',
    'location': '',
    'workHours': '',
    'wageAmount': '',
    'description': '',
    'qualifications': '',
    'benefits': '',
    'keywords': '',
    'status': '',
}

# Standard input style
input_style = {
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "width": "100%",
    "height": "40px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid #1a1f61",  # Dark blue border for inputs
    "overflowY": "auto",  # Make input scrollable if text overflows
}

# Textarea style with scroll
textarea_style = {
    "width": "100%",
    "height": "100px",
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "borderRadius": "5px",
    "padding": "5px",
    "resize": "vertical",  # Allow vertical resizing for the textarea
    "overflowY": "auto",  # Enable scrolling if content exceeds the height
    "border": "1px solid #1a1f61",  # Dark blue border for textareas
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

# Layout function for Job Posting page
def layout(mode=None, job_id=None, **kwargs):
    global screenMode
    screenMode = mode

    global jobID
    jobID = job_id

    global job
    readOnly = ''
    onlyRead = False

    # Set job details for 'view' and 'edit' modes
    if job_id is None:
        for key in job:
            job[key] = '' if key != 'id' else 0
    elif mode in ("view", "edit"):
        jobAccess = JobDataAccess()
        jobTemp = jobAccess.getJob(job_id)
        job.update(vars(jobTemp))

    if mode == 'view':
        readOnly = "readOnly"
        onlyRead = True

    # Form inputs
    inputs = [
        {
            "label": "Job Title",
            "id": "jobTitle_row",
            "value": job["title"],
            "placeholder": "Enter the Job's Title",
        },
        {
            "label": "Company Name",
            "id": "company_row",
            "value": job["company"],
            "placeholder": "Enter the Company's Name",
        },
        {
            "label": "Job Location",
            "id": "location_row",
            "value": job["location"],
            "placeholder": "Enter the Job's Location",
        },
        {
            "label": "Work Hours",
            "id": "workHours_row",
            "value": job["workHours"],
            "placeholder": "Enter the Job's Work Hours",
        },
        {
            "label": "Wage Amount",
            "id": "wageAmount_row",
            "value": job["wageAmount"],
            "placeholder": "Enter the Job's Wage Amount",
        },
    ]

    textareas = [
        {
            "label": "Job Description",
            "id": "jobDescription_row",
            "value": job["description"],
            "placeholder": "Enter the Job's Description",
        },
        {
            "label": "Job Qualifications",
            "id": "jobQualifications_row",
            "value": job["qualifications"],
            "placeholder": "Enter the Job's Qualifications",
        },
        {
            "label": "Job Benefits",
            "id": "benefits_row",
            "value": job["benefits"],
            "placeholder": "Enter the Job's Benefits",
        },
        {
            "label": "Job Keywords",
            "id": "keywords_row",
            "value": job["keywords"],
            "placeholder": "Enter the Job's Keywords",
        },
    ]

    input_rows = [
        dbc.Row(
            [
                dbc.Label(input_item["label"], html_for=input_item["id"], width=2, style={"color": "#1a1f61"}),  # Dark blue label
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
                dbc.Label(textarea_item["label"], html_for=textarea_item["id"], width=2, style={"color": "#1a1f61"}),  # Dark blue label
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