import random
from Game.Const import Const
from Game.Player import Player
        
class Clueless(Player):     # Always votes randomly
    
    def getSteemUser(self):
        return "@laxam"

    def voteForElimination(self, context):
        print (context.activePlayers.values())
        return random.choice(list(context.activePlayers.values()))


    def voteForTie(self, context):

        return random.choice(list(context.currentTies.values()))
