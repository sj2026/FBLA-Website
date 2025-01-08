import dash
from dash import  Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.ResumeDataAccess import ResumeDataAccess
from beans.Resume import Resume

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path_template="/resume/<mode>/<resume_id>")

resume = Resume()

resumeName_input = dbc.Row(
    [
        dbc.Label("Resume Name", html_for = "resumeName_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "resumeName",
                id = "resumeName_row",
                placeholder = "Enter the Resume's Name",
                #value = resume.resumeName
            ),
            width = 10,
        ),
    ],
    className = "mb-3",  
)

studentID_input = dbc.Row(
    [
        dbc.Label("Student ID", html_for = "studentID_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "studentID",
                id = "studentID_row",
                placeholder = "Enter your student ID",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

pastExperience_input = dbc.Row(
    [  
        dbc.Label("Past Experience", html_for = "pastExperience_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='pastExperience_row',
                value="Enter your past experiences",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

skillset_input = dbc.Row(
    [  
        dbc.Label("Skillset", html_for = "skillset_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='skillset_row',
                value="Enter your skillsets",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

summary_input = dbc.Row(
    [  
        dbc.Label("Summary", html_for = "summary_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='summary_row',
                value="Enter a summary",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

message = html.Div(id = "outMessage", children = "")


submitButton = html.Div(
    html.Button("Submit", id='submit_button',  className = "me-1", n_clicks=0)
    )

form = dbc.Form([resumeName_input, studentID_input, pastExperience_input, skillset_input, summary_input, submitButton, message])


layout = html.Div([
    form   
])
'''
def layout(mode=None, resume_id=None, **kwargs):
    if(mode=="view" or mode == "edit"):
        resumeAccess = ResumeDataAccess()
        resumeTemp = resumeAccess.getResume(resume_id)
        resume.resumeName = resumeTemp.resumeName
        
    return html.Div(
        form
    )
'''

@callback(
    Output('outMessage', "children"),
    Input('submit_button', 'n_clicks'),
    State('resumeName_row', 'value'),
    State('studentID_row', 'value'),
    State('pastExperience_row', 'value'),
    State('skillset_row','value'),
    State('summary_row', 'value'),
    prevent_initial_call = True

)

def onSubmit(clicks, resumeName, studentID, pastExperience, skillset, summary):
    dataAccess = ResumeDataAccess()
    
    newResume = Resume()
    newResume.resumeName = resumeName
    newResume.studentID = studentID
    newResume.pastExperience = pastExperience
    newResume.skillset = skillset
    newResume.summary = summary
    
    dataAccess.createResume(newResume)
    
    return "You have successfully created the resume."
    
#if __name__ == '__main__':
#    app.run(debug=True)
  

