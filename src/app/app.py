import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc
from dash.dependencies import Input, Output
from layout import layout2, layout
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__)

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.SLATE, dbc.icons.FONT_AWESOME]
)
app.layout = layout


if __name__ == "__main__":
    app.run_server(debug=True)
