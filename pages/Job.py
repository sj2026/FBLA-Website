import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.JobDataAccess import JobDataAccess
from beans.Job import Job
from pages import PageUtil

"""
This code handles add, edit and viewing of job posting 
"""

dash.register_page(__name__, path_template="/job/<mode>/<job_id>")

# Default job data structure

# standard input style
input_style = {
    "backgroundColor": "#FFFDF2",
    "color": "black",
    "width": "100%",
    "height": "40px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid black",  
    "overflowY": "auto",
    "fontSize": "1.5vw",  
}

# textarea style 
textarea_style = {
    "width": "100%",
    "height": "100px",
    "backgroundColor": "#FFFDF2",
    "color": "black",
    "borderRadius": "5px",
    "padding": "5px",
    "resize": "vertical",  
    "overflowY": "auto",  
    "border": "1px solid black",  
    "fontSize": "1.5vw",
}


navbar = html.Div(
    style={
        "display": "flex",
        
        "alignItems": "center",
        "justifyContent": "space-between",
        "padding": "10px 20px",
        "margin": "10px",
        "backgroundColor": "#FFFDF2",
        "boxSizing": "border-box",
        "overflowY": "auto"
        #"backgroundColor": "#FFFDF2",
            #"padding": "0",
            #"color": "black",
            #"margin": "0",
            #"border": "10px double black",
            #"boxSizing": "border-box",
            #"fontFamily": "Garamond",
            #"display": "flex",
            #"flexDirection": "column",
            #"height": "100%",
            #"overflowY": "auto",
    },
    children=[
        html.A(
            href="/",
            children=html.Img(
                src="/assets/logo.png",
                alt = "Website Logo. Shows image of a blue wolf (mascot of Sun Prairie West High School).",
                style={
                    "height": "80px",
                    "width": "auto",
                    "cursor": "pointer",
                },
            ),
        ),
        html.Div(id="navbar_job"),
        
    ],
)




# Layout function for Job Posting page
def layout(mode=None, job_id=None, **kwargs):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.

    Args:
        mode: Page mode. 
            - Edit - Edit mode
            - View - View mode
            - view_as_student - View mode for student
            - none - new application
        job_id: id of the job

    Returns: Dash HTML tags to display.
    """

    global screenMode
    screenMode = mode

    global jobID
    jobID = job_id

    #global job
    readOnly = ''
    onlyRead = False

    # Set job details for 'view' and 'edit' modes
    job = {}
    print(job_id)
    if job_id is None or job_id == "none" :
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

    elif mode in ("view", "view_as_student", "edit"):
        jobAccess = JobDataAccess()
        jobTemp = jobAccess.getJob(job_id)
        job.update(vars(jobTemp))

    if mode == 'view' or mode == "view_as_student":
        readOnly = "readOnly"
        onlyRead = True

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
                dbc.Label(input_item["label"], html_for=input_item["id"], width=2, style={"color": "#1a1f61", "fontSize": "1.5vw"}),  # Added responsive font size
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
                dbc.Label(textarea_item["label"], html_for=textarea_item["id"], width=2, style={"color": "#1a1f61", "fontSize": "1.5vw"}),  # Added responsive font size
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
    submitButton = html.Div([
        html.Button(
            "Submit",
            id="submit_button_job",
            className="button",
            n_clicks=0,
            style={
                "backgroundColor": "black",
                "color": "#FFFDF2",
                "padding": "10px 20px",
                "border": "none",
                "borderRadius": "5px",
                "cursor": "pointer",
                "fontSize": "1.5vw",  
            },
        ),
        html.Div(id = "confirmation", children = "")
        ],
        style={"textAlign": "center", "marginTop": "20px"},
    )

    
    # apply button
    applyButton = html.Div([
        html.Button(
            "Apply",
            id="apply_button_job",
            className="button",
            n_clicks=0,
            style={
                "backgroundColor": "black",
                "color": "#FFFDF2",
                "padding": "10px 20px",
                "border": "none",
                "borderRadius": "5px",
                "cursor": "pointer",
                "fontSize": "1.5vw",
            },
        ),
        html.Div(id = "redirectToapply"),
        ]
        ,style={"textAlign": "center", "marginTop": "20px"},
        
    )

    form = dbc.Form()
    
    if mode !="view" and mode !="view_as_student":
        form = dbc.Form(input_rows + textarea_rows + [submitButton] )
    if mode == "view_as_student":
        form = dbc.Form(input_rows + textarea_rows + [applyButton] )
    if mode == "view":
        form = dbc.Form(input_rows + textarea_rows)


    content = html.Div(
                children=[
                html.H2("Job Posting", style={"textAlign": "center"}),
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


    #form = dbc.Form(input_rows + textarea_rows + ([submitButton] if mode != "view" else []))
    return PageUtil.getContentWithTemplate("navbar_job", content)
    


@callback(
    Output('navbar_job', 'children'),
    Input('session','data'),
)
def initial_load(data):
    """
    Handles the intial load of the page.

    Args:
        data : session data.
    
    Returns: 
        a) Value for Resume drop down
        b) Menu to be displayed based on the session data. 
    
    """
    global session 
    session = data
    return PageUtil.getMenu(session)


@callback(
    Output('redirectToapply', "children"),
    Input('apply_button_job', 'n_clicks'),
    Input('session', 'data'),
   prevent_initial_call = True
)
def onApply(clicks, data):
    """
    Redirects the control to job application page
    
    """
    return dcc.Location(pathname="/jobapplication/none/"+ str(jobID) + "/none", id="location_applicationID")
    

    
@callback(
    Output('confirmation', "children"),
    Input('submit_button_job', 'n_clicks'),
    State('jobTitle_row', 'value'),
    State('company_row', 'value'),
    State('location_row', 'value'),
    State('workHours_row','value'),
    State('wageAmount_row', 'value'),
    State('jobDescription_row', 'value'),
    State('jobQualifications_row', 'value'),
    State('benefits_row', 'value'),
    State('keywords_row', 'value'),
    State('session', 'data'),
    prevent_initial_call = True

)

def onSubmit(clicks, title, company, location, workHours, wageAmount, description, qualifications, benefits, keywords, data):
    """
    Handles the submit event for the Job.
    
    """
    dataAccess = JobDataAccess()
    session = data
    
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
    newJob.employerID = session['id']
    
    if (screenMode == "edit"):
        newJob.id = jobID
        dataAccess.updateJob(newJob)
        return "Job edited successfully."
    else:
        dataAccess.createJob(newJob)
        return "You have successfully created the job posting. Please wait for the admin to approve or decline the posting."


