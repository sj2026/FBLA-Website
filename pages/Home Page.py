import dash
from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc

<<<<<<< HEAD
# keep this
dash.register_page(__name__, path='/')

layout = html.Div(
=======

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
>>>>>>> 22d810a160b1d39e509d7ad6fbb0075682f55579
    style={
        "backgroundColor": "#bec2cb",
        "minHeight": "300vh", 
        "padding": "0",
        "color": "#1a1f61",    # for overall look and style of website
        "margin": "0",
        "border": "10px double #1a1f61",
        "boxSizing": "border-box",
        "fontFamily": "Garamond",
        "display": "flex",    
        "flexDirection": "column",
        "height": "100%",       
        "overflowY": "auto",  
    },
    children=[

        html.Div(
            style={
                "display": "flex",  
                "alignItems": "center",
                "justifyContent": "center",  # for the logo and title to be inline
                "width": "100%",
            },
            children=[

                html.A(
                    href="/",  # so that when you click the logo it redirects to the home page.
                    children=html.Img(
                        src="/assets/logo.png",
                        style={
                            "height": "100px",
                            "width": "auto",  
                            "display": "inline",                   # logo and make it clickable
                            "marginRight": "20px",
                            "cursor": "pointer",  
                        }
                    ),
                ),
                html.H1(
                    "Sun Prairie West Job Search",
                    style={
                        "fontSize": "40px",  # title
                        "textAlign": "left",
                    }
                ),
            ]
        ),

<<<<<<< HEAD
        html.Nav(
            style={
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",  # style and look for navbar
                "alignItems": "center",
            },
            children=[
                html.A("Home", href="/", className="navbar"),
                html.A("View Jobs", href="/jobposting/<mode>/<job_id>", className="navbar"),
                html.A("Sign Up", href="/signup", className="navbar"),
                html.A("Sign In", href="/signin", className="navbar"),
                html.A("Post a Job", href="/job/new/none", className="navbar"),
            ]
        ),

        html.Div(
=======
        html.Div(id="navbar"),
        
         html.Div(
>>>>>>> 22d810a160b1d39e509d7ad6fbb0075682f55579
            style={
                "textAlign": "center",
                "position": "relative",     # spacing and scrollability for page
                "paddingTop": "10%",  
                "flex": "1",
            },
            children=[
                html.P(
                    "This is our website for Sun Prairie West High School students looking for a job. "
                    "Please sign up or sign in to view job postings.",
                    style={
                        "fontSize": "20px",
                        "marginBottom": "20px",  # margin to space out text
                    }
                ),
<<<<<<< HEAD
                html.A(
                    "Start Here",
                    href="signup",  
                    className="button",
                    style={
                        "display": "inline-block",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "backgroundColor": "#1a1f61",  # so that the button looks right and is linked
                        "color": "white",
                        "borderRadius": "5px",
                        "textDecoration": "none",
                        "cursor": "pointer",
                        "transition": "0.3s",  
                    },
                ),
            ],
        ),
        
       
        html.Div(
            style={
                "position": "absolute",
                "top": "88%",             
                "left": "5%",              
                "width": "40%",                      # position and stuff for our mission section
                "display": "flex",        
                "alignItems": "center",    
                "justifyContent": "center",
            },
            children=[
                html.Img(
                    src="/assets/logo.png",  
                    style={
                        "width": "97%",  
                        "height": "auto",  
                    }
                ),
            ]
        ),
        
        # Our Mission Section
        html.Div(
            style={
                "position": "absolute",
                "top": "100%",            
                "right": "5%",             
                "width": "40%",            
                "backgroundColor": "#1a1f61",  
                "padding": "20px",      
                "borderRadius": "10px",  
            },
            children=[
                html.H2("Our Mission:", style={"fontSize": "35px", "color": "#549fc7"}),
                html.H3(
                    "When we first entered high school as freshmen, finding a job was not an easy task. "
                    "There were limited resources for students to find a job, and the process of searching for job opportunities "
                    "often felt overwhelming and time-consuming. We are determined to change that. With this website, our mission is to "
                    "make finding a job easier and more accessible for current and future students at Sun Prairie West High School. "
                    "We want to make searching for a job easier than ever before, help them gain valuable work experience, and "
                    "ultimately help students find their lifelong passion.",
                    style={
                        "fontSize": "20px",  
                        "width": "100%",              
                        "textAlign": "left",        
                        "marginTop": "20px",    
                        "color": "white",     
                    }
                ),
            ]
        ),

        html.Div(
            style={
                "position": "absolute",
                "top": "190%",            
                "left": "5%",          
                "width": "40%",                                  # second section position and stuff
                "backgroundColor": "#1a1f61",  
                "padding": "20px",      
                "borderRadius": "10px",  
            },
            children=[
                html.H2("Yap Section 2:", style={"fontSize": "35px", "color": "#549fc7"}),                
                html.H3(
                    " Add quote here from someone important and maybe talk to principal JP and get a quote from her.",
                    style={
                        "fontSize": "20px",  
                        "width": "100%",              
                        "textAlign": "left",        
                        "marginTop": "20px",    
                        "color": "white",     
                    }
                ),
            ]
        ),

        
        html.Div(
            style={
               "position": "absolute",
        "top": "190%",              
        "right": "5%",             
        "width": "40%",            
        "display": "flex",                    #second image
        "alignItems": "center",    
        "justifyContent": "center",
        "backgroundColor": "#1a1f61", 
        "padding": "10px",  
        "borderRadius": "10px", 
            },
            children=[
                html.Img(
                    src="/assets/temporaryimage.jpg",  
                    style={
                        "width": "100%",  
                        "height": "auto",  
                        "borderRadius":"10px",
                    }
                ),
            ]
        ),

        # Footer
        html.Footer(
            style={
                "backgroundColor": "#1a1f61",
                "color": "white",
                "textAlign": "center",
                "padding": "20px",  
                "fontSize": "18px",  
                "width": "100%",   
                "borderTop": "5px solid #549fc7", 
            },
           children=[
    html.H3(
        children=[
            html.Span(
                "Sun Prairie West Job Search | ", 
                style={
                    "fontWeight": "bold",  # bold only for the title
                }
            ),
            "2850 Ironwood Dr, Sun Prairie, WI 53590",  
        ],
        style={
            "fontSize": "20px",  # footer text size
            "color": "white",    # text color
        }
    ),
             html.H4(
    children=[
        html.Span(
            "Contact Us - ", 
            style={
                "color": "white",
                "fontWeight": "bold",  # Bold only for "Contact Us"
            }
        ),
        "We're here to help! Feel free to reach out with any questions or inquiries.",
    ],
    style={
        "color": "white",
        "marginBottom": "5px",
        "fontSize": "20px",
    }
),


     
                html.A(
                    "Darsh Rewri",  
                    href="mailto:darsh.rewri@gmail.com", 
                    className="footer",                       # links to the contact us for email
                    style={
                        "marginRight": "20px",
                    }
                ),
                html.A(
                    "Sanjay Jagadeesh",  
                    href="mailto:sanjayjagadeesh2021@gmail.com",  
                    className="footer",
                ),
            ],
        ),
=======
                
            ]
        ),
         form,
         html.Div(id = "redirectToJobs") 
>>>>>>> 22d810a160b1d39e509d7ad6fbb0075682f55579
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