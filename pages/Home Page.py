from collections import Counter
import dash
from dash import html, callback, Input, Output, State, dcc,ctx
import dash_bootstrap_components as dbc
from dash_holoniq_wordcloud import DashWordcloud
from db.JobDataAccess import JobDataAccess
from pages import PageUtil

"""
This code provides the home page content.
"""

dash.register_page(__name__, path='/') 

global textColor
global textSize
global backgroundColor

textSize = 22
textColor = "black"
backgroundColor = "#FFFDF2"

#Counts number of keywords in job postings
def count_keywords():
    texts = []
    jobDataAccess = JobDataAccess() #connects to database
    jobs = jobDataAccess.getJobs("Approved") #gets all approved jobs
    #print(jobs)
    for index, row in jobs.iterrows():
        texts.append(row['keywords']) #Takes all keywords from job postings
    
    words_list  = [] #list of words
    for text in texts:
        words = text.split(',') #Splits entered keywords into individual words
        for word in words:
            words_list.append(word.strip()) #adds keywords to list
    
    word_counts = Counter(words_list) #counts the number of times a word appears in list
    
    keywords = []
    for key in word_counts.keys():
      keywords.append([key,word_counts[key]])
    #print(keywords)
    return keywords #returns keywords

#Returns size of text depending on frequency of keywords appearance in job posting
def normalise(lst, vmax=50, vmin=16):
    if (len(lst)<=0): return lst
    lmax = max(lst, key=lambda x: x[1])[1]
    lmin = min(lst, key=lambda x: x[1])[1]
    vrange = vmax-vmin
    lrange = lmax-lmin or 1
    for entry in lst:
        entry[1] = int(((entry[1] - lmin) / lrange) * vrange + vmin)
    return lst

