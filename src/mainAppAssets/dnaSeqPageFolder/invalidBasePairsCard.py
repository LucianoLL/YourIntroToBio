"""
Filename: misMatchCard.py
Created by: Luciano L. Lorenzana
Date: 11/21/2024
Python 3.12

Disc: All the assets and cards for the
      'Invalid Base Pairs Counter'
"""
import dash
import dash_bootstrap_components as dbc

'''
The above text for the card
'''
tabText = dash.dcc.Markdown(children="""
                            # Invalid Base Pairs Counter
                            """)

'''
Asking how many DNA helix strands
'''
strandAmount = dbc.InputGroup()
