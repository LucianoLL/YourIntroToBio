"""
Filename: dnaSeqPage.py
Created by: Luciano L. Lorenzana
Date: 9/13/2024
Python 3.11

Desc: The layout for the 'DNA Section' page
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.dnaSeqPageFolder.misMatchCard as mmc
import mainAppAssets.dnaSeqPageFolder.lectureCard as lec
import mainAppAssets.universalAssets as uva

'''
Setting up the page, giving the page a unique title.
'''
dash.register_page(__name__,
                   title="DNA Section")

'''
Importing variable ans assets from the files in the
'dnaSeqPageFolder' directory.
'''
tabCards = dbc.Tabs(children=[
    # dbc.Tab(lec.lecture01,
    #         tab_id="tab01",
    #         label="Lecture 01"),
    dbc.Tab(mmc.misMatchCard,
            tab_id="tab02",
            label="Mismatch Calculator")],
    id="tabs02",
    active_tab="tab02"
)

'''
Placing the tabs into a row.
'''
tabRow = dbc.Row(children=[
    dbc.Col(tabCards,
            width="auto",
            lg=5,
            className="mt-1 border"
            )
])

'''
Laying out the assets for the page.
'''
layout = dbc.Container(children=[
    tabRow,
    uva.siteFooter
])
