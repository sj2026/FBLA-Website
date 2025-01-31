import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ResumeDataAccess import ResumeDataAccess
from beans.Resume import Resume
from pages import PageUtil

dash.register_page(__name__, path_template="/resume/<mode>/<resume_id>")

resume = {
    'resumeName': '',
    'studentID':'',
    'pastExperience': '',
    'skillset': '',
    'summary': '',
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
    "fontSize": "1.5vw",  
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
    "fontSize": "1.5vw", 
}

# Navbar styling
'''
navbar = html.Div(
    style={
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "padding": "10px 20px",
        "backgroundColor": "#bec2cb",
        "width" : "100%"
        
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
         # navbar 
        html.Div(id="navbar_resume"),
    ],
)
'''

# layout for page
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
                dbc.Label(input_item["label"], html_for=input_item["id"], width=2, style={"color": "#1a1f61", "fontSize": "1.5vw"}),
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
                dbc.Label(textarea_item["label"], html_for=textarea_item["id"], width=2, style={"color": "#1a1f61", "fontSize": "1.5vw"}),
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

    submitButton = html.Div(
        html.Button(
            "Submit",
            id="submit_button_resume",
            className="button",
            n_clicks=0,
            style={
                "backgroundColor": "#1a1f61",
                "color": "white",
                "padding": "10px 20px",
                "border": "none",
                "borderRadius": "5px",
                "cursor": "pointer",
                "fontSize": "1.5vw",  
            },
        ),
        style={"textAlign": "center", "marginTop": "20px"},
    )
    
    message = html.Div(id="outMessage", children="")


    form = dbc.Form(input_rows + textarea_rows + ([submitButton, message] if mode != "view" else []))
    title = html.H2("Create Resume", style={"textAlign": "center", "fontSize": "3vw"})
    if mode == "view":
        title = html.H2("View Resume", style={"textAlign": "center", "fontSize": "3vw"})
    if mode == "edit":
        title = html.H2("Edit Resume", style={"textAlign": "center", "fontSize": "3vw"})
        
    layout =  html.Div(
        children = [
            title, 
            html.Div(
                        style={
                            "textAlign": "center",
                            "margin": "20px auto",
                            "width": "95%",
                            "backgroundColor": "none",
                            #"height": "calc(90vh - 140px)",
                            "overflowY": "auto",
                            "padding": "20px",
                            "boxSizing": "border-box",
                            "borderRadius": "5px",
                            "border": "2px solid #1a1f61",
                        },
                        children=form,
                    ),
        ]
    )
    return PageUtil.getContentWithTemplate("navbar_resume",layout)
    '''
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
                    "height": "200vh",
                    "padding": "0",
                    "color": "#1a1f61",
                    "margin": "0",
                    "border": "10px double #1a1f61",
                    "overflow": "hidden",
                    "boxSizing": "border-box",
                    "fontFamily": "Garamond",
                },
                children=[
                    navbar,
                    title, 
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
    '''


# Callback to handle form submission
@callback(
    Output('outMessage', "children"),
    Input('submit_button_resume', 'n_clicks'),
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


@callback(
    Output('navbar_resume', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp,data):
    session = data
    return PageUtil.getMenu(session)
