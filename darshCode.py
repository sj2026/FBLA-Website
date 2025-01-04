import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#1e225a", 
        "height": "100vh",
        "padding": "20px",
        "color": "lightblue",
        "border": "10px double lightblue "
        
    },
    children=[
        html.H1("Welcome to Our Version of Indeed", style={"textAlign": "center"}),

        html.H2("Darsh Rewri and Sanjay Jagadeesh", style={"textAlign": "center"}),

        html.Nav(
            style={
              
                "padding": "10px",
                "display": "flex",
                "justifyContent": "space-around",
                "alignItems": "center",},
                
                 children=[
                html.A("Home", href="#", style={"color": "lightblue", "textDecoration": "none", "fontSize": "18px"}),
                html.A("Jobs", href="#jobs", style={"color": "lightblue", "textDecoration": "none", "fontSize": "18px"}),
                html.A("Login", href="#login", style={"color": "lightblue", "textDecoration": "none", "fontSize": "18px"}),
                html.A("Contact Us", href="#contact", style={"color": "lightblue", "textDecoration": "none", "fontSize": "18px"}), ]
              
                
                
                ),

        html.P(" This is our website for Sun Prairie West High School job searching", style={"textAlign":"left" }),

       

       
    ]

)
if __name__ == "__main__":
    app.run_server(debug=True)