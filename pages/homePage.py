"""
Filename: homePage.py
Created by: Luciano L. Lorenzana
Date: 9/6/2024
Python 3.11

Disc: The code to the home page, the first
      page when booting up the app.
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.universalAssets as uva
import mainAppAssets.homePageFolder.homePageText as hpt

'''
This is how we set up the pages, each page
is given a specific title, and only the
home page requires the "path" argument
set to '/'.
'''
dash.register_page(__name__,
                   title="Home",
                   path='/',)

'''
Putting the intro text into a dbc.Card
'''
homeCard = dbc.Card(children=[hpt.introText])

'''
Grouping all the home cards into it's own set of tabs
to click through.
'''
tabCards = dbc.Tabs(children=[
    dbc.Tab(homeCard,
            tab_id="tab01",
            label="Home")],
    id="tabs01",
    active_tab="tab01"
)

'''
Formatting all cards into clickable tabs.
'''
tabRow = dbc.Row(children=[
    dbc.Col(tabCards,
            width="auto",
            lg=5,
            className="mt-1 border"
            )
])

'''
The layout of the home page
'''
layout = dbc.Container(children=[
    tabRow,
    uva.siteFooter
])
