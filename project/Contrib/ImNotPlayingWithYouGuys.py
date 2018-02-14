import random
from Game.Const import Const
from Game.Player import Player

class ImNotPlayingWithYouGuys(Player):

    def getSteemUser(self):
        return "@laxam"

    def voteForElimination(self, context):
        return self

    def voteForTie(self, context):
        return self
