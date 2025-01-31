import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.Searcher import Searcher
from beans.Job import Job
from pages import PageUtil

dash.register_page(__name__, path_template='/viewposting/<searchTerm>')

dataAccess = Searcher()

def layout(searchTerm = None):
    if searchTerm:
        df = dataAccess.search(searchTerm)
        if not df.empty:
            df = df.drop(['keywords'], axis=1)

        layout = html.Div(
            dash_table.DataTable(
                id='job-view-table',
                data=df.to_dict('records'),
                columns=[
                    {"id": 'link_student', "name": "View Full Job Posting", 'editable': False, 'presentation': 'markdown'},
                    {"id": 'company', "name": "Company Name", 'editable': False},
                    {"id": 'location', "name": "Job Location", 'editable': False},
                    {"id": 'description', "name": "Description", 'editable': False},
                    {"id": 'workHours', "name": "Work Hours", 'editable': False},
                    {"id": 'wageAmount', "name": "Wage Amount", 'editable': False},
                ],
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
                markdown_options={'link_target': '_self'},
                sort_action="native",
                sort_mode="single",
                page_action="native",
                page_current=0,
                page_size=10
            )
        )

        return PageUtil.getContentWithTemplate("navbar_viewpostings", layout)

@callback(
    Output('navbar_viewpostings', 'children'),
    Input('session', 'modified_timestamp'),
    State('session', 'data'),
)
def initial_load(modified_timestamp, data):
    global session
    session = data
    return PageUtil.getMenu(session)
