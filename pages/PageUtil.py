from dash import html

def getMenu(session):
    if session and session['loggedIn']:
        if session['userStatus'] == "Student":
            return html.Nav(
                style={
                    "padding": "10px",
                    "display": "flex",
                    "flex-direction" : "row",
                    "justifyContent": "space-around",
                    "alignItems": "center",
                },
                children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("Student Profile", href="/profile/"+ str(session['id']), className="navbar"),
                    html.A("Create Resume", href="/resume/none/none", className="navbar"),
                ]
            )

        elif session['userStatus'] == "Employee":
            return html.Nav(
                style={
                    "padding": "10px",
                    "display": "flex",
                    "justifyContent": "space-around",
                    "alignItems": "center",
                },
                children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("Create Job Posting", href="/job/none/none", className="navbar"),                   # navbar buttons
                    html.A("View Postings", href="/viewcreations/" + str(session['id']), className="navbar"),
                    ]
                    
                    
                    ),

        elif session['userStatus'] == "Admin":
            return html.Nav(
                style={
                    "padding": "10px",
                    "display": "flex",
                    "justifyContent": "space-around",
                    "alignItems": "center",
                },
                children=[
                    html.A("Home", href="/", className="navbar"),
                    html.A("View Users", href="/viewusers", className="navbar"),
                    html.A("View Job Postings", href="/viewjobs", className="navbar"),
                ]
            )
    else:
        return html.Nav(
            style={
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",
                "alignItems": "center",
            },
            children=[
                html.A("Home", href="/", className="navbar"),
                html.A("Sign Up", href="/signup", className="navbar"),
                html.A("Sign In", href="/signin", className="navbar"),
            ]
        )
        
def getContentWithTemplate(navbarId, content):
    return html.Div(
        style={
            "backgroundColor": "#bec2cb",
            "minHeight": "100vh",
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
                            "fontSize": "3.5vw",
                            "textAlign": "left",
                        }
                    ),
                ]
            ),

            # navbar 
            html.Div(id=navbarId),

            # main content determined by login status
            content,
            
            # Footer 



  ],
            ),
        