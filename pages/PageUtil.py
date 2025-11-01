import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html
from dash_chat import ChatComponent
from NewChatbot import NewChatbot
from db.JobDataAccess import JobDataAccess
from db.TextToSpeech import TextToSpeech

global chatbot

#Create a chatbot and load the documents
#This code will be called only once when the website is loaded.
chatbot = NewChatbot()
documents = chatbot.createDocuments()
chatbot.sendRequest(documents, "loadDocuments")


global textColor
global textSize
global backgroundColor
global textContent

textContent = "Discover your next opportunity with Sun Prairie West Job Search! Sign up or sign in today to start your job search journey! Start Here. Our Mission: When we first entered high school as freshmen, finding a job was not an easy task. There were limited resources for students to find a job, and the process of searching for job opportunities often felt overwhelming and time-consuming. "
textContent += "We are determined to change that. With this website, our mission is to make finding a job easier and more accessible for current and future students at Sun Prairie West High School. We want to make searching for a job easier than ever before, help them gain valuable work experience, and ultimately help students find their lifelong passion."
textContent += "Principal's Message: We asked our principal about her thoughts on job application websites like ours, and how they can benefit high school students looking for work. Here is what she had to say:"
textContent += " Job application websites can help students learn about the incredible opportunities in our community, not only for jobs they are qualified for now, but also for jobs that they may be interested in, in the future."
textContent += " - Principal Jennifer Ploeger, Sun Prairie West High School."
textContent += "Sun Prairie West Job Search. 2850 Ironwood Dr, Sun Prairie, WI 53590. Contact Us - We're here to help! Feel free to reach out with any questions or inquiries. Lead Designer - Darsh Rewri. Lead Developer - Sanjay Jagadeesh"

textSize = 22
textColor = "black"
backgroundColor = "#FFFDF2"

html.Div(
    html.Label("", id = "tempHolder")
)

def getMenu(session):
    """
    Determines the menu options based on the user logged in.

    Args:
        session : session data.
    
    Returns: Menu to be displayed based on the session data. 
    E.g. The student menu items for a student.
    
    """
    global overallSession
    overallSession = session

    # Define common elements that will appear in all navbars
    common_elements = [
        dbc.Button("Text-To-Speech", id="textToSpeech", n_clicks=0),
        dbc.Button("AI Assistant", id="openAIAssistant", n_clicks=0),
        dbc.Offcanvas(
            ChatComponent(
                id="chat-component",
                messages=[],
                persistence=True,
                persistence_type="local"
            ),
            id="offcanvas",
            title="AI Job Assistant",
            is_open=False,
            placement='end'
        ),
    ]

    if session and session['loggedIn']:
        menu_items = []
        if session['userStatus'] == "Student":
            menu_items = [
                html.A("Home", href="/", className="navbar"),
                html.A("Student Profile", href="/profile/"+ str(session['id']), className="navbar"),
                html.A("Create Resume", href="/resume/none/none", className="navbar"),
                html.A("Settings", href = "/settings", className='navbar')
            ]
        elif session['userStatus'] == "Employee":
            menu_items = [
                html.A("Home", href="/", className="navbar"),
                html.A("Create Job Posting", href="/job/none/none", className="navbar"),
                html.A("View Postings", href="/viewcreations/" + str(session['id']), className="navbar"),
                html.A("Settings", href = "/settings", className='navbar') # Added Settings for Employee
            ]
        elif session['userStatus'] == "Admin":
            menu_items = [
                html.A("Home", href="/", className="navbar"),
                html.A("View Users", href="/viewusers", className="navbar"),
                html.A("View Job Postings", href="/viewjobs", className="navbar"),
                html.A("Settings", href = "/settings", className='navbar') # Added Settings for Admin
            ]
        
        return html.Nav(
            style={
                "padding": "10px",
                "display": "flex",
                "flex-direction" : "row",
                "justifyContent": "space-around",
                "alignItems": "center",
                "backgroundColor": session['backgroundColor'],  
                "color": session['textColor'],
            },
            children=menu_items + common_elements # Combine specific items with common elements
        )
    else:
        return html.Nav(
            style={
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",
                "alignItems": "center",
                "backgroundColor": "#FFFDF2",  
                "color": "black",
            },
            children=[
                html.A("Home", href="/", className="navbar"),
                html.A("Sign Up", href="/signup", className="navbar"),
                html.A("Sign In", href="/signin", className="navbar"),
            ] + common_elements # Combine specific items with common elements
        )
    
@callback(
    Output('tempHolder', 'children'), # Output can be anything, just to trigger the callback
    Input('textToSpeech', 'n_clicks'),
    prevent_initial_call=True, # Prevent initial call if you don't want it to speak on page load
)
def sayText(n_clicks):
    """
    Handles speach to text for the website
    """
    if n_clicks and n_clicks > 0: # Only speak if the button was clicked
        textToSpeech = TextToSpeech()
        textToSpeech.sayText(textContent)
    return "" # Return something for the output

@callback(
    Output("offcanvas", "is_open"),
    Input("openAIAssistant", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(
    Output("chat-component", "messages"),
    Input("chat-component", "new_message"),
    State("chat-component", "messages"),
    prevent_initial_call=False,
)
def handle_chat(new_message, messages):
    """
    Handles chatbot dialog
    """
    if not new_message:
        updated_messages = []
        if len(messages)==0:
            updated_messages=[{"role": "assistant", "content": "Hi!\n\nI am JobAI, your personal job assistant. I can help you navigate this website and answer any questions you may have.\n\nWhat would you like to know?"}]
        return updated_messages

    updated_messages = messages + [new_message]

    if new_message["role"] == "user":
        question = {'question': new_message['content']}
        chatbotAnswer = chatbot.sendRequest(question, "answerQuestion")
        chatbotAnswer = chatbotAnswer['answer']
        
        #print(chatbotAnswer)

        bot_response = {"role": "assistant", "content": chatbotAnswer}
        return updated_messages + [bot_response]

    return updated_messages
    
        
def getContentWithTemplate(navbarId, content):
    """
    Embeds the given content in the page template.
    Args:
        navbarId : id of the navigtion bar to display the menu.
        content: content to be displaed.
    """
    global textContent # Ensure textContent is accessible within this function if needed
    return html.Div(
        style={
            "backgroundColor": overallSession['backgroundColor'],
            "minHeight": "100vh",
            "padding": "0",
            "color": overallSession['textColor'],
            "margin": "0",
            "border": "10px double " + overallSession['textColor'],
            "boxSizing": "border-box",
            "fontFamily": "Garamond",
            'fontSize': overallSession['textSize']-5,
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
            )