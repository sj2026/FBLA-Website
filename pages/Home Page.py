import dash
from dash import html
import dash_bootstrap_components as dbc

#keep this
dash.register_page(__name__, path='/home') 

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

layout = html.Div(
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

        
        html.Nav(
            style={
              
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",                 # style and look for navbar
                "alignItems": "center",},
                
                 children=[
                 html.A("Home", href="home", className="navbar"),
                html.A("View Jobs", href="jobs", className="navbar"),                   # navbar buttons
                html.A("Sign Up", href="signup", className="navbar"),
                html.A("Post a Job", href="createposting", className="navbar"),
                html.A("Contact Us", href="contactus", className="navbar"),]
                
                
                ),

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
                    "Please sign up to view job postings.",
                    style={
                        "fontSize": "20px",
                    }
                ),
                
            ]
        ),
         form
    ]
)