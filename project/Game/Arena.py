from Contrib import *

from Game.Bot import *


import Game.League, Game.Const
import Game.Bet
import Game.Context 


class Arena:
    
    availablePlayers =  [
        ExShortSighted,
        ExampleRisker,
        ExConservative,
        ExGiver,
        ExSocial,
    ]

    availableBots = [
        BotPareto,
    ]



    def __init__(self):
        self.players  = []
        for i in range(0, Game.Const.INSTANCES_PER_PLAYER):
            for p in self.availablePlayers:
                self.players.append(p(""))


    def runArena(self):
        self.league = Game.League(self.players)
        for phaseIndex in range(0, Game.Const.PHASES_PER_GAME):
            self.runPhase(phaseIndex)
        self.league.displayResults()



    def runPhase(self, phaseIndex):
        print ("\n\n\n--PHASE {}".format(phaseIndex))
        self.league.makeTables(phaseIndex)
        for roundIndex in range(0, Game.Const.ROUNDS_PER_PHASE):
            self.runRound(phaseIndex, roundIndex)

        self.league.displayResults()
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")


    def runRound(self, phaseIndex, roundIndex):
        self.league.playRound(phaseIndex, roundIndex)           


    def mkBot():
        return random.choice(Arena.availableBots)("")


