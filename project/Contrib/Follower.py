import random, string

from Game.Const import Const
from Game.Player import Player
        


class FollowerStats():
    def __init__(self):
        self.teamSizeRepartition = {i:0 for i in range(1,11)}


class Follower (Player):

    '''
        Cooperates to any friendly strong champion.
        Else leaves as soon as it gets risky
    '''
    FOREMAN_THRESHOLD = Const.DIFFICULTY_A + Const.DIFFICULTY_B

    stats = FollowerStats()


    def __init__(self, name, strength):
        super(Follower, self).__init__(name, strength)




    def getSteemUser(self):
        return ""


    def updateTurnStats(self, context):

        self.difficulty = Const.DIFFICULTY_A * len(context.activePlayers) + Const.DIFFICULTY_B
        self.teamStr = sum(p.strength for p in context.activePlayers.values())

        self.followers = []
        self.opponents = []
        self.foreman = None
        self.foremanStrength = -1

        for pl in context.activePlayers.values():
            #print ("PLAYER {}".format(pl.longDescribe()))
            if (pl.name == self.name):
                if (pl.strength > self.foremanStrength):
                    self.foreman = pl 
                self.followers.append(pl)
            else:
                self.opponents.append(pl)

        Follower.stats.teamSizeRepartition[len(self.followers)] += 1
        #print (Follower.stats.teamSizeRepartition)

        #if (len(self.followers) > 1):
            #print ("Follower in a group of {}".format(len(self.followers)))




    def voteForElimination(self, context):

        self.updateTurnStats(context)

        if (self.foreman.strength >= self.FOREMAN_THRESHOLD):
            if (self.strength < min(Const.DIFFICULTY_A, self.foreman.strength)):
                return self
            else:
                return self.weakOpponentOrWeakAlly(context.activePlayers.values())

        if (self.teamStr < self.difficulty):
            return self

        return self.weakOpponentOrWeakAlly(context.activePlayers.values())



    def voteForTie(self, context):
        if (self.foreman.strength >= self.FOREMAN_THRESHOLD):
            return self.weakOpponentOrWeakAlly(context.currentTies.values())

        if (self.teamStr >= self.difficulty):
            return self.weakOpponentOrWeakAlly(context.currentTies.values())

        return self.weakOpponentOrWeakAlly(context.currentTies.values())


    def strongOpponentOrWeakAlly(self, players):
            tiedOpponents = (set(self.opponents) and set (players))

            if (len(tiedOpponents) > 0):
                return max(tiedOpponents, key=lambda p: p.strength)
            else:
                return min(players, key=lambda p: p.strength)

    def weakOpponentOrWeakAlly(self, players):
            tiedOpponents = (set(self.opponents) and set (players))

            if (len(tiedOpponents) > 0):
                return min(tiedOpponents, key=lambda p: p.strength)
            else:
                return min(players, key=lambda p: p.strength)
