import dash
from dash import html

dash.register_page(__name__, path='/home')

layout = html.Div([
    html.H1("Welcome to Sun Prairie West's job seach website!", style={"textAlign": "center"}),
    html.Div('This website was created for the 2024 FBLA Website Design & Development contest', style={"textAlign": "center"}),
])