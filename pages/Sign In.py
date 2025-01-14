import dash
from dash import  Input, Output, html, State, callback
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User
from db import ConnectionUtil

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path="/signin")


username_input = dbc.Row(
    [
        dbc.Label("Username", html_for = "username_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "username",
                id = "username_row",
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
        dbc.Label("Password", html_for = "password_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "password",
                id = "password_row",
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
    html.Button("Submit", id='submit_button',  className="button", n_clicks=0)
    )

form = dbc.Form([username_input, password_input, submitButton, message], style={"textAlign": "center"})


layout = html.Div([
    html.P('Sign In:', style={"textAlign": "center"}, className='important'),
    
    form   
])

@callback(
    Output('finalMessage', "children"),
    Input('submit_button', 'n_clicks'),
    State('password_row', 'value'),
    State('username_row', 'value'),
    prevent_initial_call = True

)

def onSubmit(clicks, password, username):
    dataAccess = UserDataAccess()
    
    result = dataAccess.doesUserExist(username,password)
    
    if (result > 0):
        return "You have been signed in!"
    
    else:
        return "Login failed. Check you username, password, or sign up."
    
    
#if __name__ == '__main__':
#    app.run(debug=True)
  

