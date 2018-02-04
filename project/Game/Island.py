
import copy
from random import shuffle
from collections import Counter


from Game.Player import Player
from Game.Context import Context, PlayerContext
from Game.Const import Const


class Island:
    

    def __init__(self, players, name, islandIndex, gameContext):
        shuffle(players)
        #print ("Creating island with {}".format(players))
        self.allPlayers = {}
        self.eliminatedPlayers = {}
        self.betrayers = {}
        for p in players:
            self.allPlayers[p.id] = p
        self.activePlayers = self.allPlayers.copy()
        self.islandIndex = islandIndex
        self.name = name
        self.context = Context(self, gameContext)


    def playUntilLastMan(self):

        while (len(self.activePlayers) > 0):

            print(self.roundHeader())

            for p in self.activePlayers.values():
                p.decide(self.context)

            self.registerBetrayers(list(filter(lambda p: p.decision.id == p.id , self.activePlayers.values())))

            if (len(self.activePlayers) == 0):
                return self.noWinner()
                
            if (self.solveTrial() == False):
                return self.gameOver()

            self.voteAndEliminate(self.activePlayers.values())

            if (len(self.activePlayers) == 1):
                self.victory()

        return
                

    def solveTrial(self):
        difficulty = Const.DIFFICULTY_A * len(self.activePlayers) + Const.DIFFICULTY_B
        commonStrength = sum(p.strength for p in self.activePlayers.values())

        if (commonStrength > difficulty):
            for p in self.activePlayers.values():
                p.score += Const.SCORE_FOR_TRIAL
            return True

        else:
            return False


    def eliminate(self, playerId):

        p = self.allPlayers[playerId]
        print ("   ELIMINATE {}".format(p.name))

        if p in self.activePlayers.values():
            del self.activePlayers[p.id]
            self.eliminatedPlayers[p.id] = p


    def registerBetrayers(self, players):
        for p in players: 
            print ("  {} **betrays**".format(p.name))
            self.betrayers[p.id] = p
            del self.activePlayers[p.id]
        

    def victory(self):
        key, victor = self.activePlayers.popitem()
        victor.score += Const.SCORE_FOR_LASTMAN

    def gameOver(self):
        for p in self.betrayers.values():
            p.score += Const.SCORE_FOR_TRAITOR

    def noWinner(self):
        pass

    def voteAndEliminate(self, players):
        elimination = Counter()

        for p in players:
            print ("  {} votes elimination of {}".format(p.name, p.decision.name))
            elimination[p.decision] += 1

        print ("   ELIMINATION SCOREBOARD :\n     {}".format("\n     ".join(
                "{:40} : {}".format(p.name, score) for p,score in elimination.items())))

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
            #print("   * leader= {:2} {}".format(
            #    mostVotes, 
            #    "\n                ".join(p.name for p in ties)))



        if (len(ties) == 1):
            self.eliminate(ties[0].id)
        else:
            self.tieBreak(ties)

    def tieBreak(self, tiedPlayers):

        print ("-- TIE BREAK {}".format(
            "\n             ".join(p.name for p in tiedPlayers)))

        self.context.registerTies(tiedPlayers)

        elimination = Counter()

        for p in self.activePlayers.values():
            decision = p.voteForTie(self.context)
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
            self.eliminate(bye.id)


    def scoreBoard(self):
        displayBoard = "\n\n-------SCORE BOARD for Island #{}\n".format(self.islandIndex)
        orderedPlayers = sorted(self.allPlayers.values(), key=lambda p: p.score, reverse=True)
        
        displayBoard += "\n".join(p.describe() for p in orderedPlayers)

        return displayBoard



    def roundHeader(self):
        return "\n\n-- ROUND with {}/{}/{} (total {}) players".format(
                    len(self.activePlayers),
                    len(self.eliminatedPlayers),
                    len(self.betrayers),
                    len(self.allPlayers)
            )
