import random, string

from Game.Const import Const


class Player:
    
    def __init__(self, name, strength):
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Const.RANDOM_ID_LEN))
        self.score = Const.STARTING_SCORE
        self.name = "[{:10} {:2} ({:15})]".format(name, self.id, type(self).__name__)
        self.strength = strength


    def describe(self):
        return "[{} S={:3}]".format(self.name, self.score)

    def getSteemUser(self):             # override this to return your steem name
        raise NotImplementedError("Player is abstract")

    def voteForElimination(self, context):           # override this
        raise NotImplementedError("Player is abstract")

    def voteForTie(self, context):           # override this
        raise NotImplementedError("Player is abstract")

    def decide(self, context):
        self.decision = self.voteForElimination(context)

        #print ("{:20} decides against {}".format(self.name, self.decision.name))

        # Invalid decisions count as giving up/betraying
        #TODO: reintroducsthis once context is implemented
        #if (self.decision not in context.activePlayers):
        #    self.decision = self

        return self.decision

    
