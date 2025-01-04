import dash
from dash import  Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path="/createposting")

jobTitle_input = dbc.Row(
    [
        dbc.Label("Job Title", html_for = "jobTitle_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "title",
                id = "jobTitle_row",
                placeholder = "Enter the Job's Title",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",  
)

wageAmount_input = dbc.Row(
    [
        dbc.Label("Wage Amount", html_for = "wageAmount_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "wageAmount",
                id = "wageAmount_row",
                placeholder = "Enter the Job's Wage Amount",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

workHours_input = dbc.Row(
    [
        dbc.Label("Work Hours", html_for = "workHours_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "workHours",
                id = "workHours_row",
                placeholder = "Enter the Job's Work Hours",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

location_input = dbc.Row(
    [  
        dbc.Label("Job Location", html_for = "location_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "location",
                id = "location_row",
                placeholder = "Enter the Job's Location",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

company_input = dbc.Row(
    [  
        dbc.Label("Company Name", html_for = "company_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "companyName",
                id = "company_row",
                placeholder = "Enter the Company's Name",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

jobQualifications_input = dbc.Row(
    [  
        dbc.Label("Job Qualifications", html_for = "jobQualifications_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='jobQualifications_row',
                value="Enter the Job's Qualifications",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

jobDescription_input = dbc.Row(
    [  
        dbc.Label("Job Description", html_for = "jobDescription_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='jobDescription_row',
                value="Enter the Job's Description",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

benefits_input = dbc.Row(
    [  
        dbc.Label("Job Benefits", html_for = "benefits_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='benefits_row',
                value="Enter the Job's Benefits",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

keywords_input = dbc.Row(
    [  
        dbc.Label("Job Keywords", html_for = "keywords_row", width = 2),
        dbc.Col(
            dcc.Textarea(
                id='keywords_row',
                value="Enter the Job Keywords to Let Students Find the Job",
                style={'width': '100%', 'height': 200},
    ),
        ),
    ],
    className = "mb-3",
)

message = html.Div(id = "confirmation", children = "")


submitButton = html.Div(
    html.Button("Submit", id='submit_button',  className = "me-1", n_clicks=0)
    )

form = dbc.Form([jobTitle_input, company_input, location_input, workHours_input, wageAmount_input, jobDescription_input, jobQualifications_input, benefits_input, keywords_input, submitButton, message])


layout = html.Div([
    form   
])

@callback(
    Output('confirmation', "children"),
    Input('submit_button', 'n_clicks'),
    State('jobTitle_row', 'value'),
    State('company_row', 'value'),
    State('location_row', 'value'),
    State('workHours_row','value'),
    State('wageAmount_row', 'value'),
    State('jobDescription_row', 'value'),
    State('jobQualifications_row', 'value'),
    State('benefits_row', 'value'),
    State('keywords_row', 'value'),
    prevent_initial_call = True

)

def onSubmit(clicks, title, company, location, workHours, wageAmount, description, qualifications, benefits, keywords):
    dataAccess = JobDataAccess()
    
    newJob = Job()
    newJob.title = title
    newJob.company = company
    newJob.location = location
    newJob.workHours = workHours
    newJob.wageAmount = wageAmount
    newJob.description = description
    newJob.qualifications = qualifications
    newJob.benefits = benefits
    newJob.keywords = keywords
    newJob.status = "New"
    
    dataAccess.createJob(newJob)
    
    return "You have successfully created the job posting. Please wait for the admin to approve or decline the posting."
    
#if __name__ == '__main__':
#    app.run(debug=True)
  

