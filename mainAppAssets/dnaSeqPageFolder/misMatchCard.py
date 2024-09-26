"""
Filename: misMatchCard.py
Created by: Luciano L. Lorenzana
Date: 9/17/2024

Disc: All the assets and cards for the
      'Mismatch Calculator'
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.universalAssets as uva

'''
The above text of the card.
'''
tabText = dash.dcc.Markdown(children="""
                       # Mismatched DNA Groups
                       This is meant to analyze both DNA sequences 
                       and count the number of group mismatches.
                       """)

'''
The first DNA sequence input.
'''
dnaInput01 = dbc.InputGroup(children=[dbc.InputGroupText("Type your FIRST DNA Sequence"),
                                      dbc.Input(
                                          id="mmc_in01",
                                          placeholder="DNA Sequence Here",
                                          type="text"
                                      )
                                      ],
                            className="mb-3")

'''
The second DNA Sequence Input.
'''
dnaInput02 = dbc.InputGroup(children=[dbc.InputGroupText("Type your SECOND DNA Sequence"),
                                      dbc.Input(
                                          id="mmc_in02",
                                          placeholder="DNA Sequence Here",
                                          type="text"
                                      )
                                      ],
                            className="mb-3")

'''
The output box for the number of mismatches.
'''
mismatchVal = dbc.InputGroup(children=[dbc.InputGroupText("Number of Mismatches"),
                                       dbc.Input(id="mmc_out01",
                                                 disabled=True,
                                                 style={"color": "black"}
                                                 )
                                       ],
                             className="mb-3")

'''
The output box for the identity percentage, 
how closely related two DNA sequences are.
'''
identPercent = dbc.InputGroup(children=[dbc.InputGroupText("Identity Percentage"),
                                        dbc.Input(
                                            id="mmc_out02",
                                            disabled=True,
                                            style={"color": "black"}
                                        )
                                        ],
                              className="mb-3")

'''
Organizing the inputs into a container.
'''
inputGroups = dbc.Container(children=[dnaInput01,
                                      dnaInput02,
                                      mismatchVal,
                                      identPercent])

'''
Creating the card for the 'Mismatch Calculator' card.
'''
misMatchCard = dbc.Card(children=[uva.topMarginSpace_10px,
                                  tabText,
                                  inputGroups,
                                  uva.bottomMarginSpace_25px],
                        )

