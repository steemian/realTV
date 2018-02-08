import random, string

from Game.Const import Const
from Game.Player import Player
        

class SensibleExample (Player):
    

    THRESHOLD_MAX = 50
    THRESHOLD_MIN = -30
    THRESHOLD_DROP = 35

    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
        difficulty = Const.DIFFICULTY_A * len(context.activePlayers) + Const.DIFFICULTY_B
        estStr = sum(p.strength for p in context.activePlayers.values() if p.strength > self.THRESHOLD_DROP)

        if (self.strength < self.THRESHOLD_DROP and difficulty > self.strength*len(context.activePlayers)):
            print ("SensibleExample finds itself too week -> suicide ({})".format(self.shortDescribe()))
            return self

        if (estStr > difficulty + self.THRESHOLD_MAX):
            choice = self.Max(context.activePlayers.values())
            print ("SensibleExample kills max -> ({})".format(choice.shortDescribe()))
            return choice

        if (estStr > difficulty + self.THRESHOLD_MIN):
            choice = self.Min(context.activePlayers.values())
            print ("SensibleExample kills min -> ({})".format(choice.shortDescribe()))
            return choice

        print ("SensibleExample fallsback suicide ({})".format(self.shortDescribe()))
        return self

    def voteForTie(self, context):
        return self.Min(context.currentTies.values())


    def Min(self, players):
        targetStr = min(p.strength for p in players)
        return next(p for p in players if p.strength == targetStr)

    def Max(self, players):
        targetStr = max(p.strength for p in players)
        return next(p for p in players if p.strength == targetStr)


class SensibleExample0 (SensibleExample):

    def __init__(self, name, strength):
        super(SensibleExample0, self).__init__(name, strength)
        self.THRESHOLD_MIN = Const.AI_TUNE[0][0]
        self.THRESHOLD_MAX = Const.AI_TUNE[0][1]
        self.THRESHOLD_DROP = Const.AI_TUNE[0][2]

class SensibleExample1 (SensibleExample):

    def __init__(self, name, strength):
        super(SensibleExample1, self).__init__(name, strength)
        self.THRESHOLD_MIN = Const.AI_TUNE[1][0]
        self.THRESHOLD_MAX = Const.AI_TUNE[1][1]
        self.THRESHOLD_DROP = Const.AI_TUNE[1][2]

class SensibleExample2 (SensibleExample):

    def __init__(self, name, strength):
        super(SensibleExample2, self).__init__(name, strength)
        self.THRESHOLD_MIN = Const.AI_TUNE[2][0]
        self.THRESHOLD_MAX = Const.AI_TUNE[2][1]
        self.THRESHOLD_DROP = Const.AI_TUNE[2][2]

class SensibleExample3 (SensibleExample):

    def __init__(self, name, strength):
        super(SensibleExample3, self).__init__(name, strength)
        self.THRESHOLD_MIN = Const.AI_TUNE[3][0]
        self.THRESHOLD_MAX = Const.AI_TUNE[3][1]
        self.THRESHOLD_DROP = Const.AI_TUNE[3][2]

class SensibleExample4 (SensibleExample):

    def __init__(self, name, strength):
        super(SensibleExample4, self).__init__(name, strength)
        self.THRESHOLD_MIN = Const.AI_TUNE[4][0]
        self.THRESHOLD_MAX = Const.AI_TUNE[4][1]
        self.THRESHOLD_DROP = Const.AI_TUNE[4][2]
