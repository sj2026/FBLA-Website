import dash
from dash import  Input, Output, html, State, callback
import dash_bootstrap_components as dbc
from db.UserDataAccess import UserDataAccess
from beans.User import User

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path="/signup")

firstName_input = dbc.Row(
    [
        dbc.Label("First Name", html_for = "first_name_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "firstName",
                id = "first_name_row",
                placeholder = "Enter your first name"
            ),
            width = 10
        ),
    ],
    className = "mb-3",  
)

lastName_input = dbc.Row(
    [
        dbc.Label("Last Name", html_for = "last_name_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "lastName",
                id = "last_name_row",
                placeholder = "Enter your last name",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

email_input = dbc.Row(
    [
        dbc.Label("Email", html_for = "email_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "email",
                id = "email_row",
                placeholder = "Enter your email",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

phoneNumber_input = dbc.Row(
    [  
        dbc.Label("Phone Number", html_for = "phone_number_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "phoneNumber",
                id = "phone_number_row",
                placeholder = "Enter your phone number",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

password_input = dbc.Row(
    [  
        dbc.Label("Password", html_for = "password_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "password",
                id = "password_row",
                placeholder = "Create your password",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

username_input = dbc.Row(
    [  
        dbc.Label("Username", html_for = "username_row", width = 2),
        dbc.Col(
            dbc.Input(
                type = "username",
                id = "username_row",
                placeholder = "Create your username",
            ),
            width = 10,
        ),
    ],
    className = "mb-3",
)

message = html.Div(id = "message", children = "")


submitButton = html.Div(
    html.Button("Submit", id='submit_button',  className = "me-1", n_clicks=0)
    )

form = dbc.Form([firstName_input, lastName_input, email_input, phoneNumber_input, password_input, username_input, submitButton, message])


layout = html.Div([
    form   
])

@callback(
    Output('message', "children"),
    Input('submit_button', 'n_clicks'),
    State('first_name_row', 'value'),
    State('last_name_row', 'value'),
    State('email_row', 'value'),
    State('phone_number_row','value'),
    State('password_row', 'value'),
    State('username_row', 'value'),
    prevent_initial_call = True

)

def onSubmit(clicks, firstName, lastName, email, phoneNumber, password, username):
    dataAccess = UserDataAccess()
    
    newUser = User()
    newUser.firstName = firstName
    newUser.lastName = lastName
    newUser.email = email
    newUser.phoneNumber = phoneNumber
    newUser.isAdmin = "False"
    newUser.status = "New"
    newUser.password = password
    newUser.username = username
    
    dataAccess.createUser(newUser)
    
    return "You have been registered. Please wait for the admin to approve you as a student or employer. To sign in again, use your password: '" + password + "' and username: '" + username + "'"
    
#if __name__ == '__main__':
#    app.run(debug=True)
  

