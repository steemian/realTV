import random, string

from Game.Const import Const
from Game.Player import Player
        

class MinExample (Player):
    

    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
    	return min(context.activePlayers.values(), key=lambda p: p.strength)

    def voteForTie(self, context):
        return min(context.currentTies.values(), key=lambda p: p.strength)

    

