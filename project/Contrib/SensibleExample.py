import random, string

from Game.Const import Const
from Game.Player import Player
        

class SensibleExample (Player):
    

    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
    	difficulty = Const.DIFFICULTY_A * len(context.activePlayers) + Const.DIFFICULTY_B
    	estStr = sum(p.strength for p in context.activePlayers.values() if p.strength > 35)

    	if (estStr > difficulty + 100):
    		return self.Max(context.activePlayers.values())

    	if (estStr > difficulty - 30):
    		return self.Min(context.activePlayers.values())

    	return self

    def voteForTie(self, context):
        return self.Min(context.currentTies.values())


    def Min(self, players):
        targetStr = min(p.strength for p in players)
        return next(p for p in players if p.strength == targetStr)

    def Max(self, players):
        targetStr = max(p.strength for p in players)
        return next(p for p in players if p.strength == targetStr)
