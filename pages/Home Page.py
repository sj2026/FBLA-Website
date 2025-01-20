import dash
from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc


#keep this
dash.register_page(__name__, path='/') 


def layout(**kwargs):

    jobSearch_input = dbc.Row(
    [
            dbc.Col(
                dbc.Input(
                    type = "jobSearch",
                    id = "jobSearch_row",
                    placeholder = "Search For a Job Title, Company, etc",
                    className = "input"
                    
                ),
                width = 10
            ),
        ],
        className = "input",  
    )

    searchButton = html.Div(
        html.Button("Search", id='search_button',  className="button", n_clicks=0)
        )

    form = dbc.Form([jobSearch_input, searchButton], style={"textAlign": "center"})


    return html.Div(
    style={
        "backgroundColor": "#bec2cb", 
        "height": "97vh",
        "padding": "0",
        "color": "#1a1f61",                  # for overall look of website
        "margin":"0",
        "border": "10px double #1a1f61 ",
        "overflow": "hidden",
        "boxSizing":"border-box",
        "fontFamily":"Garamond",
        
    },
    children=[

        html.Div(
            style={
                "display": "flex",  
                "alignItems": "center",
                "justifyContent": "center",    #for the logo and title to be inline
                "width": "100%", 
            },
                  children=[
                
                html.A(
                    href="#",              # so that when you click the logo it redirects to home page. 
                    children=html.Img(
                        src="/assets/logo.png",
                        style={
                            "height": "100px",
                            "width": "auto",  
                            "display": "inline",                   # logo and make it click
                            "marginRight": "20px", 
                            "cursor": "pointer",  
                        }
                    ),
                ),
                html.H1(
                    "Sun Prairie West Job Search", 
                    style={
                        "fontSize": "40px",                 # title
                        "textAlign": "left", 
                    }
                ),
            ]
        ),

        html.Div(id="navbar"),
        
         html.Div(
            style={
                "textAlign": "center",
                "position": "absolute",
                "top": "60%",                                     # so that the paragraph is in the right place
                "left": "50%",
                "transform": "translate(-50%, -50%)",
            },
              children=[
                html.P(
                    "This is our website for Sun Prairie West High School students looking for a job. "
                    "Please sign up or log in to view job postings.",
                    style={
                        "fontSize": "20px",
                    }
                ),
                
            ]
        ),
         form,
         html.Div(id = "redirectToJobs") 
    ]
    )

@callback(
    Output('navbar','children'),
    Input('session','data'),
)
def initial_load(data):
    session = data
    if session and session['loggedIn']:
        if (session['userStatus'] == "Student"):
            return html.Nav(
                style={
                
                    "padding": "10px",
                    "display": "flex",
                    "justifyContent": "space-around",                 # style and look for navbar
                    "alignItems": "center",},
                    
                    children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("Student Profile", href="jobs", className="navbar"),                   # navbar buttons
                    html.A("Sign Out", href="signup", className="navbar"),
                    html.A("Resumes", href="createposting", className="navbar"),
                    html.A("Apply for a job", href="contactus", className="navbar"),]
                    
                    
                    ),
            

        elif (session['userStatus'] == "Employer"):
            return html.Nav(
                style={
                
                    "padding": "10px",
                    "display": "flex",
                    "justifyContent": "space-around",                 # style and look for navbar
                    "alignItems": "center",},
                    
                    children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("Create Job Posting", href="jobs", className="navbar"),                   # navbar buttons
                    html.A("Sign Out", href="signup", className="navbar"),
                    html.A("View Job Applications", href="createposting", className="navbar"),
                    html.A("Contact Us", href="contactus", className="navbar"),]
                    
                    
                    ),

        elif (session['userStatus'] == "Admin"):
            return html.Nav(
                style={
                
                    "padding": "10px",
                    "display": "flex",
                    "justifyContent": "space-around",                 # style and look for navbar
                    "alignItems": "center",},
                    
                    children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("View Users", href="jobs", className="navbar"),                   # navbar buttons
                    html.A("Sign Out", href="signup", className="navbar"),
                    html.A("View Job Postings", href="createposting", className="navbar"),
                    html.A("Contact Us", href="contactus", className="navbar"),]
                    
                    
                    ),
    else:
        return html.Nav(
                style={
                
                    "padding": "10px",
                    "display": "flex",
                    "justifyContent": "space-around",                 # style and look for navbar
                    "alignItems": "center",},
                    
                    children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("View Jobs", href="jobs", className="navbar"),                   # navbar buttons
                    html.A("Sign Up", href="signup", className="navbar"),
                    html.A("Post a Job", href="createposting", className="navbar"),
                    html.A("Contact Us", href="contactus", className="navbar"),]
                    
                    
                    ),


@callback(
    Output("redirectToJobs", 'children'),
    Input('search_button', 'n_clicks'),
    State('jobSearch_row', 'value'),
    prevent_initial_call=True, 
)

def onSearch(clicks, searchTerm):
    return dcc.Location(pathname="/viewposting/"+ str(searchTerm), id="location_JobID")