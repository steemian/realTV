import random
from Game.Const import Const
from Game.Player import Player
        
class Clueless(Player):     # Always votes randomly
    
    def getSteemUser(self):
        return "@laxam"

    def voteForElimination(self, context):
        return random.choice(context.activePlayers.values())

    def voteForTie(self, context):
        return random.choice(context.currentTies.values())