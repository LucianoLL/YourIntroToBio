"""
Filename: acidicBasicPage.py
Created by: Luciano L. Lorenzana
Date: 9/19/2024
Python 3.11

Disc: A page dedicated to acids and bases.
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.universalAssets as uva
import mainAppAssets.acidicBasicPageFolder.hydrogenRatioCard as hrc

dash.register_page(__name__,
                   title="Acids and Bases")

tabCards = dbc.Tabs(children=[
    dbc.Tab(hrc.hydrogenRatioCard,
            tab_id="tab02",
            label="Hydrogen Ratio Calculator")],
    id="tabs03",
    active_tab="tab02"
)

tabRow = dbc.Row(children=[
    dbc.Col(tabCards,
            width="auto",
            lg=5,
            className="mt-2 border"
            )
])

layout = dbc.Container(children=[
    tabRow,
    uva.siteFooter
])

