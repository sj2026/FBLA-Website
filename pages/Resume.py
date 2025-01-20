import dash
from dash import  Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ResumeDataAccess import ResumeDataAccess
from beans.Resume import Resume

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path_template = "/resume/<mode>/<resume_id>")

resume = {
    'resumeName': '',
    'studentID': 0,
    'pastExperience': 'Enter your past experiences',
    'skillset': 'Enter your skillsets',
    'summary': 'Enter a summary',
}

# Custom styles for inputs and textareas
input_style = {
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "width": "100%",
    "height": "40px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid #1a1f61",
    "overflowY": "auto",  # Make input scrollable if text overflows
}

textarea_style = {
    "backgroundColor": "#bec2cb",
    "color": "#1a1f61",
    "width": "100%",
    "height": "200px",
    "borderRadius": "5px",
    "padding": "5px",
    "resize": "vertical",
    "overflowY": "auto",
    "border": "1px solid #1a1f61",
}

button_style = {
    "backgroundColor": "#1a1f61",
    "color": "white",
    "padding": "10px 20px",
    "border": "none",
    "borderRadius": "5px",
    "cursor": "pointer",
    "fontSize": "16px",
}

form_style = {
    "backgroundColor": "none",
    "padding": "20px",
}

# Layout function
def layout(mode=None, resume_id=None, **kwargs):
    global screenMode
    screenMode = mode

    global resumeID
    resumeID = resume_id
    
    global resume
    readOnly = ''
    onlyRead = False
    
    if resume_id is None:
        resume = {
            'resumeName': '',
            'studentID': 0,
            'pastExperience': 'Enter your past experiences',
            'skillset': 'Enter your skillsets',
            'summary': 'Enter a summary',
        }
    
    if mode == "view" or mode == "edit":
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

    resumeName_input = dbc.Row(
        [
            dbc.Label("Resume Name", html_for="resumeName_row", width=2),
            dbc.Col(
                dbc.Input(
                    type="text",
                    id="resumeName_row",
                    placeholder="Enter the Resume's Name",
                    value=resume['resumeName'],
                    readonly=readOnly,
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
                    value=resume['studentID'],
                    readonly=readOnly,
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
                    id='pastExperience_row',
                    value=resume['pastExperience'],
                    readOnly=onlyRead,
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
                    id='skillset_row',
                    value=resume['skillset'],
                    readOnly=onlyRead,
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
                    id='summary_row',
                    value=resume['summary'],
                    readOnly=onlyRead,
                    style=textarea_style,
                ),
            ),
        ],
        className="mb-3",
    )

    message = html.Div(id="outMessage", children="")

    submitButton = html.Div(
        html.Button("Submit", id='submit_button', className="button", n_clicks=0, style=button_style),
        style={"textAlign": "center", "marginTop": "20px"},
    )

    # Form layout for 'view' and 'edit' modes
    if mode == 'view':
        form = dbc.Form([resumeName_input, studentID_input, pastExperience_input, skillset_input, summary_input, message])
    else:
        form = dbc.Form([resumeName_input, studentID_input, pastExperience_input, skillset_input, summary_input, submitButton, message])

    return html.Div(
        style=form_style,
        children=form
    )


# Callback to handle form submission
@callback(
    Output('outMessage', "children"),
    Input('submit_button', 'n_clicks'),
    State('resumeName_row', 'value'),
    State('studentID_row', 'value'),
    State('pastExperience_row', 'value'),
    State('skillset_row', 'value'),
    State('summary_row', 'value'),
    prevent_initial_call=True
)
def onSubmit(clicks, resumeName, studentID, pastExperience, skillset, summary):
    dataAccess = ResumeDataAccess()

    resume = Resume()
    resume.resumeName = resumeName
    resume.studentID = studentID
    resume.pastExperience = pastExperience
    resume.skillset = skillset
    resume.summary = summary

    if screenMode == "edit":
        resume.id = resumeID
        dataAccess.updateResume(resume)
    else:
        dataAccess.createResume(resume)

    return "You have successfully created or updated the resume."
