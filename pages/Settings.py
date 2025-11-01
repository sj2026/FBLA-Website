import dash
from dash import Input, Output, html, State, callback, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

from beans.Session import Session
from pages import PageUtil

"""
This code handles settings page
"""
# Registers page on website (to make it visible)
dash.register_page(__name__, path_template="/settings")


input_style = {
    "backgroundColor": "#FFFDF2",
    "color": "black",
    "width": "80%",
    "height": "25px",
    "borderRadius": "5px",
    "padding": "5px",
    "border": "1px solid black",
    "overflowY": "auto",
    "fontSize": "1.5vw",
}


def layout(**kwargs):
    """
    Defines the content for the page.
    Embeds the content inside the template for the website.

    Returns: Dash HTML tags to display.
    """
    form = dbc.Form(
        [
            # This dbc.Row will contain the Text Size and Switches
            dbc.Row(
                [
                    # Empty column for left spacing (1/4th of the page)
                    dbc.Col(width=3), # Takes 3 columns (1/4 of 12)

                    # Column for Text Size (1/4th of the page)
                    dbc.Col(
                        [
                            html.Div(
                                "Text Size",
                                id="textSizeLabel",
                                style={
                                    "textAlign": "center",
                                    "fontSize": "2vw",
                                    "marginBottom": "15px",
                                },
                            ),
                            daq.NumericInput(
                                id="textSize",
                                value=22,
                                min=0,
                                max=50,
                                style={
                                    "width": "100%",
                                    "textAlign": "center",
                                    "margin": "0 auto",
                                    "fontSize": "1.5vw",
                                },
                                className="daq-numeric-input-custom",
                            ),
                        ],
                        width=2,  # Takes 3 columns (1/4 of 12)
                        className="d-flex flex-column align-items-center justify-content-center py-4",
                    ),

                    # Empty column for middle spacing (between Text Size and Switches)
                    dbc.Col(width=2), # Takes 2 columns. Adjust this to fine-tune spacing

                    # Column for Switches (1/4th of the page)
                    dbc.Col(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Light Mode", "value": 1},
                                    {"label": "Dark Mode", "value": 2},
                                    {"label": "Default", "value": 3},
                                ],
                                value=[1],
                                id="switches-mode",
                                switch=True,
                                className="fs-3 d-grid gap-3 ps-4",
                            ),
                        ],
                        width=2,  # Takes 3 columns (1/4 of 12)
                        className="d-flex flex-column justify-content-center py-4",
                    ),
                    
                    # Empty column for right spacing (remaining 1/4th of the page)
                    dbc.Col(width=1), # The remaining column (3+3+2+3+1 = 12)
                ],
                className="mb-5 align-items-center mx-auto",
            ),
            
            # Submit Button (moved closer to the bottom as requested previously)
            html.Div(
                dbc.Button(
                    "Save Preferences",
                    id="submit_button_settings",
                    className="button",
                    n_clicks=0,
                    style={
                        "backgroundColor": "#0F9AE6",
                        "color": "white",
                        "padding": "10px 20px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "fontSize": "1.5vw",
                    },
                ),
                style={
                    "textAlign": "center",
                    "marginTop": "120px",  # Adjust as needed to push it down
                    "position": "relative",
                    "bottom": "20px",  # Adjust as needed for final positioning
                },
            ),
        ]
    )

    layout = html.Div(
        children=[
            html.H2(
                "Settings",
                style={"fontSize": "3vw", "textAlign": "center", "marginBottom": "30px"},
            ),
            html.Div(
                children=form,
            ),
        ]
    )

    return PageUtil.getContentWithTemplate("navbar_settings", layout)


@callback(
    Output("navbar_settings", "children"),
    Input("session", "modified_timestamp"),
    State("session", "data"),
)
def initial_load(modified_timestamp, data):
    """
    Handles the intial load of the page.

    Args:
        data : session data.
    
    Returns: 
        a) Value for Resume drop down
        b) Menu to be displayed based on the session data. 
    
    """
    session = data
    return PageUtil.getMenu(session)


@callback(Output("switches-mode", "value"), Input("switches-mode", "value"))
def update_checklist(selected_values):
    if not selected_values:
        return []  # Return empty list if nothing is selected
    else:
        return [selected_values[-1]]  # Return only the last selected option


@callback(
    [
        Output("session", "data", allow_duplicate=True),
        Output("url", "pathname", allow_duplicate=True),
    ],
    Input("submit_button_settings", "n_clicks"),
    State("session", "data"),
    State("textSize", "value"),
    State("switches-mode", "value"),
    prevent_initial_call=True,
    # allow_duplicate=True
)
def save_data_to_session(n_clicks, existing_data, newTextSize, mode):
    """
    Saves the settings data to session.
    Redirects the control to home page.
    
    """
    if n_clicks:
        # print(newTextSize)
        existing_data["textSize"] = newTextSize
        # print(mode[0])
        if mode[0] == 1:
            existing_data["textColor"] = "#1D1D1D"
            existing_data["backgroundColor"] = "white"

        elif mode[0] == 2:
            existing_data["textColor"] = "white"
            existing_data["backgroundColor"] = "#1D1D1D"

        else:
            existing_data["textColor"] = "#1D1D1D"
            existing_data["backgroundColor"] = "#FFFDF2"

        # existing_data.update(data_to_save)
        # print(existing_data)

        return [existing_data, "/"]

    return [dash.no_update, dash.no_update]