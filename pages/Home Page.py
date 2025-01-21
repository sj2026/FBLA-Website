import dash
from dash import html

# keep this
dash.register_page(__name__, path='/')

layout = html.Div(
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
                        "fontSize": "3.5vw",  # title
                        "textAlign": "left",
                    }
                ),
            ]
        ),

        # Navigation Bar
        html.Nav(
            style={
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",  # style and look for navbar
                "alignItems": "center",
                "fontSize": "2vw",  
            },
            children=[
                html.A(
                    "Home", href="/", className="navbar", 
                    style={"fontSize": "1.5vw"}
                ),
                html.A(
                    "Sign Up", href="/signup", className="navbar", 
                    style={"fontSize": "1.5vw"}
                ),
                html.A(
                    "Sign In", href="/signin", className="navbar", 
                    style={"fontSize": "1.5vw"}
                ),
            ]
        ),

        html.Div(
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
                        "fontSize": "1.5vw",  
                        "marginBottom": "20px",  # margin to space out text
                    }
                ),
                html.A(
                    "Start Here",
                    href="signup",  
                    className="button",
                    style={
                        "display": "inline-block",
                        "padding": "10px 20px",
                        "fontSize": "1.5vw",
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
                "left": "5%",               # position and stuff for our mission section
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
                html.H2("Our Mission:", style={
                    "fontSize": "2.5vw",  
                    "color": "#549fc7"
                }),
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

        # Quote From Our Principal 
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
                html.H2("Quote From Our Principal:", style={
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
                  '  not only for jobs they are qualified for now, but also for jobs that they may be interested in, in the future." ' ,
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
                "top": "190%",               # second image
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
                    src="/assets/professional.webp",  
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
                "fontSize": "2vw",  
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
                    className="footer",                       # links to the contact us for email
                    style={
                        "fontSize": "1.5vw", 
                        "marginRight": "20px",
                    }
                ),
                html.A(
                    "Sanjay Jagadeesh",  
                    href="mailto:sanjayjagadeesh2021@gmail.com",  
                    className="footer",
                    style={
                        "fontSize": "1.5vw", 
                    }
                ),
            ],
        ),
    ]
)
