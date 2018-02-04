

from enum import Enum

from Game.Player import Player



class PlayerContext:

    def __init__(self, player):
        self.id = player.id
        self.previousMoves = []
        self.name = player.name
        self.strength = player.strength


    def describe(self):
        return "[{:50} #{} STR={}]".format(self.name, self.id, self.strength)


class GameContext:
    def __init__(self, phaseIndex, totalBots, totalHumans):
        self.totalBots = totalBots
        self.totalHumans = totalHumans
        self.phaseIndex = phaseIndex



class historyContext(object):

        def __init__(self):
            self.playerActions = {}    






class Context:

    def __init__(self, island, gameContext):
        self.islandIndex = island.islandIndex
        self.game = gameContext
        self.history = []
        self.update(island, None)


    def update(self, island, lastTurnHistory):
        self.activePlayers = {}
        self.betrayers = {}
        self.eliminatedPlayers = {}
        self.currentTies = []
        if (lastTurnHistory != None):
            self.history.append(lastTurnHistory) 

        for p in island.activePlayers.values():
            self.activePlayers[p.id] = PlayerContext(p)
        for p in island.betrayers.values():
            self.betrayers[p.id] = PlayerContext(p)
        for p in island.eliminatedPlayers.values():
            self.eliminatedPlayers[p.id] = PlayerContext(p)    


    def registerTies(self, ties):
        self.currentTies = list(self.activePlayers[pc.id] for pc in ties)


    def describe(self):

        description = "CONTEXT ({}/{}/{})\n  ACTIVE ({})\n    {}\n  ELIMINATED ({})\n    {}\n  BETRAYERS ({})\n    {}".format(
            len(self.activePlayers),
            len(self.eliminatedPlayers),
            len(self.betrayers),
            len(self.activePlayers), 
            "\n    ".join(p.describe() for p in self.activePlayers.values()),
            len(self.eliminatedPlayers), 
            "\n    ".join(p.describe() for p in self.eliminatedPlayers.values()),
            len(self.betrayers), 
            "\n    ".join(p.describe() for p in self.betrayers.values()))

        return description

                
