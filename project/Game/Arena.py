from random import shuffle 
from math import ceil, floor
from collections import Counter


from Contrib import *
from Game.BotPareto import *
import Game.League, Game.Const
from Game.Context import Context, GameContext 
from Game.Island import Island


class Arena:
    
    availablePlayers =  [
        RandomPlayer,
        SimpleExample,
    ]

    availableBots = [
        BotPareto,
    ]



    def __init__(self):
        self.humans = []
        self.islands = []
        for str in Const.INSTANCES_STRENGTH:
            for p in self.availablePlayers:
                self.humans.append(p("STR={}".format(str), str))


    def makeIslands(self, phaseIndex):
        
        totalHumans = len(self.humans)
        nbIslands = ceil(totalHumans / Const.MAX_HUMANS_PER_ISLAND)
        totalBots = (nbIslands*Const.PLAYERS_PER_ISLAND) - totalHumans

        print("Making islands.. Humans={} nbIslands={} totalBots={}".format(totalHumans, nbIslands, totalBots))

        shuffle(self.humans)
        self.islands = []

        humansIndex = 0
        minHumansPerIsland = floor(totalHumans / nbIslands)

        for islIndex in range(0,nbIslands):

            if ((totalHumans-humansIndex)/(nbIslands-islIndex) > minHumansPerIsland):
                curHumans = minHumansPerIsland+1
            else:
                curHumans = minHumansPerIsland

            humansToAdd = self.humans[humansIndex:humansIndex+curHumans]
            nbBotsToAdd = Const.PLAYERS_PER_ISLAND - curHumans
            botsToAdd = [Game.Arena.mkBot() for i in range(0, nbBotsToAdd)]

            gameContext = GameContext(phaseIndex, nbBotsToAdd, totalHumans)
            isl = Island(humansToAdd+botsToAdd, "Isl {}".format(islIndex), islIndex, gameContext)
            self.islands.append(isl)
            humansIndex += curHumans



    def runArena(self):
        for phaseIndex in range(0, Const.PHASES_PER_GAME):
            self.runPhase(phaseIndex)
        #self.displayResults()



    def runPhase(self, phaseIndex):
        print ("\n\n\n--PHASE {}".format(phaseIndex))
        self.makeIslands(phaseIndex)
        for isl in self.islands:
            isl.playUntilLastMan()

        self.displayResults()
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")


    def mkBot():
        str = random.choice(Const.INSTANCES_STRENGTH)
        return random.choice(Arena.availableBots)("BOT {}".format(str),str)


    def displayResults(self):
        print ("\n\n")
        print ("-----------------------")
        print ("-- ARENA RESULTS")
        print ("-----------------------")
        print ("")
        print ("{} registered AIs with {} instances each".format(len(Arena.availablePlayers), Const.INSTANCES_PER_PLAYER))
        print ("{} humans and {} short-lived bots dispatched into {} tables (average of {:2.2f} humans per table)".format(
                len(self.humans), (len(self.islands)*Const.PLAYERS_PER_ISLAND) - len(self.humans) ,len(self.islands),  
                len(self.humans)/len(self.islands)))
        print ("")
        print ("-----------------------")
        print ("-- ALL INSTANCES")
        print ("-----------------------")

        self.humans.sort(reverse=True, key=lambda p:p.score )
        index = 1
        for p in self.humans:
            print ("{:3} - {:3}   {}".format(index, p.score, p.name))
            index += 1

        print ("")
        print ("-----------------------")
        print ("-- WINNING PLAYERS")
        print ("-----------------------")

        scores = Counter()
        for p in self.humans:
            scores[type(p).__name__] += p.score


        sortedScores = sorted(scores, key=lambda k : scores[k], reverse=True   )
        index = 1

        for k in sortedScores:  
            print ("{:3} - {:3}   {}".format(index, scores[k], k))
            index += 1
