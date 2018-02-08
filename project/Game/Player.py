import random, string

from Game.Const import Const


class Player:
    
    def __init__(self, name, strength):
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Const.RANDOM_ID_LEN))
        #self.name = "[{:10} {:2} ({:15})]".format(name, self.id, type(self).__name__)
        self._name = name
        self.score = Const.STARTING_SCORE
        self.strength = strength


    def longDescribe(self):
        return "[{:10} {} ({:15}) S={}  [{:5.0f} pts]]".format(self._name, self.id, type(self).__name__, self.strength, self.score)

    def shortDescribe(self):
        return "{:<3}-{:2}_{:<3}".format(self.id, self.strength, type(self).__name__)


    def getSteemUser(self):             # override this to return your steem name
        raise NotImplementedError("Player is abstract")

    def voteForElimination(self, context):           # override this
        raise NotImplementedError("Player is abstract")

    def voteForTie(self, context):           # override this
        raise NotImplementedError("Player is abstract")

    def decide(self, context):
        self.decision = self.voteForElimination(context)

        if (self.decision.id not in pc.id for pc in context.activePlayers):
            print ("decision {} -> {}".format(self.decision, self))
            self.decision = self

        return self.decision

    
