import dash
from dash import html


#keep this
dash.register_page(__name__, path='/')


layout = html.Div(
    style={
        "backgroundColor": "#bec2cb",
        "height": "100vh",
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
                    href="/",              # so that when you click the logo it redirects to home page.
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


       
        html.Nav(
            style={
             
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",                 # style and look for navbar
                "alignItems": "center",},
               
                 children=[
               html.A("Home", href="/", className="navbar"),
                html.A("View Jobs", href="/jobposting/<mode>/<job_id>", className="navbar"),                   # navbar buttons
                html.A("Sign Up", href="/signup", className="navbar"),
                html.A("Sign In", href="/signin", className="navbar"),
                html.A("Post a Job", href="/job/new/none", className="navbar"),]
               
               
                ),


         html.Div(
            style={
                "textAlign": "center",
                "position": "absolute",
                "top": "55%",                                     # so that the paragraph is in the right place
                "left": "50%",
                "transform": "translate(-50%, -50%)",
            },
              children=[
                html.P(
                    "This is our website for Sun Prairie West High School students looking for a job. "
                    "Please sign up to view job postings.",
                    style={
                        "fontSize": "20px",
                    }
                ),
                html.A(
                    "Start Here",
                    href="signup",  
                    className="button",
                    style={
                        "display": "inline-block",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "backgroundColor": "#1a1f61",       # so that the button looks right and is linked to the same as the login button
                        "color": "white",
                        "borderRadius": "5px",
                        "textDecoration": "none",
                        "cursor": "pointer",
                        "transition": "0.3s",  
                    },
                ),
            ]
        ),
    ]
)
