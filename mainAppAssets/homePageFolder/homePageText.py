"""
Filename: homePageText.py
Created by: Luciano L. Lorenzana
Date: 9/19/2014
Python 3.11

Disc: Holds all the text that is used and displayed in the home page.
"""
import dash

'''
The block of text that you see in the first tab/card
of the home page.
'''
introText = dash.dcc.Markdown(children=[
    """
    # Welcome
    This is a website filled with tools to
    help out students with their assignments.
    From notes to calculators, there is bound
    to be something that can help you with
    learning the basics of biology. 
    """
    ],
    style={"margin-top": 10,
           "margin-bottom": 25}
    )
