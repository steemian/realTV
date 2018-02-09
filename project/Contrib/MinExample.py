import random, string

from Game.Const import Const
from Game.Player import Player
        

class MinExample (Player):
    

    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
    	elim = min(context.activePlayers.values(), key=lambda p: p.strength)
    	print ("{} votes {} among \n{}".format(self.shortDescribe(), elim.longDescribe(), context.describe()))
    	return elim

    def voteForTie(self, context):
        return min(context.currentTies.values(), key=lambda p: p.strength)

    

