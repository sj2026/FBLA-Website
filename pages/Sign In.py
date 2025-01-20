import dash
from dash import  Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User
from db import ConnectionUtil
from beans.Session import Session

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path="/signin")


username_input = dbc.Row(
    [
        dbc.Label("Username", html_for = "username_input", width = 2),
        dbc.Col(
            dbc.Input(
                type = "username",
                id = "username_input",
                placeholder = "Enter your username",
                className = "inputMedium"
            ),
            width = 10
        ),
    ],
    className = "input",  
)

password_input = dbc.Row(
    [
        dbc.Label("Password", html_for = "password_input", width = 2),
        dbc.Col(
            dbc.Input(
                type = "password",
                id = "password_input",
                placeholder = "Enter your password",
                className = "inputMedium"
            ),
            width = 10,
        ),
    ],
    className = "input",
)


message = html.Div(id = "finalMessage", children = "")


submitButton = html.Div(
    html.Button("Submit", id='submit_button_Signin',  className="button", n_clicks=0)
    )

form = dbc.Form([username_input, password_input, submitButton, message], style={"textAlign": "center"})

def layout(**kwargs):

    return html.Div([
    html.P('Sign In:', style={"textAlign": "center"}, className='important'),
    
    form,
    
    html.Div(id = "redirectOutput") 
    ])

@callback(
    [Output('session', 'data'), Output("redirectOutput", 'children')],
    Input('submit_button_Signin', 'n_clicks'),
    State('password_input', 'value'),
    State('username_input', 'value'),
    prevent_initial_call = True,

)

def onSubmit(clicks, password, username):
    dataAccess = UserDataAccess()
    if (username):
        result = dataAccess.doesUserExist(username,password)
        
        if (result > 0):
            session = Session()
            session.id = result
            session.userStatus = dataAccess.getUserStatus(result)
            session.loggedIn = True
            return [session.to_dict(), dcc.Location(pathname="/", id="locationID")]
        
        
    session = Session()
    session.loggedIn = False
    return [session.to_dict(), ""]
    
     
#if __name__ == '__main__':
#    app.run(debug=True)
  

