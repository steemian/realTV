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
    for i in range(0,3):
        players.append(SimpleExample("Bot {}".format(i), 100))
    t = Island(players, "testIsland", 0, 0, 3)
    t.playUntilLastMan(0)


smokeTest()
#populateTable()
#tablesDispatch()
#fullGame()
#instantiateGame()