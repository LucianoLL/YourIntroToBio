"""
Filename: app.py
Created by: Luciano L. Lorenzana
Date: 9/6/2024
Python 3.11

Disc: A Dash app that calls all necessary assets to run
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.universalAssets as uva
import mainAppAssets.callbackFcns as cbf

'''
Setting up the Dash app, using:
    - the SOLAR stylesheet/theme for the GUI
    - Using pages/links 
'''
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SOLAR,
                                      dbc.icons.FONT_AWESOME],
                use_pages=True)


'''
Fetching the links for the pages in this project
'''
siteLinks = dash.html.Div([
    dash.html.Div(
        dash.dcc.Link(children=page["title"],
                      href=page["relative_path"]),
        style={"margin-right": 10}  # This is meant to space out the page links
    ) for page in dash.page_registry.values()],
    style={"display": "flex"}  # To display the links in a row than a column
)

'''
These are essentially the assets that'll be displayed
in all the pages of this project
'''
app.layout = dbc.Container(children=[
    uva.siteHeader,  # The header that'll be displayed at the top of the app
    siteLinks,  # The row of links to several pages in this project
    uva.bottomMarginSpace_25px,
    dash.page_container  # Always at the bottom of our container...
                         # ...includes the pages of our app in our GUI
])

'''
Since there are plenty of pages, files, and functions
it's easier if we just call those function from another file
'''
cbf.dnaSeqPageFcns(app=app)
cbf.acidicBasicPageFcns(app=app)




if __name__ == '__main__':
    app.run(debug=True, port=8051, jupyter_mode="external")

