import dash
from dash import  Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ResumeDataAccess import ResumeDataAccess
from beans.Resume import Resume

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path_template = "/resume/<mode>/<resume_id>")


resume = {
    'resumeName' : '',
    'studentID' : 0,
    'pastExperience' : '"Enter your past experiences"',
    'skillset' : 'Enter your skillsets',
    'summary' : 'Enter a summary',
}



#layout = html.Div([
#    form   
#])

def layout(mode=None, resume_id=None, **kwargs):
    global screenMode
    screenMode = mode

    global resumeID
    resumeID = resume_id
    
    global resume
    readOnly = ''
    onlyRead = False
    
    if (resume_id == None):
        resume = {
            'resumeName' : '',
            'studentID' : 0,
            'pastExperience' : '"Enter your past experiences"',
            'skillset' : 'Enter your skillsets',
            'summary' : 'Enter a summary',
        }
    
    if(mode=="view" or mode == "edit"):
        resumeAccess = ResumeDataAccess()
        resumeTemp = resumeAccess.getResume(resume_id)
        resume['resumeName'] = resumeTemp.resumeName
        resume['studentID'] = resumeTemp.studentID
        resume['pastExperience'] = resumeTemp.pastExperience
        resume['skillset'] = resumeTemp.skillset
        resume['summary'] = resumeTemp.summary
    
    if (mode == 'view'):
        readOnly = "readOnly"
        onlyRead = True

    resumeName_input = dbc.Row(
    [
        dbc.Label("Resume Name", html_for = "resumeName_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "resumeName",
                id = "resumeName_row",
                placeholder = "Enter the Resume's Name",
                value = resume['resumeName'], 
                readonly=readOnly,
                className = "inputSmall"
            ),
            width = 10,
        ),
    ],
    className = "inputSmall",  
    )

    studentID_input = dbc.Row(
    [
        dbc.Label("Student ID", html_for = "studentID_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "studentID",
                id = "studentID_row",
                placeholder = "Enter your student ID",
                value = resume['studentID'], 
                readonly=readOnly,
                className = "inputSmall"
            ),
            width = 10,
        ),
    ],
    className = "inputSmall",
)

    pastExperience_input = dbc.Row(
    [  
        dbc.Label("Past Experience", html_for = "pastExperience_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='pastExperience_row',
                style={'width': '100%', 'height': 200},
                value = resume['pastExperience'], 
                readOnly=onlyRead,
                className = "inputSmall"
    ),
        ),
    ],
    className = "inputSmall",
)

    skillset_input = dbc.Row(
    [  
        dbc.Label("Skillset", html_for = "skillset_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='skillset_row',
                style={'width': '100%', 'height': 200},
                value = resume['skillset'], 
                readOnly=onlyRead,
                className = "inputSmall"
    ),
        ),
    ],
    className = "inputSmall",
)

    summary_input = dbc.Row(
    [  
        dbc.Label("Summary", html_for = "summary_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='summary_row',
                style={'width': '100%', 'height': 200},
                value = resume['summary'], 
                readOnly=onlyRead,
                className = "inputSmall"
    ),
        ),
    ],
    className = "inputSmall",
)

    message = html.Div(id = "outMessage", children = "")


    submitButton = html.Div(
    html.Button("Submit", id='submit_button_resume',  className = "button", n_clicks=0)
    )

    if (mode == 'view'):
        form = dbc.Form([resumeName_input, studentID_input, pastExperience_input, skillset_input, summary_input, message])
    
    else:
        form = dbc.Form([resumeName_input, studentID_input, pastExperience_input, skillset_input, summary_input, submitButton, message])

        
    return html.Div(
        form
    )


@callback(
    Output('outMessage', "children"),
    Input('submit_button_resume', 'n_clicks'),
    State('resumeName_row', 'value'),
    State('studentID_row', 'value'),
    State('pastExperience_row', 'value'),
    State('skillset_row','value'),
    State('summary_row', 'value'),
    prevent_initial_call = True

)

def onSubmit(clicks, resumeName, studentID, pastExperience, skillset, summary):
    
    dataAccess = ResumeDataAccess()
    
    resume = Resume()
    resume.resumeName = resumeName
    resume.studentID = studentID
    resume.pastExperience = pastExperience
    resume.skillset = skillset
    resume.summary = summary
    

    if (screenMode == "edit"):
        resume.id = resumeID
        dataAccess.updateResume(resume)
    
    else:
        dataAccess.createResume(resume)
    
    return "You have successfully created the resume."
    
#if __name__ == '__main__':
#    app.run(debug=True)
  

