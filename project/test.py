from __future__ import print_function

import random
import datetime
import sys


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

    players = [] 
    for i in range(0,5):
        players.append(SimpleExample("Suicide {}".format(i), 100))
        players.append(RandomPlayer( "Rand    {}".format(i), 100))
        players.append(BotPareto(    "Pareto  {}".format(i), 100))

    gameContext = GameContext(0, 0, 3)    
    t = Island(players, "testIsland", 0, gameContext)
    t.playUntilLastMan()

    print (t.scoreBoard())

#smokeTest()
instantiateGame()



print ("\n\n\n------------------------------------\n\n")


