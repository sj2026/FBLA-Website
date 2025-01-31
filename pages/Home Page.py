import dash
from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc

from pages import PageUtil



dash.register_page(__name__, path='/') 

def layout(**kwargs):

   
    jobSearch_input = dbc.Row(
        [
            dbc.Col(
                dbc.Input(
                    type="text",  
                    id="jobSearch_row",
                    placeholder="Search For a Job Title, Company, etc",
                    className="input",
                    disabled=False,
                    style={  "backgroundColor": "#bec2cb",  
                                            "color": "#1a1f61",  
                                            "borderColor": "#1a1f61",  
                                            "fontFamily": "Garamond",  
                                            "fontSize": "1.5vw",  
                                            "padding": "10px",  
                                            "width": "100%",  
                                            "borderRadius": "5px",  
                                            "textAlign": "center",  
                                            "marginTop": "0px",  
                                            "marginBottom": "5px",  
                             }
              ),
                width=15
            ),
        ],
        className="input",  
    )

    searchButton = html.Div(
        html.Button("Search", id='search_button', className="button", n_clicks=0) 
    )

    global form
    form = dbc.Form([jobSearch_input, searchButton], style={"textAlign": "center"})

    # main layout structure
    return html.Div(
        style={
            "backgroundColor": "#bec2cb",
            "minHeight": "300vh",
            "padding": "0",
            "color": "#1a1f61",
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

            # logo and title section
            html.Div(
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "width": "100%",
                },
                children=[
                    html.A(
                        href="/",
                        children=html.Img(
                            src="/assets/logo.png",
                            style={
                                "height": "100px",
                                "width": "auto",
                                "display": "inline",
                                "marginRight": "20px",
                                "cursor": "pointer",
                            }
                        ),
                    ),
                    html.H1(
                        "Sun Prairie West Job Search",
                        style={
                            "fontSize": "4vw",
                            "textAlign": "left",
                        }
                    ),
                ]
            ),

            # navbar 
            html.Div(id="navbar"),

            # main content determined by login status
            html.Div(
                style={
                    "textAlign": "center",
                    "position": "relative",
                    "paddingTop": "10%",
                    "flex": "1",
                },
                children=[
                    # if logged in show form
                    html.Div(id="main_content", children=[]),
                ],
            ),

            # mission section 
            html.Div(
                style={
                    "position": "absolute",
                    "top": "86%",
                    "left": "5%",
                    "width": "40%",
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

            # our mission 
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
                    html.H2("Our Mission:", style={"fontSize": "2.5vw", "color": "#549fc7"}),
                    html.H3(
                        "When we first entered high school as freshmen, finding a job was not an easy task. "
                        "There were limited resources for students to find a job, and the process of searching for job opportunities "
                        "often felt overwhelming and time-consuming. We are determined to change that. With this website, our mission is to "
                        "make finding a job easier and more accessible for current and future students at Sun Prairie West High School. "
                        "We want to make searching for a job easier than ever before, help them gain valuable work experience, and "
                        "ultimately help students find their lifelong passion.",
                        style={
                            "fontSize": "1.5vw",
                            "width": "100%",
                            "textAlign": "left",
                            "marginTop": "20px",
                            "color": "white",
                        }
                    ),
                ]
            ),

            # quote section
            html.Div(
                style={
                    "position": "absolute",
                    "top": "190%", 
                    "left": "5%",
                    "width": "40%",
                    "backgroundColor": "#1a1f61",
                    "padding": "20px",
                    "borderRadius": "10px",
                },
                children=[
                    html.H2(" Principals Message: ", style={
                        "fontSize": "2.5vw",  
                        "color": "#549fc7"
                    }),                
                    html.H3(
                        "We asked our principal about her thoughts on job application websites like ours, and how they can benefit high school students looking for work. "
                        "Here is what she had to say:",
                        style={
                            "fontSize": "1.5vw",  
                            "width": "100%",               
                            "textAlign": "left",        
                            "marginTop": "20px",    
                            "color": "white",    
                        }
                    ),
                    html.H3(
                        '"Job application websites can help students learn about the incredible opportunities in our community, '
                      'not only for jobs they are qualified for now, but also for jobs that they may be interested in, in the future."',
                        style={
                            "fontSize": "1.5vw",  
                            "width": "100%",               
                            "textAlign": "left",        
                            "marginTop": "10px",    
                            "color": "white",    
                        }
                    ),
                    html.H4("- Principal Jennifer Ploeger, Sun Prairie West High School", style={
                        "fontSize": "1.5vw",  
                        "color": "white",
                        "textAlign": "left",
                        "marginTop": "10px",
                    })
                ]
            ),

            html.Div(
                style={
                    "position": "absolute",
                    "top": "192%",               # second image
                    "right": "5%",            
                    "width": "40%",            
                    "display": "flex",                    
                    "alignItems": "center",    
                    "justifyContent": "center",
                    "backgroundColor": "#1a1f61",
                    "padding": "10px",  
                    "borderRadius": "10px",
                },
                children=[
                    html.Img(
                        src="/assets/jobfair.jpg",  
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
                    "fontSize": "1.5vw",
                    "width": "100%",
                    "borderTop": "5px solid #549fc7",
                },
                children=[
                    html.H3(
                        children=[ 
                            html.Span(
                                "Sun Prairie West Job Search | ",
                                style={
                                    "fontWeight": "bold",
                                }
                            ),
                            "2850 Ironwood Dr, Sun Prairie, WI 53590",
                        ],
                        style={
                            "fontSize": "1.5vw",
                            "color": "white",
                        }
                    ),
                    html.H4(
                        children=[ 
                            html.Span(
                                "Contact Us - ",
                                style={
                                    "color": "white",
                                    "fontWeight": "bold",
                                }
                            ),
                            "We're here to help! Feel free to reach out with any questions or inquiries.",
                        ],
                        style={
                            "color": "white",
                            "marginBottom": "5px",
                            "fontSize": "1.5vw",
                        }
                    ),
                    html.A(
                        "Darsh Rewri",
                        href="mailto:darsh.rewri@gmail.com",
                        className="footer",
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
        ]
    )

# navbar based on logged-in user
@callback(
    Output('navbar', 'children'),
    Input('session', 'data'),
)
def initial_load(data):
    session = data
    return PageUtil.getMenu(session)
    

@callback(
    Output("main_content", "children"),
    Input('session', 'data'),
)
def update_content(data):
    session = data
    if session and session['loggedIn']:
        # show job search form if logged in
        return html.Div(
            children=[
                form,
                html.Div(id = "redirectToJobs"),
            ]
        )
    else:
        # show the introductory text and sign-in button if not logged in
        return html.Div(
            children=[
                html.P(
                    "This is our website for Sun Prairie West High School students looking for a job. "
                    "Please sign up or sign in to view job postings.",
                    style={
                        "fontSize": "1.5vw",
                        "marginBottom": "20px",
                    }
                ),
                html.Div(
                    html.A(
                        "Start Here",
                        href="signup",
                        className="button",
                        style={
                                "backgroundColor": "#1a1f61", 
                            "color": "white",  
                            "fontFamily": "Garamond", 
                            "fontSize": "1.5vw",  
                            "padding": "10px 20px",  
                            "border": "none", 
                            "borderRadius": "5px",  
                            "cursor": "pointer",  
                            "marginTop": "0px",  
                            "marginBottom": "10px",  
                        },

                    )
                ),
            ]
        )


@callback(
    Output("redirectToJobs", 'children'),
    Input('search_button', 'n_clicks'),
    State('jobSearch_row', 'value'),
    prevent_initial_call=True, 
)

def onSearch(clicks, searchTerm):
    #print("in search")
    return dcc.Location(pathname="/viewposting/"+ str(searchTerm), id="location_JobID")