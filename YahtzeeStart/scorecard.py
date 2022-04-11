"""
    This module contains all of the functions related to working with the scorecard
"""

import constants
from playing import clear

# TODO: write resetScorecard and updateScorecard
def resetScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    sets each of the individual values for the user and the computer to the constant empty.
    The subtotal, bonus and total should be set to 0.
    It does not return a value but the scorecard is altered by the function
    """
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]
    for i in range(len(uScorecard)):
        uScorecard[i] = constants.EMPTY
    for i in range(len(cScorecard)):
        cScorecard[i] = constants.EMPTY
    uScorecard[constants.SUBTOTAL] = 0
    cScorecard[constants.SUBTOTAL] = 0
    uScorecard[constants.TOTAL] = 0
    cScorecard[constants.TOTAL] = 0    


def updateScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    calculates the subtotal, bonus and total for both the user and the computer.
    It does not return a value but the scorecard is altered by the function
    """
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]
    ###RESET TOTALS####
    cScorecard[constants.SUBTOTAL] = 0
    uScorecard[constants.SUBTOTAL] = 0
    cScorecard[constants.TOTAL] = 0
    uScorecard[constants.TOTAL] = 0
    ####UPDATE SUBTOTALS####
    for i in range(constants.ONES, constants.SIXES + 1):
        if cScorecard[i] > 0:
            cScorecard[constants.SUBTOTAL] = cScorecard[constants.SUBTOTAL] + cScorecard[i]
        if uScorecard[i] > 0:
            uScorecard[constants.SUBTOTAL] = uScorecard[constants.SUBTOTAL] + uScorecard[i]
    ####CALCULATE BONUS####
    if uScorecard[constants.SUBTOTAL] >= 63:
        uScorecard[constants.BONUS] = 35
    else:
        uScorecard[constants.BONUS] = 0
    if cScorecard[constants.SUBTOTAL] >= 63:
        cScorecard[constants.BONUS] = 35
    else:
        cScorecard[constants.BONUS] = 0
    ####UPDATE TOTAL####
    cScorecard[constants.TOTAL] = 0
    uScorecard[constants.TOTAL] = 0
    for i in range(constants.THREE_OF_A_KIND, constants.BONUS + 1):
        if cScorecard[i] > 0:
            cScorecard[constants.TOTAL] = cScorecard[constants.TOTAL] + cScorecard[i]
        if uScorecard[i] > 0:
            uScorecard[constants.TOTAL] = uScorecard[constants.TOTAL] + uScorecard[i]

def formatCell(value):
    return "" if value < 0 else str(value)


def displayScorecards(scorecard):
    labels = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
              "3 of a Kind", "4 of a Kind", "Full House", "Small Straight", "Large Straight",
              "Chance", "Yahtzee", "Sub Total", "Bonus", "Total Score"]
    lineFormat = "| {3:2s} {0:<15s}|{1:>8s}|{2:>8s}|"
    border = '-' * 39
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]

    #clear()
    print(border)
    print(lineFormat.format("", "  You   ", "Computer", ""))
    print(border)

    for i in range(constants.ONES, constants.SIXES + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.SUBTOTAL], formatCell(uScorecard[constants.SUBTOTAL]), formatCell(cScorecard[constants.SUBTOTAL]), ""))
    print(border)
    print(lineFormat.format(labels[constants.BONUS], formatCell(uScorecard[constants.BONUS]), formatCell(cScorecard[constants.BONUS]), ""))
    print(border)

    for i in range(constants.THREE_OF_A_KIND, constants.YAHTZEE + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.TOTAL], formatCell(uScorecard[constants.TOTAL]), formatCell(cScorecard[constants.TOTAL]), ""))
    print(border)



def completedScorecards(scorecard):
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]
    for i in range(len(uScorecard)):
        if uScorecard[i] < 0:
            uScorecardComplete = False
            break
        else:
            uScorecardComplete = True
    for i in range(len(cScorecard)):
        if cScorecard[i] < 0:
            cScorecardComplete = False
            break
        else:
            cScorecardComplete = True
    if uScorecardComplete == False or cScorecardComplete == False:
        return False
    else:
        return True
