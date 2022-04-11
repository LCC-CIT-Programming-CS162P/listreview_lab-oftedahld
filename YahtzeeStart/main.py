from time import sleep
import os
import random

import constants
import scoring
import scorecard
import playing

# TODO: write main AFTER you have written and tested each function
def main():
    scoreCardList = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    userTurn = False
    boardcomplete = False
    scorecard.resetScorecard(scoreCardList)
    while boardcomplete == False:
        userTurn = not userTurn
        scorecard.updateScorecard(scoreCardList)
        scorecard.displayScorecards(scoreCardList)
        if userTurn == True:
            print("User's turn.....")
            sleep(5)
            playing.userPlay(scoreCardList[constants.USER])
        else:
            print("Computer's turn.....")
            sleep(5)
            playing.computerPlay(scoreCardList[constants.COMPUTER])
        boardcomplete = scorecard.completedScorecards(scoreCardList)
    scorecard.updateScorecard(scoreCardList)
    scorecard.displayScorecards(scoreCardList)
    if scoreCardList[constants.USER][constants.TOTAL] > scoreCardList[constants.COMPUTER][constants.TOTAL]:
        print("User wins... Take that Skynet!!!!")
    else:
        print("Computer wins... The singularity is imminent")
    
    
    
    """
    while there are still empty items in either scorecard
        swap players
        call updateScorecard
        call displayScorecard
        if it's the user's turn
            print a message and pause briefly
            call userPlay
        else
            print a message and pause breifly
            call computerPlay
        end if
     end while
     call updateScorecard
     call displayScorecard
     determine who won and display a message

    """


# this block is the same all of the time
# when the name of the file is main, call main
if __name__ == '__main__':
    main()
