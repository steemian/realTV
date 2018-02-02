import copy
from random import shuffle
from collections import Counter


from Game.Player import Player
from Game.Context import Context, PlayerContext
from Game.Const import Const


class Island:
    

    def __init__(self, players, name, islandIndex, totalBots, totalHumans):
        shuffle(players)
        print ("Creating island with {}".format(players))
        self.activePlayers = players
        self.eliminatedPlayers = []
        self.betrayers = []
        self.name = name
        self.context = Context(players, islandIndex, totalBots, totalHumans)

    def playUntilLastMan(self, phaseIndex):

        while (len(self.activePlayers) > 0):

            context = None

            print ("\n-- ROUND with {}/{}/{} players".format(
                    len(self.activePlayers),
                    len(self.eliminatedPlayers),
                    len(self.betrayers)
            ))
            

            for p in self.activePlayers:
                p.decide(context)

            self.registerBetrayers(filter(lambda p: p.decision == p, self.activePlayers))

            print ("\nafter betray:  {}/{}/{} players".format(
                    len(self.activePlayers),
                    len(self.eliminatedPlayers),
                    len(self.betrayers)
            ))


            if (self.solveTrial() == False):
                self.gameOver()
            else:
                for p in self.activePlayers:
                    p.score += Const.SCORE_FOR_TRIAL

                self.voteAndEliminate(self.activePlayers)

                if (len(self.activePlayers) == 1):
                    self.victory()
                

    def solveTrial(self):
        difficulty = Const.DIFFICULTY_A * len(self.activePlayers) + Const.DIFFICULTY_B
        commonStrength = sum(p.strength for p in self.activePlayers)

        if (commonStrength > difficulty):
            return True
        else:
            return False

    def eliminate(self, player):
        self.activePlayers.remove(player)
        self.eliminatedPlayers.append(player)

    def registerBetrayers(self, players):
        for p in players: 
            print ("  BETRAY {}".format(p.name))
            self.betrayers.append(p)
            self.activePlayers.remove(p)

    def victory(self):
        self.activePlayers[0].score += Const.SCORE_FOR_LASTMAN

    def gameOver(self):
        for p in self.betrayers:
            p.score += Const.SCORE_FOR_TRAITOR

    def voteAndEliminate(self, players):
        elimination = Counter()

        for p in players:
            print ("{} votes elimiation of {}".format(p.name, p.decision.name))
            elimination[p.decision] += 1

        print (" ELIMINATION :\n  {}".format("\n  ".join(
                "{:40} : {}".format(p.name, elimination[p.name]) for p in elimiation.items())))

        ties = []
        mostVotes = 0
        for player,votes in elimination.items():
            if (len(ties) == 0):
                ties = [player]
                mostVotes = votes
            else:
                if (votes == mostVotes):
                    ties.append(player)
                else: 
                    if (votes > mostVotes):
                        ties = [player]
                        mostVotes = votes

        if (len(ties) == 1):
            self.eliminate(ties[0])
        else:
            self.tieBreak(ties)

    def tieBreak(self, tiedPlayers):

        context = None
        elimination = dict(tiedPlayers, 0)

        for p in players:
            decision = p.voteForTies(context)
            if (decision in tiedPlayers):
                elimination[decision] += 1


        tiedAgain = []
        mostVotes = 0
        for player,votes in elimination.items():
            if (len(tiedAgain) == 0):
                tiedAgain = [player]
                mostVotes = votes
            else:
                if (votes == mostVotes):
                    tiedAgain.append(player)
                else: 
                    if (votes > mostVotes):
                        tiedAgain = [player]
                        mostVotes = votes

        for bye in tiedAgain:
            self.eliminate(bye)
