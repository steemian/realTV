import random, string

from Game.Const import Const


class Player:
    
    def __init__(self, name, strength):
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Const.RANDOM_ID_LEN))
        #self.name = "[{:10} {:2} ({:15})]".format(name, self.id, type(self).__name__)
        self.name = type(self).__name__
        self.score = Const.STARTING_SCORE
        self.strength = strength
        self.decision = None
        self.tieDecision = None


    def longDescribe(self):
        return "[{:10} {} ({:15}) S={}  [{:5.0f} pts]]".format(self.name, self.id, type(self).__name__, self.strength, self.score)

    def shortDescribe(self):
        return "{:<3}-{:2}_{:<3}".format(self.id, self.strength, type(self).__name__)


    def getSteemUser(self):             # override this to return your steem name
        raise NotImplementedError("Player is abstract")

    def voteForElimination(self, context):           # override this
        raise NotImplementedError("Player is abstract")

    def voteForTie(self, context):           # override this
        raise NotImplementedError("Player is abstract")



    def decisionCheck(self, allowedValues, decisionAsPlayerDescriptor, defaultValue):

        try:
            #print (allowedValues)   
            #print ("\n\n\n")
            #print ("Checking {} desc = {}".format(self.shortDescribe(), decisionAsPlayerDescriptor))

            if (decisionAsPlayerDescriptor == None):
                print ("Checking {} decided -None- -> {}".format(self.shortDescribe(), defaultValue)) 
                return defaultValue

            if (decisionAsPlayerDescriptor.id in allowedValues.keys()):
                playerTOBeVoted = allowedValues[decisionAsPlayerDescriptor.id]
                return playerTOBeVoted
            else:
                print ("Checking {} decided invalid {} -> {}".format(self.shortDescribe(), decisionAsPlayerDescriptor.shortDescribe(), defaultValue)) 
                playerTOBeVoted = defaultValue
                return playerTOBeVoted

            

        except Exception as ex:
            print ("Exception from {} lookup in {}. Falling back to {}\n{}".format(
                self.shortDescribe(),
                ' '.join(pc.shortDescribe() for pc in allowedValues.values()),
                defaultValue,
                ex
                ))
            return defaultValue

        print ("Fallback while {} lookup in {}. Falling back to {}".format(
                self.shortDescribe(),
                ' '.join(pc.shortDescribe() for pc in allowedValues.values()),
                defaultValue
                ))
        return defaultValue



    def decideVote(self, context):
#        print ("CONTEXT {}".format(context.describe()))
        originalDecision = self.voteForElimination(context)
#        if (originalDecision in (None, self)):
#            print("{} tries to vote {}".format(self.shortDescribe(), originalDecision))
        self.decision = self.decisionCheck(context.activePlayers, originalDecision, self)
#        print ("{} votes  {} corrected is {}".format(self.shortDescribe(), originalDecision.shortDescribe(), self.decision.shortDescribe()))
        return self.decision


    def decideTie(self, context):
        originalDecision = self.voteForTie(context)
        self.tiedDecision = self.decisionCheck(context.currentTies, originalDecision, None)
#        print ("{} breaks {} corrected is {}".format(self.shortDescribe(), originalDecision.shortDescribe(), self.decision.shortDescribe()))
        return self.tiedDecision
