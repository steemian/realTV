from enum import Enum

from Game.Player import Player



class PlayerContext:



    def __init__(self, player):
        self.id = player.id
        self.previousMoves = []


class Context:

    def __init__(self, players, islandIndex, totalBots, totalHumans):
        self.payouts = []
        self.playerContexts = {}
        self.roundIndex = 0
        self.phaseIndex = 0
        self.islandIndex = islandIndex
        self.totalBots = totalBots
        self.totalHumans = totalHumans
        for p in players:
            self.playerContexts[p.id] = PlayerContext(p)


    def update(self, players, payout):
        raise Error("Not implemented")
        self.payouts.append(payout)
        for p in players:   
            c = self.playerContexts[p.id]
            c.previousMoves.append(p.action)
            c.wealth = p.wealth
        
        print (self.describe())


    def describe(self):

        raise Error("Not implemented")
        lastPayout = "{:3.2f}".format(self.payouts[-1]) if (len(self.payouts) > 0) else "N/A"

        description = "  TABLE {:2}  ROUND {}.{}  - pays {} each - Hum/Bots = {:2}/{:2}\n".format(
                self.tableIndex, 
                self.phaseIndex, 
                self.roundIndex, 
                lastPayout, 
                self.totalHumans, 
                self.totalBots)

        for p in self.playerContexts.values():
            description += "     {:6}  {:<4.2f} \t-  [{}];\n".format(
                p.id,
                p.wealth,
                " ".join(m.asChar() for m in p.previousMoves)
                )

        return description


                
