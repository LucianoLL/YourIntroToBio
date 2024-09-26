"""
Filename: lectureCard.py
Created by: Luciano L. Lorenzana
Date: 9/19/2024
Python 3.11

Disc: Holds text for any lecture material for
      the 'DNA Section' page.
"""
import dash
import dash_bootstrap_components as dbc

'''
Meant to be a quick lecture on DNA sequences and structure.
'''
lecText01 = dash.dcc.Markdown(children=
                              """
                              ### Quick Lecture
                              DNA (Deoxyribonucleic acid) is portrayed as
                              double helix structure holding pairings composed of:
                              * Adenine (A)
                              * Guanine (G)
                              * Cytosine (C)
                              * Thymine (G)
        
                              And each of these chemicals have set pairings:
                              * A - T
                                  * T - A
                              * G - C
                                  * C - G
        
                              The sequence of these patterns are unique to each
                              individual being, which is what this concept 
                              contributes to, identification. It's also important
                              to note that when portraying DNA, only one
                              strand is necessary since the set pairing can tell
                              us what the other strand will be like.
                              """,
                              mathjax=True
                              )

'''
A temporary card until I can verify any lecture material text.
'''
tbdCard = dash.dcc.Markdown(children="TBD")

'''
The card for the lecture material in the DAN page.
'''
lecture01 = dbc.Card(children=[
    # lecText01,
    tbdCard
])