def layout(**kwargs):
    """
    Defines the content for the home page.
    Embeds the content inside the template for the website.

    Returns: Dash HTML tags to display.
    """
   
    jobSearch_input = dbc.Row(
        [
            dbc.Col(
                dbc.Input(
                    type="text",  
                    id="jobSearch_row",
                    placeholder="Search For a Job Title, Company, etc",
                    className="form-control",
                    disabled=False,
                    style={  "backgroundColor": 'white',  
                                            "color": 'black',  
                                            "borderColor": textColor,  
                                            "fontFamily": "Garamond",  
                                            "fontSize": textSize,  
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

    
    # Word cloud
    word_cloud = html.Div(
        
    id = "wordcloud_div", #word cloud id
    style = {
        'cursor': 'pointer', #allows you to click word cloud
        
    },
    children = [
    html.Header([
        
        #makes word cloud (sets variables)
        DashWordcloud(
            id='wordcloud',
            list=normalise(count_keywords()),
            width=400, height=300,
            gridSize=14,
            color= textColor,
            backgroundColor= backgroundColor,
            shuffle=False,
            rotateRatio=0,
            shrinkToFit=True,
            shape='circle',
            hover=False,
            ),
            html.H4("", id="report")
        ], className="App-header"),
    ], className ="App")
    
    global form
    form_tmp = html.Div(
        style={

                },
        children = [
            dbc.Form([jobSearch_input, searchButton], style={"textAlign": "center"})
        ]
    )
    form = html.Div(
        style={  "backgroundColor": backgroundColor,  
                "color": textColor,  
                "fontFamily": "Garamond",  
                "fontSize": textSize,  
                "width": "100%",  
                "textAlign": "center",  
                "marginTop": "0px",  
                'display': 'flex',
                'flexDirection': 'row',
                'justifyContent': 'space-evenly',
                'alignItems': 'center',
                
        },
        children = 
        [
            form_tmp,
            word_cloud
        ]
    )
    
    # main layout structure
    return html.Div(
        style={
            "backgroundColor": backgroundColor,
            "minHeight": "300vh",
            "padding": "0",
            "color": textColor,
            "margin": "0",
            "border": "10px double " + textColor,
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
                            alt = "Website Logo. Shows image of a blue wolf (mascot of Sun Prairie West High School).",
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
                            "fontSize": textSize + 20,
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
                    "paddingTop": "5%",
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
                        alt = "Website Logo. Shows image of a blue wolf (mascot of Sun Prairie West High School).",
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
                    "backgroundColor": backgroundColor,
                    "padding": "20px",
                    "borderRadius": "10px",
                    "border": "3px solid " + textColor,  
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",  
                    "boxSizing": "border-box",  
                },
                children=[
                    html.H2("Our Mission:", style={"fontSize": "2.5vw", "color": "#0f9ae6","fontWeight": "bold",}),
                    html.H3(
                        "When we first entered high school as freshmen, finding a job was not an easy task. "
                        "There were limited resources for students to find a job, and the process of searching for job opportunities "
                        "often felt overwhelming and time-consuming. We are determined to change that. With this website, our mission is to "
                        "make finding a job easier and more accessible for current and future students at Sun Prairie West High School. "
                        "We want to make searching for a job easier than ever before, help them gain valuable work experience, and "
                        "ultimately help students find their lifelong passion.",
                        style={
                            "fontSize": textSize,
                            "width": "100%",
                            "textAlign": "left",
                            "marginTop": "20px",
                            "color": textColor,
                        }
                    ),
                ]
            ),

            # quote section
            html.Div(
                style={
                    "position": "absolute",
                    "top": "183%", 
                    "left": "5%",
                    "width": "40%",
                    "backgroundColor": backgroundColor,
                    "padding": "20px",
                    "borderRadius": "10px",
                    "border": "3px solid " + textColor,  
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",  
                    "boxSizing": "border-box",  
                },
                children=[
                    html.H2(" Principal's Message: ", style={
                        "fontSize": "2.5vw",  
                        "color": "#0f9ae6",
                        "fontWeight": "bold"
                    }),                
                    html.H3(
                        "We asked our principal about her thoughts on job application websites like ours, and how they can benefit high school students looking for work. "
                        "Here is what she had to say:",
                        style={
                            "fontSize": textSize,  
                            "width": "100%",               
                            "textAlign": "left",        
                            "marginTop": "20px",    
                            "color": textColor,    
                        }
                    ),
                    html.H3(
                        '"Job application websites can help students learn about the incredible opportunities in our community, '
                      'not only for jobs they are qualified for now, but also for jobs that they may be interested in, in the future."',
                        style={
                            "fontSize": textSize,  
                            "width": "100%",               
                            "textAlign": "left",        
                            "marginTop": "10px",    
                            "color": textColor,    
                        }
                    ),
                    html.H4("- Principal Jennifer Ploeger, Sun Prairie West High School", style={
                        "fontSize": textSize,  
                        "color": textColor,
                        "textAlign": "left",
                        "marginTop": "10px",
                    })
                ]
            ),

            html.Div(
                style={
                    "position": "absolute",
                    "top": "185%",               # second image
                    "right": "5%",            
                    "width": "40%",            
                    "display": "flex",                    
                    "alignItems": "center",    
                    "justifyContent": "center",
                    "backgroundColor": textColor,
                    "padding": "10px",  
                    "borderRadius": "10px",
                },
                children=[
                    html.Img(
                        src="/assets/jobfair.jpg",  
                        alt = "shows an image of a high school job fair (where companies come and advertise to students).",
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
                    "backgroundColor": textColor,
                    "color": backgroundColor,
                    "textAlign": "center",
                    "padding": "20px",
                    "fontSize": textSize,
                    "width": "100%",
                    "borderTop": "5px solid #0f9ae6",
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
                            "fontSize": textSize,
                            "color": backgroundColor,
                        }
                    ),
                    html.H4(
                        children=[ 
                            html.Span(
                                "Contact Us - ",
                                style={
                                    "color": backgroundColor,
                                    "fontWeight": "bold",
                                }
                            ),
                            "We're here to help! Feel free to reach out with any questions or inquiries.",
                        ],
                        style={
                            "color": backgroundColor,
                            "marginBottom": "5px",
                            "fontSize": textSize,
                        }
                    ),
                    html.A(
                        "Lead Designer - Darsh Rewri",
                        href="mailto:darsh.rewri@gmail.com",
                        className="footer",
                        style={
                            "marginRight": "20px",
                            "fontSize": textSize,
                        }
                    ),
                    html.A(
                        "Lead Developer - Sanjay Jagadeesh",
                        href="mailto:sanjayjagadeesh2021@gmail.com",
                        className="footer",
                        style={
                            "fontSize": textSize,
                        }
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
    """
    Handles the intial load of the page.

    Args:
        data : session data.
    
    Returns: Menu to be displayed based on the session data. 
    E.g. The student menu for a student.
    
    """
    print("In home page initial load")
    session = data
    
    if (session):
        global textSize
        global textColor
        global backgroundColor

        textSize = session['textSize']
        textColor = session['textColor']
        backgroundColor = session['backgroundColor']
        #print(session)
        #print(backgroundColor)

    return PageUtil.getMenu(session)
    

@callback(
    Output("main_content", "children"),
    Input('session', 'data'),
)
def update_content(data):
    """
    Provides the page content based on the user login status

    Args:
        data : session data.
    
    Returns: content to display based on user login status.
    
    """
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
                    "Discover your next opportunity with Sun Prairie West Job Search! "
                    "Sign up or sign in today to start your job search journey!",
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
                                "backgroundColor": "#0f9ae6", 
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
    Input(component_id='wordcloud', component_property='click'),
    State('jobSearch_row', 'value'),
    prevent_initial_call=True, 
)

def onSearch(clicks, wordcloud, searchTerm):
    """
    Handles the search and click on word cloud.

    Args:
        wordcloud : wordcloud term clicked.
        searchTerm : search term entered.
    
    Returns: Redirects to view job posting page with the search term
    
    """
    #print("in search")
    trigger_id = ctx.triggered_id
    if trigger_id == "search_button":
        return dcc.Location(pathname="/viewposting/"+ str(searchTerm), id="location_JobID")
    else:
        if(len(wordcloud) > 0):
            term = wordcloud[0]
            return dcc.Location(pathname="/viewposting/"+ str(term), id="location_JobID")
        

