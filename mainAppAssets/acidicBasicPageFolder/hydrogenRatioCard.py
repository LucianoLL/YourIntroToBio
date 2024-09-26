"""
Filename: hydrogenRatioCard.py
Created by: Luciano L. Lorenzana
Date: 9/19/2024
Python 3.11

Disc: These are all the assets associated with
      the 'Hydrogen Ratio Calculator'
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.universalAssets as uva

'''
The above text of the card
'''
tabText = dash.dcc.Markdown(children=
                            """
                            # Hydrogen Concentration Calculator
                            This is to calculate the (H+) ion ratio between two
                            separate pH levels.
                            """
                            )

phInput01 = dbc.InputGroup(children=[dbc.InputGroupText("Type your INITIAL pH level"),
                                     dbc.Input(
                                         id="hrc_in01",
                                         placeholder="pH Level Here",
                                         type="number",
                                         min=0,
                                         max=14,
                                     )
                                     ],
                           className="mb-4")

phInput02 = dbc.InputGroup(children=[dbc.InputGroupText("Type your RESULTING pH level"),
                                     dbc.Input(
                                         id="hrc_in02",
                                         placeholder="pH Level Here",
                                         type="number",
                                         min=0,
                                         max=14
                                     )
                                     ],
                           className="mb-4")

phOutput = dbc.InputGroup(children=[dbc.InputGroupText("Resulting (H+) Ion Concentration"),
                                    dbc.Input(
                                        id="hrc_out",
                                        disabled=True,
                                        style={"color": "black"}
                                    )
                                    ],
                          className="mb-4")

inputGroups = dbc.Container(children=[phInput01,
                                      phInput02,
                                      phOutput]
                            )

hydrogenRatioCard = dbc.Card(children=[uva.topMarginSpace_10px,
                                       tabText,
                                       inputGroups,
                                       uva.bottomMarginSpace_25px]
                             )
