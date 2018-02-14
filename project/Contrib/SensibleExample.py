import random, string

from Game.Const import Const
from Game.Player import Player
        

class SensibleExample (Player):
    

    THRESHOLD_MAX = 10              # Targets MAX if overkill > x
    THRESHOLD_MIN = -3              # Targets MIN if overkill still > x
    OFFSET_DROP_PER_PLAYER = 0      # drop if challenge is harder than expected strength + (A.n + B)
    OFFSET_DROP_GLOB = 0            
    THRESHOLD_DROP = 2              # drops when self.strength < x
    THRESHOLD_OTHERS_DROP = 2       # consider others drop at strength < x



    AI_TUNE = [#THRESHOLD_MAX, THRESHOLD_MIN, OFFSET_DROP_PER_PLAYER, OFFSET_DROP_GLOB, THRESHOLD_DROP, THRESHOLD_OTHERS_DROP
                [10,           -3,            0,                      0,                2,              2],
                [15,           -3,            0,                      0,                2,              2],
                [20,           -3,            0,                      0,                2,              2],
                [5,           -3,            0,                      0,                2,              2],
                [0,           -3,            0,                      0,                2,              2],
            ]    

    def getSteemUser(self):
        return ""

        def __init__(self, name, strength):
            self.THRESHOLD_MAX =            self.AI_TUNE[self.SensibleIndex][0]
            self.THRESHOLD_MIN =            self.AI_TUNE[self.SensibleIndex][1]
            self.OFFSET_DROP_PER_PLAYER =   self.AI_TUNE[self.SensibleIndex][2]
            self.OFFSET_DROP_GLOB =         self.AI_TUNE[self.SensibleIndex][3]            
            self.THRESHOLD_DROP =           self.AI_TUNE[self.SensibleIndex][4]
            self.THRESHOLD_OTHERS_DROP =    self.AI_TUNE[self.SensibleIndex][5]
            super(SensibleExample, self).__init__(name, strength)


    def voteForElimination(self, context):

        #print ("{} gets context \n{}".format(self.longDescribe(), context.describe()))


        difficulty = Const.DIFFICULTY_A * len(context.activePlayers) + Const.DIFFICULTY_B
        estStr = sum(p.strength for p in context.activePlayers.values() if p.strength > self.THRESHOLD_OTHERS_DROP)

        if (self.strength <= self.THRESHOLD_DROP):
            #print ("{} BELOW THRESHOLD_DROP -> suicide ({})".format(self.shortDescribe(), self.id))
            return self

        if (difficulty > self.strength*len(context.activePlayers) + self.OFFSET_DROP_GLOB + self.OFFSET_DROP_PER_PLAYER*len(context.activePlayers)):
            #print ("{} finds team too week -> suicide ({})".format(self.shortDescribe(), self.id))
            return self

        if (estStr > difficulty + self.THRESHOLD_MAX):
            choice = self.Max(context.activePlayers.values())
            #print ("{} feels confident -> kill max ({})".format(self.shortDescribe(), choice.shortDescribe()))
#            print ("SensibleExample kills max -> ({})".format(choice.shortDescribe()))
            return choice

        if (estStr > difficulty + self.THRESHOLD_MIN):
            choice = self.Min(context.activePlayers.values())
            #print ("{} want strength -> kill min ({})".format(self.shortDescribe(), choice.shortDescribe()))
#            print ("SensibleExample kills min -> ({})".format(choice.shortDescribe()))
            return choice

#        print ("SensibleExample feels too weak  ({})".format(self.shortDescribe()))
        #print ("{} feels weak -> self ({})".format(self.shortDescribe(), self.id))
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
    SensibleIndex = 0

class SensibleExample1 (SensibleExample):
    SensibleIndex = 1

class SensibleExample2 (SensibleExample):
    SensibleIndex = 2

class SensibleExample3 (SensibleExample):
    SensibleIndex = 3

class SensibleExample4 (SensibleExample):
    SensibleIndex = 4
