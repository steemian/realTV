import random, string

from Game.Const import Const
from Game.Player import Player
        

class MaxExample (Player):
    

    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
        return self.MinOrMax(context.activePlayers.values())

    def voteForTie(self, context):
        return self.MinOrMax(context.currentTies.values())

    def MinOrMax(self, players):
        targetStr = max(p.strength for p in players)
        return next(p for p in players if p.strength == targetStr)
    

