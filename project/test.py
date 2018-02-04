from __future__ import print_function

import random
import datetime
import sys
from collections import Counter


from Game import *
from Contrib import *

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)






def smokeTest():
    print ("Smoke Test")
    players = [] 
    for i in range(0,5):
        players.append(SimpleExample("Suicide {}".format(i), 100))
        players.append(RandomPlayer( "Rand    {}".format(i), 100))

    gameContext = GameContext(0, 0, 3)    
    t = Island(players, "testIsland", 0, gameContext)
    t.playUntilLastMan()

    print (t.scoreBoard())

def instantiateGame():
    print ("instantiateGame")

    a = Arena()
    a.runArena()
    a.displayResults()



def manyRuns():

    totalScores = Counter()
    ranks = {}
    for p in Arena.availablePlayers:
        ranks[p.__name__] = []


    for i in range(0, 100   ):
        a = Arena()
        a.runArena()

        # Accumulate scores
        localScores = Counter()
        for p in a.humans:
            totalScores[type(p).__name__] += p.score
            localScores[type(p).__name__] += p.score

        # Record ranks
        sortedScores = sorted(localScores, key=lambda k : localScores[k], reverse=True   )
        curRank = 1
        for k in sortedScores:
            ranks[k].append(curRank)
            curRank += 1

    eprintscores(totalScores, "Iteration {}".format(i))
    eprintRanks(ranks, "Iteration {}".format(i))


def eprintRanks(ranks, comment):

    eprint("\n RANKS {}".format(comment))
    for player,rk in ranks.items():
        eprint("{:30} - {}".format(player, " ".join(str(i) for i in rk )))



def eprintscores(scores, comment):
    sortedScores = sorted(scores, key=lambda k : scores[k], reverse=True   )
    index = 1
    eprint("\n SCORES {}".format(comment))
    for k in sortedScores:  
        eprint ("{:3} - {:3}   {}".format(index, scores[k], k))
        index += 1


#smokeTest()
#instantiateGame()
manyRuns()

