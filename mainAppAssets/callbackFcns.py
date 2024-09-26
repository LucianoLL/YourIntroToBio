"""
Filename: callBackFcn.py
Created by: Luciano L. Lorenzana
Date: 9/17/2024
Python 3.11

Disc: Housing any functions that'd be used in the
      'DNA Sequence' page.
"""
import dash

'''
This is the set of functions associated with
the 'DNA Section' page.
'''
def dnaSeqPageFcns(app):
    '''
    This function is used for calculating the number
    of mismatches between two DNA sequences, along
    with the identity percentage.
    '''
    @app.callback(
        dash.Output(component_id="mmc_out01", component_property="value"),
        dash.Output(component_id="mmc_out02", component_property="value"),
        dash.Input(component_id="mmc_in01", component_property="value"),
        dash.Input(component_id="mmc_in02", component_property="value")
    )
    def mismatchfcn(seqOne, seqTwo):

        '''Checks if the first input is empty'''
        if ((seqOne == "") or (seqOne == None)):
            return None, None
        '''Checks if the second input is empty'''
        if ((seqTwo == "") or (seqTwo == None)):
            return None, None

        '''Else, we check the length of both inputs'''
        firstLen = len(seqOne)
        secondLen = len(seqTwo)

        '''
        If both input lengths are equal, then we can perform the analysis,
        Else, we just return a default error message.
        '''
        if firstLen == secondLen:
            errCount = 0
            for tmpInd in range(firstLen):
                if seqOne[tmpInd] != seqTwo[tmpInd]:
                    errCount += 1

            strVal = str(errCount)
            strPercent = str(int(((1 - (errCount / firstLen)) * 100))) + "%"
            return strVal, strPercent

        else:
            return "Unequal Length", "Can't Compute"

'''
This is the set of functions associated with
the 'Acids and Bases' page.
'''
def acidicBasicPageFcns(app):
    @app.callback(
        dash.Output(component_id="hrc_out", component_property="value"),
        dash.Input(component_id="hrc_in01", component_property="value"),
        dash.Input(component_id="hrc_in02", component_property="value")
    )
    def hydrogenRatioFcn(phOne, phTwo):
        if phOne == None or phTwo == None:
            return None

        tmpStr01 = "Equal Amount of H+ Ions"

        if phOne < phTwo:
            tmpStr01 = "DECREASED by "

        elif phOne > phTwo:
            tmpStr01 = "INCREASED by "

        else:
            return tmpStr01

        absVal = str(10 ** (abs(phOne - phTwo)))

        return (tmpStr01 + absVal + " times")
