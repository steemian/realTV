
import copy
from random import shuffle
from collections import Counter


from Game.Player import Player
from Game.Context import Context, PlayerContext
from Game.Const import Const
from Game.IslandStats import IslandStats


class Island:
    

    def __init__(self, players, name, islandIndex, gameContext):
        shuffle(players)
        #print ("Creating island with CTX={}\n              PL={}".format(gameContext, players))
        self.allPlayers = {}
        self.eliminatedPlayers = {}
        self.betrayers = {}
        for p in players:
            self.allPlayers[p.id] = p
        self.activePlayers = self.allPlayers.copy()
        self.islandIndex = islandIndex
        self.name = name
        self.context = Context(self, gameContext)
        self.stats = IslandStats()


    def playUntilLastMan(self):

        while (len(self.activePlayers) > 0):

            #print(self.roundHeader())

            playersAtStartOfRound = len(self.activePlayers)

            for p in self.activePlayers.values():
                p.decide(self.context)

            self.registerBetrayers(list(filter(lambda p: p.decision.id == p.id , self.activePlayers.values())))

            if (len(self.activePlayers) == 0):
                return self.noWinner()

            if (len(self.activePlayers) == 1):
                self.victory()
                return
                
            if (self.solveTrial(len(self.activePlayers)) == False):
                return self.gameOver()

            self.voteAndEliminate(self.activePlayers.values())

            if (len(self.activePlayers) == 1):
                self.victory()
                return

            lastTurn = None
            self.context.update(self, lastTurn)

        return
                

    def solveTrial(self, nbPlayers):
        difficulty = Const.DIFFICULTY_A * nbPlayers + Const.DIFFICULTY_B
        commonStrength = sum(p.strength for p in self.activePlayers.values())

        if (commonStrength > difficulty):
            for p in self.activePlayers.values():
                p.score += Const.SCORE_FOR_TRIAL
                self.stats.PointsForTrial += Const.SCORE_FOR_TRIAL
            return True

        else:
            return False


    def eliminate(self, playerId):

        p = self.allPlayers[playerId]
        #print ("   ELIMINATE {}".format(p.name))

        if p in self.activePlayers.values():
            del self.activePlayers[p.id]
            self.eliminatedPlayers[p.id] = p


    def registerBetrayers(self, players):
        for p in players: 
            #print ("  {} **betrays**".format(p.name))
            self.betrayers[p.id] = p
            del self.activePlayers[p.id]

        

    def victory(self):
        victor = next(iter(self.activePlayers.values()))
        victor.score += Const.SCORE_FOR_LASTMAN
        self.stats.PointsForVic += Const.SCORE_FOR_LASTMAN
        self.stats.VICTORIES += 1
#        print ("  Isl {}.{} : VICTORY for {}".format(
#            self.context.game.phaseIndex,
#            self.islandIndex,
#            victor.name))

    def gameOver(self):
        for p in self.betrayers.values():
            p.score += Const.SCORE_FOR_EACH_TRAITOR
            p.score += Const.SCORE_FOR_ALL_TRAITORS / len(self.betrayers)
            self.stats.PointsForGO += Const.SCORE_FOR_EACH_TRAITOR
            self.stats.PointsForGO += Const.SCORE_FOR_ALL_TRAITORS / len(self.betrayers)

        self.stats.GAMEOVERS.append(len(self.betrayers))    
#        print ("  Isl {}.{} : GAME OVER for {}".format(
#            self.context.game.phaseIndex,
#            self.islandIndex,
#            " ".join(p.id for p in self.activePlayers.values())))

    def noWinner(self):
        self.stats.NOWINNERS += 1
#        print ("  Isl {}.{} : NO WINNER".format(
#            self.context.game.phaseIndex,
#            self.islandIndex,))


    def voteAndEliminate(self, players):
        elimination = Counter()

        for p in players:
            if (p.decision.id in list(p.id for p in players)):
                #print ("  {} votes elimination of {}".format(p.name, p.decision.name))
                elimination[p.decision] += 1
            else:
                pass
                #print ("  {} vote lost for        {}".format(p.name, p.decision.name))

#        print ("   ELIMINATION SCOREBOARD :\n     {}".format("\n     ".join(
#                "{:40} : {}".format(p.name, score) for p,score in elimination.items())))

        if (len(elimination) == 0):
            #print ("   NO VOTES FOR holders - no elimination")
            return

        ties = self.getTies(elimination)
        if (len(ties) == 1):
            self.eliminate(ties[0].id)
        else:
            self.tieBreak(ties)


    def getTies(self, eliminationCounter):
        ties = []
        mostVotes = 0
        for player,votes in eliminationCounter.items():
            if (len(ties) == 0):
                ties = [player]
                mostVotes = votes
                #print("   * leader= {:2} {}".format(mostVotes, "\n                ".join(p.name for p in ties)))

            else:
                if (votes == mostVotes):
                    ties.append(player)
                    #print("   * leader= {:2} {}".format(mostVotes, "\n                ".join(p.name for p in ties)))

                else: 
                    if (votes > mostVotes):
                        ties = [player]
                        mostVotes = votes
                        #print("   * leader= {:2} {}".format(mostVotes, "\n                ".join(p.name for p in ties)))
        return ties


    def tieBreak(self, tiedPlayers):

        #print ("-- TIE BREAK ({})".format(
        #    " ".join(p.id for p in tiedPlayers)))

        self.context.registerTies(tiedPlayers)

        elimination = Counter()

        for p in self.activePlayers.values():
            decision = p.voteForTie(self.context)
            #print ("    TIE : {} votes {}".format(p.name, decision.name))
            if (decision.id in list(pc.id for pc in tiedPlayers)):
                elimination[decision] += 1
            else:
                print (" !! Invalid tie vote {} for {} - VOTE SELF".format(
                    p.name,
                    decision.name
                    ))
                elimination[p] += 1


        tiedAgain =  self.getTies(elimination)
        for bye in tiedAgain:
            self.eliminate(bye.id)


    def scoreBoard(self):
        #displayBoard = "\n\n-------SCORE BOARD for Island #{}\n".format(self.islandIndex)
        orderedPlayers = sorted(self.allPlayers.values(), key=lambda p: p.score, reverse=True)
        
        displayBoard += "\n".join(p.describe() for p in orderedPlayers)

        return displayBoard



    def roundHeader(self):
        return "-- Isl {}.{} - ROUND with {}/{}/{} (total {}) players".format(
                    self.context.game.phaseIndex, 
                    self.islandIndex,
                    len(self.activePlayers),
                    len(self.betrayers),
                    len(self.eliminatedPlayers),
                    len(self.allPlayers)
            )
