"""
Filename: universalAssets.py
Created by: Luciano L. Lorenzana
Date: 9/19/2024
Python 3.11

Disc: A file to quickly call some of the assets that are
      most commonly used in all pages and tabs.
"""

import dash

'''
Headers and Footers
'''
siteHeader = dash.html.Div(children="Your Intro to BIO Course",
                           style={"fontSize": 100,
                                  "margin-top": 5,
                                  "margin-bottom": 15}
                           )

siteFooter = dash.html.Footer(
    children=[dash.html.Center(
        children=
        """
        Created: Luciano L. Lorenzana, 2024
        """)
    ],
    style={"margin-top": 50,
           "margin-bottom": 50}

)

'''
Page Space Margins
'''
topMarginSpace_10px = dash.dcc.Markdown(style={"margin-top": 10})
bottomMarginSpace_25px = dash.dcc.Markdown(style={"margin-bottom": 25})

