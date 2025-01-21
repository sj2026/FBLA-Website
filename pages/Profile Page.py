import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/profile')

layout = html.Div(
    style={
        "backgroundColor": "#bec2cb",
        "height": "100vh",
        "padding": "0",
        "color": "#1a1f61",
        "margin": "0",
        "border": "10px double #1a1f61",
        "overflow": "hidden",
        "boxSizing": "border-box",
        "fontFamily": "Garamond",
    },
    children=[
        html.Div(
            style={
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
                "padding": "10px 20px",
                "backgroundColor": "#bec2cb",
            },
            children=[
                html.A(
                    href="/",
                    children=html.Img(
                        src="/assets/logo.png",
                        style={
                            "height": "80px",
                            "width": "auto",
                            "cursor": "pointer",
                        },
                    ),
                ),
                html.Nav(
                    style={
                        "padding": "10px",
                        "display": "flex",
                        "justifyContent": "space-around",
                        "gap": "20px",
                        "alignItems": "center",
                    },
                    children=[
                        html.A("Home", href="/", className="navbar", style={"fontSize": "1.5vw"}),
                        html.A("View Jobs", href="/jobposting/<mode>/<job_id>", className="navbar", style={"fontSize": "1.5vw"}),
                        html.A("Sign Up", href="/signup", className="navbar", style={"fontSize": "1.5vw"}),
                        html.A("Sign In", href="/signin", className="navbar", style={"fontSize": "1.5vw"}),
                        html.A("Post a Job", href="/job/<mode>/<job_id>", className="navbar", style={"fontSize": "1.5vw"}),
                    ]
                ),
            ],
        ),
        html.Div(
            style={
                "textAlign": "center",
                "position": "absolute",
                "top": "53%",
                "left": "50%",
                "transform": "translate(-50%, -50%)",
                "width": "95%",
                "backgroundColor": "none",
            },
            children=[
                html.H2("Your Profile", style={"color": "#1a1f61", "fontSize": "3vw"}),  
                dbc.Form(
                    [
                        dbc.Row(
                            [
                                dbc.Label("Full Name", width=3, style={"fontSize": "1.5vw"}),
                                dbc.Col(
                                    dbc.Input(
                                        type="text",
                                        id="name-input",
                                        placeholder="Enter your full name",
                                        style={
                                            "backgroundColor": "#bec2cb",
                                            "color": "#1a1f61",
                                            "borderColor": "#1a1f61",
                                            "fontSize": "1.5vw",  
                                        },
                                    ),
                                    width=8,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Email", width=3, style={"fontSize": "1.5vw"}),
                                dbc.Col(
                                    dbc.Input(
                                        type="email",
                                        id="email-input",
                                        placeholder="Enter your email",
                                        style={
                                            "backgroundColor": "#bec2cb",
                                            "color": "#1a1f61",
                                            "borderColor": "#1a1f61",
                                            "fontSize": "1.5vw", 
                                        },
                                    ),
                                    width=8,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Resumes", width=3, style={"fontSize": "1.5vw"}),
                                dbc.Col(
                                    dbc.Input(
                                        type="text",
                                        id="resume-input",
                                        placeholder="Enter resume title",
                                        style={
                                            "backgroundColor": "#bec2cb",
                                            "color": "#1a1f61",
                                            "borderColor": "#1a1f61",
                                            "fontSize": "1.5vw", 
                                        },
                                    ),
                                    width=8,
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Ul(id="resume-list", style={"marginTop": "10px", "color": "#1a1f61", "fontSize": "1.5vw"}), 
                        html.Div(
                            dbc.Button(
                                "Save Profile",
                                id="save-profile-btn",
                                className="button",
                                n_clicks=0,
                                style={
                                    "backgroundColor": "#1a1f61",
                                    "color": "white",
                                    "fontSize": "1.5vw",  
                                },
                            ),
                            style={"textAlign": "center", "marginTop": "20px"},
                        ),
                    ]
                ),
            ],
        ),
    ],
)

