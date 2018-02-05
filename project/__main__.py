from __future__ import print_function

import random
import datetime
import sys
from collections import Counter


from Game import *
from Contrib import *

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def run():
    eprint("Running game .. please wait")
    print ("----- Game run on {}".format("now()"))

    a = Arena()
    a.runArena()
    a.displayResults()

    eprint("... DONE !!")



run()

