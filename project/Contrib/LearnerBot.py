import random
from Game.Const import Const
from Game.Player import Player
        
class LearnerBot(Player):     # Always votes randomly
    
    def getSteemUser(self):
        return "@gbd"

    def voteForElimination(self, context):
        
        raise NotImplementedError("Abstract")


    def voteForTie(self, context):
        raise NotImplementedError("Abstract")

