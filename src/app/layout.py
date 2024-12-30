import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from data.data import df

import dash_bootstrap_components as dbc

fig1 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Create the second figure
fig2 = px.line(df, x="Fruit", y="Amount", color="City")


def generate_table(dataframe, max_rows=10):
    return html.Table(
        [
            html.Thead(html.Tr([html.Th(col) for col in dataframe.columns])),
            html.Tbody(
                [
                    html.Tr(
                        [html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]
                    )
                    for i in range(min(len(dataframe), max_rows))
                ]
            ),
        ]
    )


fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Define the vertical navbar
navbar = dbc.Nav(
    [
        dbc.NavLink("Home", href="#", active="exact"),
        dbc.NavLink("Page 1", href="#", active="exact"),
        dbc.NavLink("Page 2", href="#", active="exact"),
    ],
    vertical=True,
    pills=True,
)


layout2 = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            [
                dbc.Col(navbar, width=2),  # Add the navbar here
                dbc.Col(
                    html.H1(
                        children="Hola mundo",
                        style={"textAlign": "center"},
                    ),
                    width=12,
                ),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children="Dash: A web application framework for Python.",
                    style={"textAlign": "center"},
                ),
                width=12,
            )
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="graph-1", figure=fig1), width=6),
                dbc.Col(dcc.Graph(id="graph-2", figure=fig2), width=6),
                dbc.Button(),
            ],
        ),
        dbc.Row(
            [
                dbc.Label(className="fa fa-moon", html_for="switch"),
                dbc.Switch(
                    id="switch",
                    value=True,
                    className="d-inline-block ms-1",
                    persistence=True,
                ),
                dbc.Label(className="fa fa-sun", html_for="switch"),
            ]
        ),
    ],
)

# Create the first figure
fig1 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Create the second figure
fig2 = px.line(df, x="Fruit", y="Amount", color="City")

# Define the vertical navbar
navbar = dbc.Nav(
    [
        dbc.NavLink("Home", href="#", active="exact"),
        dbc.NavLink("Page 1", href="#", active="exact"),
        dbc.NavLink("Page 2", href="#", active="exact"),
    ],
    vertical=True,
    pills=True,
)

# Define the layout
layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            children="Hola mundo",
                            style={"textAlign": "center"},
                        ),
                        html.Div(
                            children="Dash: A web application framework for Python.",
                            style={"textAlign": "center"},
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            dcc.Graph(id="graph-1", figure=fig1)
                                        ),
                                        className="mb-4",
                                    ),
                                    width=3,
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        children=[
                                            dbc.CardHeader("Graph 2"),
                                            dbc.CardBody(
                                                dcc.Graph(id="graph-2", figure=fig2)
                                            ),
                                            dbc.CardFooter(
                                                "this is a graph description"
                                            ),
                                        ],
                                        className="mb-4",
                                    ),
                                    width=3,
                                ),
                            ],
                        ),
                    ],
                    width=10,
                ),
            ],
        ),
    ],
)
