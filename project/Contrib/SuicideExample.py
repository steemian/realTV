from Game.Player import Player


class SuicideExample(Player):


    def getSteemUser(self):
        return "@gbd"


    def voteForElimination(self, context):
        return self

    def voteForTie(self, context):
        return None

