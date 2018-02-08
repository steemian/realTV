import random

from Game.Player import Player


class RandomExample(Player):


    def getSteemUser(self):
        return "@gbd"


    def voteForElimination(self, context):
        return random.choice(list(context.activePlayers.values()))

    def voteForTie(self, context):
        if (len(context.currentTies) == 0):
            return None

        return random.choice(list(context.currentTies.values()))

