import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.UserDataAccess import UserDataAccess
from beans.User import User
from pages import PageUtil

dash.register_page(__name__, path='/viewusers')

dataAccess = UserDataAccess()

df = dataAccess.getUsers("All")

def layout(**kwargs):


    layout = html.Div(
        style={
            "backgroundColor": "#bec2cb",
            "height": "80vh",
            "fontFamily": "Garamond",
        },
        children=[
            dcc.Dropdown(
                options=[
                    {'label': 'All Users', 'value': 'All'},
                    {'label': 'New Users', 'value': 'New'},
                    {'label': 'All Students', 'value': 'Student'},
                    {'label': 'All Employees', 'value': 'Employee'},
                    {'label': "All Admins", 'value': 'Admin'}
                ],
                value='New',
                id='dropDownMenu-adminViewUsers',
                style={
                    "width": "100%",
                    "margin": "20px 0",
                }
            ),
            
            html.Div(
                dash_table.DataTable(
                    id='Usertable',
                    #style_data = {'border': 'none'},
                #style_header = {'display': 'none'},
                data=df.to_dict('records'),
                    columns=[
                        {"id": 'id', "name": "User ID", 'editable': False},
                        {"id": 'firstName', "name": "User First Name", 'editable': False},
                        {"id": 'lastName', "name": "User Last Name", 'editable': False},
                        {"id": 'username', "name": "User Username", 'editable': False},
                        {"id": 'email', "name": "User Email", 'editable': False},
                        {"id": 'phoneNumber', "name": "User Phone Number", 'editable': False},
                        {"id": 'isAdmin', "name": "Is User Admin", 'presentation': 'dropdown', 'editable': True},
                        {"id": 'status', "name": "User Status", 'presentation': 'dropdown', 'editable': True},
                    ],
                    dropdown={
                        'isAdmin': {
                            'options': [
                                {'label': 'True', 'value': 'True'},
                                {'label': 'False', 'value': 'False'}
                            ]
                        },
                        'status': {
                            'options': [
                                {'label': "New", 'value': 'New'},
                                {'label': "Student", 'value': 'Student'},
                                {'label': "Employee", 'value': 'Employee'},
                                {'label': "Admin", 'value': 'Admin'}
                            ]
                        }
                    },
                    sort_action="native",
                    sort_mode="single",
                    page_action="native",
                    page_current=0,
                    page_size=8,
                   style_as_list_view=True,
            style_data={
                'whiteSpace': 'normal',  
                'height': 'auto',  
                  'backgroundColor':'#bec2cb',
            },
            style_cell_conditional=[
                {'if': {'column_id': 'description'}, 'width': '30%'},
            ],
            style_table={
                'fontFamily': 'Garamond',  
                'color': '#1a1f61',  
            },
            style_header={
                'backgroundColor': '#1a1f61',  
                'color': 'white',  
                'fontWeight': 'bold', 
            },
            style_cell={
                'padding': '10px', 
                'textAlign': 'left', 
            },
                )
            ),
            
            html.Div(id='table-dropdown-container'),
            html.Div(id='div-result', children="")
        ]
    )
    
    return PageUtil.getContentWithTemplate("navbar_adminviewusers",layout)

@callback(
    Output('div-result', 'children'),
    [Input('Usertable', 'data'),
     Input('Usertable', 'columns')],
    [State("Usertable", "data_previous")],
    prevent_initial_call=True
)
def update_tol_db(rows, columns, prev_rows):
    if prev_rows:
        df1 = pd.DataFrame(rows)
        df2 = pd.DataFrame(prev_rows)
        diff = dataframe_difference(df1, df2)
        user = User()
        user.status = diff.iloc[0]['status']
        user.isAdmin = diff.iloc[0]['isAdmin']
        user.id = diff.iloc[0]['id']
        dataAccess.updateUser(user)
    return ""

@callback(
    Output('Usertable', 'data'),
    Input('dropDownMenu-adminViewUsers', "value")
)
def loadTable(value):
    df = dataAccess.getUsers(value)
    return df.to_dict('records')

def dataframe_difference(df1: pd.DataFrame, df2: pd.DataFrame):
    return pd.concat([df1, df2]).drop_duplicates(keep=False)


@callback(
    Output('navbar_adminviewusers', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp,data):
    global session
    session = data
    return PageUtil.getMenu(session)
