import random

from Game.Player import Player


class RandomPlayer(Player):


    def getSteemUser(self):
        return "@gbd"


    def voteForElimination(self, context):
    	return random.choice(list(context.activePlayers.values()))

    def voteForTie(self, context):
        return None

