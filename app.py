import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = html.Div(

           
    
    children=[

        dcc.Store(id = "session", storage_type="session"),
    
        html.Div([
            #html.Div(
        #     dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        # ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])


if __name__ == '__main__':
    app.run(debug=True)
