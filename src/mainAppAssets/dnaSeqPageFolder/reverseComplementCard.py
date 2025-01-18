"""
Filename: reverseComplementCard.py
Created by: Luciano L. Lorenzana
Date: 11/19/2024
Python 3.12

Disc: All the assets and cards for the
      'Reverse Complement Calculator'
"""
import dash
import dash_bootstrap_components as dbc
import mainAppAssets.universalAssets as uva

'''
The above text of the card.
'''
tabText = dash.dcc.Markdown(children="""
                        # Reverse Complement of a DNA Sequence
                        Produces the complement of any given DNA Sequence
                        and display it in reverse.
                        """)

'''
User DNA sequence input.
'''
dnaInput = dbc.InputGroup(children=[dbc.InputGroupText("Type Your DNA Sequence"),
                                    dbc.Input(
                                        id="rcc_in",
                                        placeholder="DNA Sequence Here",
                                        type="text"
                                    )
                                    ],
                          className="mb-4")


'''
The output box for the reverse complement for
a DNA sequence.
'''
reverseComp = dbc.InputGroup(children=[dbc.InputGroupText("Reverse Complement"),
                                       dbc.Input(
                                           id="rcc_out",
                                           disabled=True,
                                           style={"color": "black"}
                                       )
                                       ],
                             className="mb-4")

'''
Organizing inputs into a container.
'''
inputGroups = dbc.Container(children=[dnaInput,
                                      reverseComp])

'''
Creating the card for the calculator.
'''
reverseCompCard = dbc.Card(children=[uva.topMarginSpace_10px,
                                     tabText,
                                     inputGroups,
                                     uva.bottomMarginSpace_25px]
                           )

