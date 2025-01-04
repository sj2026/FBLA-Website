import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.UserDataAccess import UserDataAccess
from beans.User import User

dash.register_page(__name__, path='/viewusers')

dataAccess = UserDataAccess()

df = dataAccess.getUsers("All")

layout = html.Div([
    dcc.Dropdown(options=[
       {'label': 'All Users', 'value': 'All'},
       {'label': 'New Users', 'value': 'New'},
       {'label': 'All Students', 'value': 'Student'},
       {'label': 'All Employees', 'value': 'Employee'},
   ],
   value='New', 
   id = 'dropDownMenu'),
    
    html.Div(
        dash_table.DataTable(
            id = 'table',
            data = df.to_dict('records'), 
            columns = [
                {"id": 'id', "name": "User ID", 'editable' : False},
                {"id": 'firstName', "name": "User First Name", 'editable' : False},
                {"id": 'lastName', "name": "User Last Name", 'editable' : False},
                {"id": 'username', "name": "User Username", 'editable' : False},
                {"id": 'email', "name": "User Email", 'editable' : False},
                {"id": 'phoneNumber', "name": "User Phone Number", 'editable' : False},
                {"id": 'isAdmin', "name": "Is User Admin", 'presentation' : 'dropdown', 'editable' : True},
                {"id": 'status', "name": "User Status", 'presentation' : 'dropdown', 'editable' : True},
            ],
        
        
        dropdown = {
            'isAdmin': {
                'options': [
                    {'label': 'True', 'value': 'True'},
                    {'label': 'False', 'value': 'False'}
                ]
            },
            'status': {
                'options' : [
                    {'label' : "New", 'value' : 'New'},
                    {'label' : "Student", 'value' : 'Student'},
                    {'label' : "Employee", 'value' : 'Employee'}        
                ]
            }
        },
        
        sort_action = "native",
        sort_mode = "single",
        page_action = "native",
        page_current = 0,
        page_size = 10
        )
    ),
    html.Div(id='table-dropdown-container'),
    html.Div(id='div-result', children = "")
    ]
)

@callback(
    Output('div-result', 'children'),
    [Input('table', 'data'),
     Input('table', 'columns')],
     [
        State("table", "data_previous"),], prevent_initial_call=True
)
def update_tol_db(rows, columns, prev_rows):
    if prev_rows:
        df1 = pd.DataFrame(rows)
        df2 = pd.DataFrame(prev_rows)
        diff = dataframe_difference(df1,df2)
        user = User()
        user.status = diff.iloc[0]['status']
        user.isAdmin = diff.iloc[0]['isAdmin']
        user.id = diff.iloc[0]['id']
        dataAccess.updateUser(user)
    return ""

@callback(
    Output('table', 'data'),
    Input('dropDownMenu', "value")
)
def loadTable(value):
    df = dataAccess.getUsers(value)
    return df.to_dict('records') 


def dataframe_difference(df1: pd.DataFrame, df2: pd.DataFrame):
    """Find rows which are different between two DataFrames."""
    return pd.concat([df1,df2]).drop_duplicates(keep=False) 
