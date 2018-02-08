import random, string

from Game.Const import Const
from Game.Player import Player
        

class BotPareto (Player):
    
    def __init__(self, name, strength):
        super(BotPareto, self).__init__(name, strength)
        self.id = "-" + self.id[1:]



    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
        return self.MinOrMax(context.activePlayers.values())

    def voteForTie(self, context):
        return self.MinOrMax(context.currentTies.values())

    def MinOrMax(self, players):
        if (random.random() > 0.2):
            targetStr = min(p.strength for p in players)
        else:
            targetStr = max(p.strength for p in players)

        return next(p for p in players if p.strength == targetStr)
    

