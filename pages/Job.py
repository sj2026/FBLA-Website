import dash
from dash import  Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.JobDataAccess import JobDataAccess
from beans.Job import Job

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path_template = "/job/<mode>/<job_id>")

job = {
    "id": 0,
    "title" : '',
    "company" : '',
    'location' : '',
    'workHours' : '',
    'wageAmount' : '',
    'description' : '',
    'qualifications' : '',
    'benefits' : '',
    'keywords' : '',
    'status' : '',
}
    
'''
layout = html.Div([
    form   
])
'''

def layout(mode = None, job_id = None, **kwargs):
    global screenMode
    screenMode = mode

    global jobID
    jobID = job_id
    
    global job
    readOnly = ''
    onlyRead = False
    
    if (job_id == None):
        job['id'] = 0
        job['title'] = ''
        job['company'] = ''
        job['location'] = ''
        job['workHours'] = ''
        job['wageAmount'] = ''
        job['description'] = ''
        job['qualifications'] = ''
        job['benefits'] = ''
        job['keywords'] = ''
        job['status'] = ''
    
    if(mode=="view" or mode == "edit"):
        jobAccess = JobDataAccess()
        jobTemp = jobAccess.getJob(job_id)
        job['id'] = jobID
        job['title'] = jobTemp.title
        job['company'] = jobTemp.company
        job['location'] = jobTemp.location
        job['workHours'] = jobTemp.workHours
        job['wageAmount'] = jobTemp.wageAmount
        job['description'] = jobTemp.description
        job['qualifications'] = jobTemp.qualifications
        job['benefits'] = jobTemp.benefits
        job['keywords'] = jobTemp.keywords
        job['status'] = jobTemp.status
    
    if (mode == 'view'):
        readOnly = "readOnly"
        onlyRead = True
    
    jobTitle_input = dbc.Row(
    [
        dbc.Label("Job Title", html_for = "jobTitle_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "title",
                id = "jobTitle_row",
                placeholder = "Enter the Job's Title",
                className = "inputSmall",
                value = job['title'],
                readonly=readOnly
            ),
            width = 10,
        ),
    ],
    className = "inputSmall",  
)

    wageAmount_input = dbc.Row(
        [
            dbc.Label("Wage Amount", html_for = "wageAmount_row", width = 2),
            dbc.Col(
                dbc.Input(
                    type = "wageAmount",
                    id = "wageAmount_row",
                    placeholder = "Enter the Job's Wage Amount",
                    className = "inputSmall",
                    value = job['wageAmount'],
                    readonly=readOnly
                ),
                width = 10,
            ),
        ],
        className = "inputSmall",
    )

    workHours_input = dbc.Row(
        [
            dbc.Label("Work Hours", html_for = "workHours_row", width = 2),
            dbc.Col(
                dbc.Input(
                    type = "workHours",
                    id = "workHours_row",
                    placeholder = "Enter the Job's Work Hours",
                    className = "inputSmall",
                    value = job['workHours'],
                    readonly=readOnly
                ),
                width = 10,
            ),
        ],
        className = "inputSmall",
    )

    location_input = dbc.Row(
        [  
            dbc.Label("Job Location", html_for = "location_row", width = 2),
            dbc.Col(
                dbc.Input(
                    type = "location",
                    id = "location_row",
                    placeholder = "Enter the Job's Location",
                    className = "inputSmall",
                    value = job['location'],
                    readonly=readOnly
                ),
                width = 10,
            ),
        ],
        className = "inputSmall",
    )

    company_input = dbc.Row(
        [  
            dbc.Label("Company Name", html_for = "company_row", width = 2),
            dbc.Col(
                dbc.Input(
                    type = "companyName",
                    id = "company_row",
                    placeholder = "Enter the Company's Name",
                    className = "inputSmall",
                    value = job['company'],
                    readonly=readOnly
                ),
                width = 10,
            ),
        ],
        className = "inputSmall",
    )

    jobQualifications_input = dbc.Row(
        [  
            dbc.Label("Job Qualifications", html_for = "jobQualifications_row", width = 2),
            dbc.Col(
                dcc.Textarea(
                    id='jobQualifications_row',
                    style={'width': '100%', 'height': 200},
                    value = job['qualifications'],
                    readOnly=onlyRead,
                    className = "inputSmall",
        ),
            ),
        ],
        className = "inputSmall",
    )

    jobDescription_input = dbc.Row(
        [  
            dbc.Label("Job Description", html_for = "jobDescription_row", width = 2),
            dbc.Col(
                dcc.Textarea(
                    id='jobDescription_row',
                    style={'width': '100%', 'height': 200},
                    value = job['description'],
                    readOnly=onlyRead,
                    className = "inputSmall",
        ),
            ),
        ],
        className = "inputSmall",
    )

    benefits_input = dbc.Row(
        [  
            dbc.Label("Job Benefits", html_for = "benefits_row", width = 2),
            dbc.Col(
                dcc.Textarea(
                    id='benefits_row',
                    style={'width': '100%', 'height': 200},
                    value = job['benefits'],
                    readOnly=onlyRead,
                    className = "inputSmall",
        ),
            ),
        ],
        className = "inputSmall",
    )

    keywords_input = dbc.Row(
        [  
            dbc.Label("Job Keywords", html_for = "keywords_row", width = 2),
            dbc.Col(
                dcc.Textarea(
                    id='keywords_row',
                    style={'width': '100%', 'height': 200},
                    value = job['keywords'],
                    readOnly=onlyRead,
                    className = "inputSmall",
        ),
            ),
        ],
        className = "inputSmall",
    )

    message = html.Div(id = "confirmation", children = "")


    submitButton = html.Div(
        html.Button("Submit", id='submit_button',  className = "button", n_clicks=0)
        )

    
    if (mode == 'view'):
        form = dbc.Form([jobTitle_input, company_input, location_input, workHours_input, wageAmount_input, jobDescription_input, jobQualifications_input, benefits_input,keywords_input, message])
    
    else:
        form = dbc.Form([jobTitle_input, company_input, location_input, workHours_input, wageAmount_input, jobDescription_input, jobQualifications_input, benefits_input,keywords_input, submitButton, message])
        
        
        
    return html.Div(
        form
    )    

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
    
    if (screenMode == "edit"):
        newJob.id = jobID
        dataAccess.updateJob(job)
    
    else:
        dataAccess.createJob(job)
    
    
        return "You have successfully created the job posting. Please wait for the admin to approve or decline the posting."
    
#if __name__ == '__main__':
#    app.run(debug=True)
  

