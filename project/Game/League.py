from random import shuffle 
from math import ceil, floor

from Game.Player import Player
from Game.Table import Table
from Game.Const import Const    
from Game.Context import Context, PlayerContext
from Game.Arena import Arena



class League:

    # tables = []
    # humans = []

    def __init__(self, humans):
        self.humans = humans
        for h in humans:
            h.wealth = Const.STARTING_WEALTH

    def totalPlayersInTables(self):
        toreturn = 0
        for t in self.tables:
            toreturn += len(t.players)
        return toreturn

        
    def playRound (self, phaseIndex, roundIndex):
        print (" -ROUND {}/{} -------".format(roundIndex, Const.ROUNDS_PER_PHASE))
        for t in self.tables:
            #print ("\n -TABLE {}/{}".format(t.name, "X"))
            t.play(phaseIndex, roundIndex)
            t.distribute()




    def makeTables(self, phaseIndex):
        
        totalHumans = len(self.humans)
        nbTables = ceil(totalHumans / Const.MAX_HUMANS_PER_TABLE)
        totalBots = (nbTables*Const.PLAYERS_PER_TABLE) - totalHumans

        shuffle(self.humans)
        self.tables = []

        humansIndex = 0
        minHumansPerTable = floor(totalHumans / nbTables)

        for tabIndex in range(0,nbTables):

            if ((totalHumans-humansIndex)/(nbTables-tabIndex) > minHumansPerTable):
                curHumans = minHumansPerTable+1
            else:
                curHumans = minHumansPerTable

            humansToAdd = self.humans[humansIndex:humansIndex+curHumans]
            nbBotsToAdd = Const.PLAYERS_PER_TABLE - curHumans
            botsToAdd = [Arena.mkBot() for i in range(0, nbBotsToAdd)]
            table = Table(humansToAdd+botsToAdd, "Tab {}".format(tabIndex), tabIndex, totalBots, totalHumans)
            self.tables.append(table)
            humansIndex += curHumans


    def displayResults(self):
        print ("\n\n")
        print ("-----------------------")
        print ("-- LEAGUE RESULTS")
        print ("-----------------------")
        print ("")
        print ("{} registered AIs with {} instances each".format(len(Arena.availablePlayers), Const.INSTANCES_PER_PLAYER))
        print ("{} humans and {} short-lived bots dispatched into {} tables (average of {:2.2f} humans per table)".format(
                len(self.humans), (len(self.tables)*Const.PLAYERS_PER_TABLE) - len(self.humans) ,len(self.tables),  
                len(self.humans)/len(self.tables)))
        print ("Distributed {:.2f} $ to players in {} phases of {} rounds".format(
            sum(p.wealth for p in self.humans), Const.PHASES_PER_GAME, Const.ROUNDS_PER_PHASE))
        print ("")
        print ("-----------------------")
        print ("-- ALL INSTANCES")
        print ("-----------------------")

        self.humans.sort(reverse=True, key=lambda p:p.wealth )
        index = 1
        for p in self.humans:
            print ("{:3} - {:4.2f}   {}".format(index, p.wealth, p.name))
            index += 1

        print ("")
        print ("-----------------------")
        print ("-- WINNING PLAYERS")
        print ("-----------------------")

        ais = {}
        for p in self.humans:
            name = type(p).__name__
            if (name in  ais):
                if (p.wealth > ais[name].wealth):
                    ais[name] = p
            else:
                ais[name] = p

        sorted(ais, key=lambda key:ais[key].wealth)
        index = 1
        for k,v in ais.items():
            print ("{:3} - {:6.2f}   {}".format(index, v.wealth, v.name))
            index += 1


