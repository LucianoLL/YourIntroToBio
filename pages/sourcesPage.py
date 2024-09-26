"""
Filename: sourcesPage.py
Created by: Luciano L. Lorenzana
Date: 9/19/2024

Disc: A page that holds all sources and references to
      the information presented in this project
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.sourcesPageFolder.sourcesFile as spff
import mainAppAssets.universalAssets as uva

dash.register_page(__name__,
                   title="Sources and References")

sourceCard = dbc.Card(children=[
    spff.campbellBioSource
])

layout = dbc.Container(children=[
    sourceCard,
    uva.siteFooter
])
