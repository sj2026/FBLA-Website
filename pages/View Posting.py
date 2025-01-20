import dash
from dash import Dash, dash_table, html, dcc, Input, Output, State, callback
import pandas as pd
from db.Searcher import Searcher
from beans.Job import Job

dash.register_page(__name__, path_template='/viewposting/<searchTerm>')

dataAccess = Searcher()


def layout (searchTerm = None):
    if searchTerm:
        df = dataAccess.search(searchTerm)
        df = df.drop(['keywords'], axis=1)
        return html.Div(
        dash_table.DataTable(
            id = 'job-view-table',
            data = df.to_dict('records'), 
            columns = [
                #{"id": 'id', "name": "Job ID", 'editable' : False},
                {"id": 'title', "name": "Job Title", 'editable' : False},
                {"id": 'company', "name": "Company Name", 'editable' : False},
                {"id": 'location', "name": "Job Location", 'editable' : False},
                {"id": 'description', "name": "Description", 'editable' : False},
                {"id": 'workHours', "name": "Work Hours", 'editable' : False},
                {"id": 'wageAmount', "name": "Wage Amount", 'editable' : False},
            ],
        
            style_as_list_view=True,
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
             },
            style_cell_conditional=[
            {'if': {'column_id': 'description'},
            'width': '30%'}
            ],
        
        
        sort_action = "native",
        sort_mode = "single",
        page_action = "native",
        page_current = 0,
        page_size = 10
        ))
    

