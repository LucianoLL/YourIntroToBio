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
import assets.mainAppAssetStyles as mas


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
Changing the default favicon to a custom one
'''
app._favicon = "images/logo.ico"

'''
Logo for the Dash app
'''
img01 = dash.html.Img(src="assets/images/logo.png",
                      style=mas.headerImg,
                      )
'''
Fetching the links for the pages in this project
'''
siteLinks = dash.html.Div([
    dash.html.Div(
        dbc.Button(
            children=page["title"],
            id="button" + str(ind),
            href=page["relative_path"],
            style=mas.mainTabButtons  # This is meant to space out the page links
        )
    ) for ind, page in enumerate(dash.page_registry.values())
    ],
    style=mas.rowStyle  # To display the links in a row than a column
)

'''
These are essentially the assets that'll be displayed
in all the pages of this project
'''
app.layout = dbc.Container(children=[
    img01,  # Replaced the text header with an image
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
    app.run(debug=True, jupyter_mode="external")
