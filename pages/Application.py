import dash
from dash import Dash, Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ApplicationDataAccess import ApplicationDataAccess
from beans.Application import Application
from db.ResumeDataAccess import ResumeDataAccess
from pages import PageUtil


#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path_template = "/jobapplication/<mode>/<job_id>/<application_id>")

application = {
    'jobID': 0,
    'studentID': 0,
    'resumeID': 0,
    'additionalDetails': '',
    'status': '',
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
def layout(mode=None, job_id = None, application_id = None, **kwargs):
    global screenMode
    screenMode = mode

    global jobID
    jobID = job_id
    
    global applicationID
    applicationID = application_id
    
    global application
    readOnly = ''
    onlyRead = False
    
    
    global ResumedataAccess
    ResumedataAccess = ResumeDataAccess()
    
    if application_id is None:
        application = {
            'jobID': 0,
            'studentID': 0,
            'resumeID': 0,
            'additionalDetails': '',
            'status': '',
        }
    
    if mode == "view" or mode == "edit":
        applicationAccess = ApplicationDataAccess()
        applicationTemp = applicationAccess.getApplication(application_id)
        application['jobID'] = applicationTemp.jobID
        application['studentID'] = applicationTemp.studentID
        application['resumeID'] = applicationTemp.resumeID
        application['additionalDetails'] = applicationTemp.additionalDetails
        application['status'] = applicationTemp.status
        
    
    if mode == 'view':
        readOnly = "readOnly"
        onlyRead = True
        
    studentID_input = dbc.Row(
            [
                dbc.Label("Student ID", html_for="studentIDApplication_row", width=2),
                dbc.Col(
                    dbc.Input(
                        id="studentIDApplication_row",
                        value=application['studentID'],
                        style=input_style,
                        readonly=readOnly,
                    ),
                    width=10,
                ),
            ],
            className="mb-3",
        )

    additionalDetails_input = dbc.Row(
        [
            dbc.Label("Additional Comments to Employer", html_for="additionalDetails_row", width=2),
            dbc.Col(
                dcc.Textarea(
                    id='additionalDetails_row',
                    value=application['additionalDetails'],
                    readOnly=onlyRead,
                    style=textarea_style,
                ),
            ),
        ],
        className="mb-3",
    )

    resume_input = dbc.Row(
        [
        dbc.Label("Add Resume", html_for="resumeID_row", width = 2),
        dbc.Col(
            dcc.Dropdown(
            options= [],
            multi=True,
            placeholder="Select a Resume",
            style={
                "width": "100%",
                "margin": "20px 0",
            },
            id = "resumeID_row"
        )
        )
        ]
    )
    
    resume_input_hidden = dbc.Row(
        [
        dbc.Col(
            dcc.Dropdown(
            options= [],
            multi=True,
            placeholder="Select a Resume",
            style={
                "display" : "none",
            },
            id = "resumeID_row",
            
        )
        )
        ]
    )

    message = html.Div(id="OutputJobApplication", children="")

    submitButton = html.Div(
        html.Button("Submit", id='Application_submitButton', className="button", n_clicks=0, style=button_style),
        style={"textAlign": "center", "marginTop": "20px"},
    )
    
    link_element = html.Div(
        dcc.Link("View Resume", href="/resume/view/"+str(application['resumeID']))
    ) 

    # Form layout for 'view' and 'edit' modes
    if mode == 'view':
        form = dbc.Form([ studentID_input, additionalDetails_input, resume_input_hidden, link_element, message])
    else:
        form = dbc.Form([additionalDetails_input, resume_input, submitButton, message])

    layout= html.Div(
        style=form_style,
        children=form
    )
    
    return PageUtil.getContentWithTemplate("navbar_application",layout)
    
@callback(
    [Output('resumeID_row','options'),
    Output('navbar_application', 'children')],
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp,data):
    #print(data)
    global session 
    session = data
    options = []
    
    if (screenMode != "view"):
        studentID = session['id']
        resumeList = ResumedataAccess.getResumes(studentID, "List")
        #print(resumeList)
        for i in range(0, len(resumeList)):
            resume = resumeList[i]
            options.append(
                {"label": resume.resumeName, "value": str(resume.id)}
            )
    if len(options) == 0:
        options.append(
                {"label": "None", "value": "None"}
            )
    return [options,PageUtil.getMenu(session)]
    
    #if (screenMode == 'view' and applicationID != None):
     #   options = []
     #   application = ApplicationDataAccess.getApplication(applicationID)
     #   resume = ResumedataAccess.getResume(application.resumeID)
     #   options.append(
     #       {"label": resume.resumeName, "value": str(resume.id)}
     #   )

# Callback to handle form submission
@callback(
    Output('OutputJobApplication', "children"),
    Input('Application_submitButton', 'n_clicks'),
    State('additionalDetails_row', 'value'),
    State('resumeID_row', 'value'),
    prevent_initial_call=True
)
def onSubmit(clicks, additionalDetails, resume):
    dataAccess = ApplicationDataAccess()
    application = Application()
    application.additionalDetails = additionalDetails
    application.resumeID = ''.join(map(str, resume))
    application.studentID = session["id"]
    application.jobID = jobID
    application.status = 'New'

    if screenMode == "edit":
        application.id = applicationID
        dataAccess.updateApplication(application)
    else:
        dataAccess.createApplication(application)

    return "You have successfully created or updated the application."


