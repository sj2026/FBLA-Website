import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dmc.MantineProvider(

           
    
    children=[
        dcc.Location(id='url', refresh=True),
        dcc.Store(id = "session", storage_type="session"),
        html.Div(html.Label("", id="tempHolder")),
        
    
        html.Div([
    ]),
    dash.page_container
])


if __name__ == '__main__':
    app.run(debug=True)
